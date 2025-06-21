import logging
import math
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Tuple, Union

logger = logging.getLogger(__name__)

class SpaceEnvironment:
    """
    Modelado del entorno espacial para simulación y análisis.
    
    Proporciona modelos para:
    - Radiación espacial
    - Campo magnético terrestre
    - Densidad atmosférica
    - Debris espacial
    - Eventos solares
    """
    
    def __init__(self):
        logger.info("Initializing Space Environment module")
        
        # Inicializar modelos
        self._init_radiation_model()
        self._init_magnetic_field_model()
        self._init_atmospheric_model()
        self._init_debris_model()
        self._init_solar_model()
    
    def _init_radiation_model(self):
        """Inicializa el modelo de radiación espacial"""
        # Coeficientes para el modelo de cinturones de Van Allen
        self.radiation_params = {
            "inner_belt_peak": 2.5,  # Radio terrestre
            "outer_belt_peak": 5.0,  # Radio terrestre
            "inner_belt_intensity": 1000.0,  # rad/año
            "outer_belt_intensity": 200.0,  # rad/año
            "solar_cycle_phase": 0.5  # 0-1, posición en el ciclo solar
        }
    
    def _init_magnetic_field_model(self):
        """Inicializa el modelo de campo magnético terrestre"""
        # Coeficientes para el modelo dipolar
        self.magnetic_params = {
            "dipole_moment": 7.94e22,  # A·m²
            "dipole_tilt": 11.0,  # grados
            "dipole_offset": [0.0, 0.0, 0.07]  # Desplazamiento del centro en radios terrestres
        }
    
    def _init_atmospheric_model(self):
        """Inicializa el modelo atmosférico"""
        # Parámetros para el modelo exponencial simple
        self.atmo_params = {
            "base_density": 1.225,  # kg/m³ a nivel del mar
            "scale_height": 8500.0,  # m
            "f10_7": 150.0,  # Flujo solar en 10.7 cm (SFU)
            "geomagnetic_index": 3.0  # Índice Ap
        }
    
    def _init_debris_model(self):
        """Inicializa el modelo de debris espacial"""
        # Parámetros para el modelo de densidad de debris
        self.debris_params = {
            "leo_density": 1e-6,  # objetos/km³ en LEO
            "meo_density": 1e-8,  # objetos/km³ en MEO
            "geo_density": 1e-9,  # objetos/km³ en GEO
            "size_distribution": [0.7, 0.2, 0.1]  # Distribución por tamaños (pequeño, mediano, grande)
        }
    
    def _init_solar_model(self):
        """Inicializa el modelo de actividad solar"""
        # Parámetros para el modelo de ciclo solar
        self.solar_params = {
            "cycle_length": 11.0,  # años
            "current_year": datetime.now().year,
            "cycle_start": 2020.0,  # Año de inicio del ciclo actual
            "max_sunspot_number": 180.0,
            "current_sunspot_number": 120.0,
            "flare_probability": 0.05  # Probabilidad diaria de llamarada solar
        }
    
    def calculate_radiation_dose(self, position: np.ndarray, 
                               shielding: float = 1.0) -> float:
        """
        Calcula la dosis de radiación en una posición dada.
        
        Args:
            position: Vector de posición [x, y, z] en metros
            shielding: Factor de blindaje (1.0 = sin blindaje adicional)
            
        Returns:
            Dosis de radiación en rad/día
        """
        # Convertir posición a radios terrestres
        r_earth = 6371000.0  # m
        pos_re = np.linalg.norm(position) / r_earth
        
        # Calcular contribución de los cinturones de Van Allen
        inner_belt = self.radiation_params["inner_belt_intensity"] * \
                    math.exp(-((pos_re - self.radiation_params["inner_belt_peak"]) ** 2) / 0.5)
        
        outer_belt = self.radiation_params["outer_belt_intensity"] * \
                    math.exp(-((pos_re - self.radiation_params["outer_belt_peak"]) ** 2) / 2.0)
        
        # Calcular contribución de rayos cósmicos (disminuye con la proximidad a la Tierra)
        cosmic_rays = 50.0 * (1.0 - math.exp(-0.4 * (pos_re - 1.0)))
        
        # Calcular contribución solar (varía con el ciclo solar)
        solar_factor = 0.5 + 0.5 * math.sin(2 * math.pi * self.radiation_params["solar_cycle_phase"])
        solar_radiation = 30.0 * solar_factor
        
        # Calcular dosis total
        total_dose = (inner_belt + outer_belt + cosmic_rays + solar_radiation) / shielding
        
        return max(0.0, total_dose)
    
    def calculate_magnetic_field(self, position: np.ndarray) -> np.ndarray:
        """
        Calcula el campo magnético terrestre en una posición dada.
        
        Args:
            position: Vector de posición [x, y, z] en metros
            
        Returns:
            Vector de campo magnético [Bx, By, Bz] en nT
        """
        # Convertir posición a radios terrestres
        r_earth = 6371000.0  # m
        pos_re = position / r_earth
        
        # Aplicar desplazamiento del dipolo
        pos_re = pos_re - self.magnetic_params["dipole_offset"]
        
        # Calcular distancia al centro
        r = np.linalg.norm(pos_re)
        
        if r < 1.0:
            # Dentro de la Tierra, campo no definido correctamente
            return np.array([0.0, 0.0, 0.0])
        
        # Convertir coordenadas a esféricas
        theta = math.acos(pos_re[2] / r)  # Colatitud
        phi = math.atan2(pos_re[1], pos_re[0])  # Longitud
        
        # Aplicar inclinación del dipolo
        tilt_rad = math.radians(self.magnetic_params["dipole_tilt"])
        theta_m = theta + tilt_rad * math.sin(phi)
        
        # Calcular componentes del campo en coordenadas esféricas
        B_r = -2.0 * self.magnetic_params["dipole_moment"] * math.cos(theta_m) / (r ** 3)
        B_theta = -self.magnetic_params["dipole_moment"] * math.sin(theta_m) / (r ** 3)
        B_phi = 0.0
        
        # Convertir a coordenadas cartesianas
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)
        sin_phi = math.sin(phi)
        cos_phi = math.cos(phi)
        
        B_x = B_r * sin_theta * cos_phi + B_theta * cos_theta * cos_phi - B_phi * sin_phi
        B_y = B_r * sin_theta * sin_phi + B_theta * cos_theta * sin_phi + B_phi * cos_phi
        B_z = B_r * cos_theta - B_theta * sin_theta
        
        # Convertir a nanoteslas
        B = np.array([B_x, B_y, B_z]) * 1e9
        
        return B
    
    def calculate_atmospheric_density(self, altitude: float, 
                                    latitude: float = 0.0, 
                                    local_time: float = 12.0) -> float:
        """
        Calcula la densidad atmosférica a una altitud dada.
        
        Args:
            altitude: Altitud en metros
            latitude: Latitud en grados
            local_time: Hora local (0-24)
            
        Returns:
            Densidad atmosférica en kg/m³
        """
        if altitude < 0:
            return self.atmo_params["base_density"]
        
        # Modelo exponencial básico
        density = self.atmo_params["base_density"] * math.exp(-altitude / self.atmo_params["scale_height"])
        
        # Corrección por actividad solar
        f10_factor = (self.atmo_params["f10_7"] / 150.0) ** 0.25
        density *= f10_factor
        
        # Corrección por variación diurna
        diurnal_factor = 1.0 + 0.2 * math.sin(2 * math.pi * (local_time - 14.0) / 24.0)
        density *= diurnal_factor
        
        # Corrección por latitud
        latitude_rad = math.radians(latitude)
        latitude_factor = 1.0 + 0.1 * math.sin(latitude_rad) ** 2
        density *= latitude_factor
        
        return density
    
    def calculate_debris_risk(self, position: np.ndarray, 
                            cross_section: float = 1.0) -> Dict[str, float]:
        """
        Calcula el riesgo de colisión con debris espacial.
        
        Args:
            position: Vector de posición [x, y, z] en metros
            cross_section: Sección transversal de la nave en m²
            
        Returns:
            Diccionario con métricas de riesgo
        """
        # Convertir posición a radios terrestres
        r_earth = 6371000.0  # m
        altitude = np.linalg.norm(position) - r_earth
        
        # Determinar región orbital
        if altitude < 2000000:  # 2000 km
            region = "leo"
            density = self.debris_params["leo_density"]
        elif altitude < 35000000:  # 35000 km
            region = "meo"
            density = self.debris_params["meo_density"]
        else:
            region = "geo"
            density = self.debris_params["geo_density"]
        
        # Calcular probabilidad de colisión
        # P = 1 - exp(-density * cross_section * velocity * time)
        # Asumiendo velocidad relativa de 10 km/s y período de 1 día
        velocity = 10000.0  # m/s
        time = 86400.0  # s (1 día)
        
        collision_probability = 1.0 - math.exp(-density * cross_section * velocity * time)
        
        # Calcular riesgo por tamaño de debris
        risk_by_size = {
            "small": collision_probability * self.debris_params["size_distribution"][0],
            "medium": collision_probability * self.debris_params["size_distribution"][1],
            "large": collision_probability * self.debris_params["size_distribution"][2]
        }
        
        # Calcular riesgo total ponderado
        # Los debris pequeños son menos dañinos que los grandes
        risk_weights = {"small": 0.2, "medium": 0.6, "large": 1.0}
        weighted_risk = sum(risk_by_size[size] * risk_weights[size] for size in risk_by_size)
        
        return {
            "region": region,
            "collision_probability": collision_probability,
            "risk_by_size": risk_by_size,
            "weighted_risk": weighted_risk
        }
    
    def predict_solar_activity(self, date: datetime) -> Dict[str, Any]:
        """
        Predice la actividad solar para una fecha dada.
        
        Args:
            date: Fecha para la predicción
            
        Returns:
            Diccionario con métricas de actividad solar
        """
        # Calcular fase en el ciclo solar
        years_since_start = date.year + date.timetuple().tm_yday / 365.0 - self.solar_params["cycle_start"]
        cycle_phase = (years_since_start % self.solar_params["cycle_length"]) / self.solar_params["cycle_length"]
        
        # Modelar número de manchas solares con una curva sinusoidal
        sunspot_number = self.solar_params["max_sunspot_number"] * \
                        math.sin(math.pi * cycle_phase) ** 2
        
        # Calcular flujo solar F10.7 (correlacionado con el número de manchas)
        f10_7 = 60.0 + 1.0 * sunspot_number
        
        # Calcular probabilidad de llamarada solar
        base_flare_probability = self.solar_params["flare_probability"]
        flare_probability = base_flare_probability * (0.5 + 0.5 * math.sin(math.pi * cycle_phase) ** 2)
        
        # Calcular probabilidad de eyección de masa coronal (CME)
        cme_probability = flare_probability * 0.3
        
        # Calcular índice geomagnético Ap (correlacionado con la actividad solar)
        ap_index = 5.0 + 20.0 * math.sin(math.pi * cycle_phase) ** 2
        
        return {
            "date": date.isoformat(),
            "cycle_phase": cycle_phase,
            "sunspot_number": sunspot_number,
            "f10_7_flux": f10_7,
            "flare_probability": flare_probability,
            "cme_probability": cme_probability,
            "ap_index": ap_index
        }
    
    def simulate_space_weather(self, start_date: datetime, 
                             days: int = 30) -> List[Dict[str, Any]]:
        """
        Simula condiciones de clima espacial para un período.
        
        Args:
            start_date: Fecha de inicio
            days: Número de días a simular
            
        Returns:
            Lista de condiciones diarias
        """
        results = []
        
        # Obtener predicción base para el inicio
        base_prediction = self.predict_solar_activity(start_date)
        base_flare_prob = base_prediction["flare_probability"]
        base_cme_prob = base_prediction["cme_probability"]
        
        # Simular cada día
        for day in range(days):
            current_date = start_date + timedelta(days=day)
            
            # Obtener predicción para el día actual
            prediction = self.predict_solar_activity(current_date)
            
            # Añadir variabilidad aleatoria
            random_factor = 0.8 + 0.4 * np.random.random()
            prediction["sunspot_number"] *= random_factor
            prediction["f10_7_flux"] = 60.0 + 1.0 * prediction["sunspot_number"]
            
            # Simular ocurrencia de llamaradas solares
            flares = []
            flare_classes = ["C", "M", "X"]
            flare_probs = [0.7, 0.25, 0.05]  # Distribución de clases
            
            # Número de llamaradas (distribución de Poisson)
            flare_lambda = prediction["flare_probability"] * 3.0  # Esperanza matemática
            num_flares = np.random.poisson(flare_lambda)
            
            for _ in range(num_flares):
                # Determinar clase de llamarada
                flare_class = np.random.choice(flare_classes, p=flare_probs)
                
                # Determinar magnitud dentro de la clase
                if flare_class == "C":
                    magnitude = 1.0 + 9.0 * np.random.random()
                elif flare_class == "M":
                    magnitude = 1.0 + 9.0 * np.random.random()
                else:  # X
                    magnitude = 1.0 + 9.0 * np.random.random()
                
                # Hora de la llamarada
                hour = np.random.randint(0, 24)
                minute = np.random.randint(0, 60)
                
                flares.append({
                    "class": flare_class,
                    "magnitude": magnitude,
                    "time": f"{hour:02d}:{minute:02d} UTC"
                })
            
            # Simular eyecciones de masa coronal
            cmes = []
            if np.random.random() < prediction["cme_probability"]:
                # Velocidad de la CME
                velocity = 500.0 + 1500.0 * np.random.random()  # km/s
                
                # Dirección (ángulo respecto al plano eclíptico)
                direction = -90.0 + 180.0 * np.random.random()  # grados
                
                # Probabilidad de impacto con la Tierra
                earth_impact_prob = max(0.0, 1.0 - abs(direction) / 45.0)
                
                # Tiempo estimado de llegada si hay impacto
                if earth_impact_prob > 0:
                    # Distancia Sol-Tierra: ~150 millones de km
                    travel_time_hours = 150000000.0 / (velocity * 3600.0)
                    arrival_time = current_date + timedelta(hours=travel_time_hours)
                else:
                    arrival_time = None
                
                cmes.append({
                    "velocity": velocity,
                    "direction": direction,
                    "earth_impact_probability": earth_impact_prob,
                    "estimated_arrival": arrival_time.isoformat() if arrival_time else None
                })
            
            # Añadir resultado del día
            daily_result = {
                "date": current_date.isoformat(),
                "sunspot_number": prediction["sunspot_number"],
                "f10_7_flux": prediction["f10_7_flux"],
                "ap_index": prediction["ap_index"],
                "flares": flares,
                "cmes": cmes
            }
            
            results.append(daily_result)
        
        return results
    
    def evaluate_mission_environment(self, orbit_params: Dict[str, float], 
                                   mission_duration: int,
                                   spacecraft_properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evalúa las condiciones ambientales para una misión espacial.
        
        Args:
            orbit_params: Parámetros orbitales
            mission_duration: Duración de la misión en días
            spacecraft_properties: Propiedades de la nave
            
        Returns:
            Evaluación de riesgos y condiciones ambientales
        """
        # Extraer parámetros relevantes
        semi_major_axis = orbit_params.get("semi_major_axis", 0.0)
        eccentricity = orbit_params.get("eccentricity", 0.0)
        inclination = orbit_params.get("inclination", 0.0)
        
        # Calcular altitud de perigeo y apogeo
        r_earth = 6371000.0  # m
        perigee_altitude = semi_major_axis * (1.0 - eccentricity) - r_earth
        apogee_altitude = semi_major_axis * (1.0 + eccentricity) - r_earth
        
        # Extraer propiedades de la nave
        cross_section = spacecraft_properties.get("cross_section", 1.0)
        shielding = spacecraft_properties.get("radiation_shielding", 1.0)
        
        # Evaluar radiación
        # Posición en el perigeo (punto más cercano a la Tierra)
        perigee_position = np.array([perigee_altitude + r_earth, 0.0, 0.0])
        radiation_dose_perigee = self.calculate_radiation_dose(perigee_position, shielding)
        
        # Posición en el apogeo (punto más lejano de la Tierra)
        apogee_position = np.array([apogee_altitude + r_earth, 0.0, 0.0])
        radiation_dose_apogee = self.calculate_radiation_dose(apogee_position, shielding)
        
        # Dosis promedio
        avg_radiation_dose = (radiation_dose_perigee + radiation_dose_apogee) / 2.0
        total_mission_dose = avg_radiation_dose * mission_duration
        
        # Evaluar riesgo de debris
        debris_risk_perigee = self.calculate_debris_risk(perigee_position, cross_section)
        debris_risk_apogee = self.calculate_debris_risk(apogee_position, cross_section)
        
        # Probabilidad acumulada de colisión durante la misión
        collision_prob_daily = (debris_risk_perigee["collision_probability"] + 
                              debris_risk_apogee["collision_probability"]) / 2.0
        mission_collision_prob = 1.0 - (1.0 - collision_prob_daily) ** mission_duration
        
        # Evaluar clima espacial
        start_date = datetime.now()
        space_weather = self.simulate_space_weather(start_date, min(30, mission_duration))
        
        # Contar eventos significativos
        num_x_flares = sum(1 for day in space_weather 
                         for flare in day["flares"] 
                         if flare["class"] == "X")
        
        num_earth_directed_cmes = sum(1 for day in space_weather 
                                   for cme in day["cmes"] 
                                   if cme.get("earth_impact_probability", 0) > 0.5)
        
        # Calcular índices de riesgo
        radiation_risk = min(1.0, total_mission_dose / 1000.0)  # Normalizado a 1000 rad
        debris_risk = mission_collision_prob
        space_weather_risk = min(1.0, (num_x_flares + 2 * num_earth_directed_cmes) / 10.0)
        
        # Riesgo total
        total_risk = 0.4 * radiation_risk + 0.4 * debris_risk + 0.2 * space_weather_risk
        
        # Clasificar riesgo
        if total_risk < 0.3:
            risk_category = "low"
        elif total_risk < 0.6:
            risk_category = "medium"
        else:
            risk_category = "high"
        
        return {
            "mission_parameters": {
                "orbit": {
                    "semi_major_axis": semi_major_axis,
                    "eccentricity": eccentricity,
                    "inclination": inclination,
                    "perigee_altitude": perigee_altitude,
                    "apogee_altitude": apogee_altitude
                },
                "duration": mission_duration,
                "spacecraft": spacecraft_properties
            },
            "radiation_assessment": {
                "perigee_dose_rate": radiation_dose_perigee,
                "apogee_dose_rate": radiation_dose_apogee,
                "average_dose_rate": avg_radiation_dose,
                "total_mission_dose": total_mission_dose,
                "risk_factor": radiation_risk
            },
            "debris_assessment": {
                "perigee_risk": debris_risk_perigee["weighted_risk"],
                "apogee_risk": debris_risk_apogee["weighted_risk"],
                "mission_collision_probability": mission_collision_prob,
                "risk_factor": debris_risk
            },
            "space_weather_assessment": {
                "x_flares_expected": num_x_flares * (mission_duration / len(space_weather)),
                "earth_directed_cmes_expected": num_earth_directed_cmes * (mission_duration / len(space_weather)),
                "risk_factor": space_weather_risk
            },
            "overall_assessment": {
                "total_risk_factor": total_risk,
                "risk_category": risk_category,
                "recommendations": self._generate_recommendations(total_risk, radiation_risk, 
                                                               debris_risk, space_weather_risk)
            }
        }
    
    def _generate_recommendations(self, total_risk: float, radiation_risk: float,
                               debris_risk: float, space_weather_risk: float) -> List[str]:
        """Genera recomendaciones basadas en la evaluación de riesgos"""
        recommendations = []
        
        # Recomendaciones generales
        if total_risk > 0.7:
            recommendations.append("Considerar rediseño de la misión para reducir exposición a riesgos ambientales")
        
        # Recomendaciones específicas para radiación
        if radiation_risk > 0.6:
            recommendations.append("Aumentar blindaje contra radiación en componentes críticos")
            recommendations.append("Implementar redundancia en sistemas sensibles a radiación")
        elif radiation_risk > 0.3:
            recommendations.append("Monitorear dosis de radiación acumulada durante la misión")
        
        # Recomendaciones específicas para debris
        if debris_risk > 0.5:
            recommendations.append("Implementar capacidad de maniobra evasiva para debris detectables")
            recommendations.append("Considerar órbita alternativa con menor densidad de debris")
        elif debris_risk > 0.2:
            recommendations.append("Mantener sistema de alerta temprana para conjunciones con debris catalogados")
        
        # Recomendaciones específicas para clima espacial
        if space_weather_risk > 0.5:
            recommendations.append("Implementar modo seguro automático durante tormentas solares severas")
            recommendations.append("Aumentar margen de radiación en componentes electrónicos")
        elif space_weather_risk > 0.2:
            recommendations.append("Monitorear predicciones de clima espacial durante la misión")
        
        return recommendations
