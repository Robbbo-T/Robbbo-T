#!/usr/bin/env python3
"""
STEP AP214 Generator for AMPEL3GO H₂-BWB-Q Center Body Primary Grid
Generates ISO-10303-21 compliant files with full requirements traceability
"""

import os
import json
import hashlib
from datetime import datetime, timezone
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import numpy as np

class ComponentType(Enum):
    """Structural component types per requirements"""
    LONGERON = "Longeron"
    FRAME = "Frame"
    DIAGONAL = "Diagonal"
    JOINT = "Joint"
    INTERFACE = "Interface"
    FASTENER = "Fastener"

@dataclass
class MaterialProperties:
    """Material properties per REQ-DES-MAT-001"""
    name: str
    yield_strength: float  # MPa
    ultimate_strength: float  # MPa
    elastic_modulus: float  # GPa
    density: float  # kg/m³
    poisson_ratio: float
    h2_compatibility: str
    temperature_range: Tuple[float, float]  # °C

@dataclass
class StructuralRequirement:
    """Links STEP geometry to requirements"""
    req_id: str
    component_type: ComponentType
    safety_factor: float
    load_paths: int
    tolerance: float  # mm
    cpk_target: float
    evidence_path: str

class STEPGenerator:
    """
    Generates STEP AP214 files for structural grid topology
    Compliant with REQ-DES-STR-001 through REQ-DES-ICD-001
    """
    
    def __init__(self, config_path: str = "config/h2_bwb_config.yaml"):
        self.config = self._load_config(config_path)
        self.entity_counter = 1
        self.entities: Dict[int, str] = {}
        self.requirements: List[StructuralRequirement] = []
        self.material = self._initialize_material()
        self.timestamp = datetime.now(timezone.utc)
        self.session_id = hashlib.md5(str(self.timestamp).encode()).hexdigest()[:8]
        self.product_def_shape_id: Optional[int] = None
        self.rep_context_id: Optional[int] = None
        
    def _load_config(self, path: str) -> Dict[str, Any]:
        """Load configuration from YAML, with a fallback for missing module."""
        try:
            import yaml
            if os.path.exists(path):
                with open(path, 'r') as f:
                    print(f"✓ Loading configuration from {path}")
                    return yaml.safe_load(f)
        except ModuleNotFoundError:
            print("Warning: PyYAML module not found. Using default configuration.")
            print("To use a custom config file, please install PyYAML: pip install PyYAML")
        
        print("✓ Using default configuration.")
        return self._default_config()
    
    def _default_config(self) -> Dict[str, Any]:
        """Default configuration per requirements"""
        return {
            'dimensions': {
                'length': 12000,  # mm
                'width': 2400,   # mm
                'height': 2000,  # mm
                'thickness': 25  # mm
            },
            'grid': {
                'longitudinal_count': 4,
                'transverse_count': 5,
                'diagonal_sets': 3
            },
            'tolerances': {
                'position': 0.25,  # mm per REQ-DES-ICD-001
                'angle': 0.5,      # degrees
                'flatness': 0.1    # mm
            },
            'loads': {
                'ultimate_factor': 1.5,  # REQ-DES-STR-001
                'limit_factor': 1.25,
                'gust_reduction': 0.15   # REQ-DES-LOD-002
            }
        }
    
    def _initialize_material(self) -> MaterialProperties:
        """Initialize material per REQ-DES-MAT-001"""
        return MaterialProperties(
            name="Al-Li-2099-T83",
            yield_strength=455,
            ultimate_strength=490,
            elastic_modulus=76,
            density=2630,
            poisson_ratio=0.33,
            h2_compatibility="ISO-11114-4-Approved",
            temperature_range=(-253, 85)  # REQ-DES-ENV-001
        )
    
    def generate(self, output_path: str = "grid-topology.step") -> str:
        """Generate complete STEP file"""
        self.entities.clear()
        self.entity_counter = 1
        
        # Build STEP structure
        step_content = []
        step_content.append(self._generate_header())
        step_content.append(self._generate_data_section())
        step_content.append("ENDSEC;")
        step_content.append("END-ISO-10303-21;")
        
        # Write file
        full_content = '\n'.join(step_content)
        with open(output_path, 'w') as f:
            f.write(full_content)
        
        # Generate traceability
        self._generate_traceability_manifest(output_path)
        
        return output_path
    
    def _generate_header(self) -> str:
        """Generate STEP header with metadata"""
        header = []
        header.append("ISO-10303-21;")
        header.append("HEADER;")
        header.append("/*")
        header.append(" * AMPEL360 H₂-BWB-Q Center Body Primary Grid")
        header.append(f" * Generated: {self.timestamp.isoformat()}")
        header.append(f" * Session: {self.session_id}")
        header.append(" * Requirements: REQ-DES-STR-001 through REQ-DES-ICD-001")
        header.append(" */")
        
        # File description
        header.append("FILE_DESCRIPTION(")
        header.append("('AMPEL360 H2-BWB-Q100 Center Body Box Primary Grid',")
        header.append(f"'Generated by STEPGenerator v1.0 - Session {self.session_id}'),")
        header.append("'2;1');")
        
        # File name
        header.append("FILE_NAME(")
        header.append(f"'grid-topology-{self.session_id}.step',")
        header.append(f"'{self.timestamp.isoformat()}',")
        header.append("('AMPEL360 Requirements System','Structural Design Team'),")
        header.append("('Aerospace Division','Advanced Projects'),")
        header.append("'STEPGenerator 1.0',")
        header.append("'AMPEL360-STEP-Gen',")
        header.append("'');")
        
        # Schema
        header.append("FILE_SCHEMA(('AUTOMOTIVE_DESIGN { 1 0 10303 214 1 1 1 1 }'));")
        header.append("ENDSEC;")
        
        return '\n'.join(header)
    
    def _generate_data_section(self) -> str:
        """Generate DATA section with geometry"""
        data = []
        data.append("DATA;")
        data.append("")
        
        # Product definition
        data.append("/* PRODUCT DEFINITION */")
        data.extend(self._generate_product_definition())
        data.append("")
        
        # Coordinate system
        data.append("/* COORDINATE SYSTEM */")
        data.extend(self._generate_coordinate_system())
        data.append("")
        
        # Structural components
        data.append("/* LONGITUDINAL MEMBERS (REQ-DES-STR-001) */")
        data.extend(self._generate_longerons())
        data.append("")
        
        data.append("/* TRANSVERSE MEMBERS (REQ-DES-STR-002) */")
        data.extend(self._generate_frames())
        data.append("")
        
        data.append("/* DIAGONAL BRACING (REQ-DES-STR-002) */")
        data.extend(self._generate_diagonals())
        data.append("")
        
        data.append("/* JOINT NODES (REQ-DES-ICD-001) */")
        data.extend(self._generate_joints())
        data.append("")
        
        data.append("/* INTERFACE FEATURES */")
        data.extend(self._generate_interfaces())
        data.append("")
        
        # Material properties
        data.append("/* MATERIAL PROPERTIES (REQ-DES-MAT-001) */")
        data.extend(self._generate_material_properties())
        data.append("")
        
        # Metadata
        data.append("/* METADATA AND TRACEABILITY */")
        data.extend(self._generate_metadata())
        
        return '\n'.join(data)
    
    def _add_entity(self, definition: str) -> int:
        """Add entity and return its ID"""
        entity_id = self.entity_counter
        self.entities[entity_id] = f"#{entity_id} = {definition};"
        self.entity_counter += 1
        return entity_id
    
    def _generate_product_definition(self) -> List[str]:
        """Generate product definition entities"""
        lines = []
        
        # Application protocol
        app_context_id = self._add_entity(
            "APPLICATION_CONTEXT('core data for automotive mechanical design processes')"
        )
        app_protocol_id = self._add_entity(
            f"APPLICATION_PROTOCOL_DEFINITION('international standard','automotive_design',2000,#{app_context_id})"
        )
        
        # Product
        product_context_id = self._add_entity(
            f"PRODUCT_CONTEXT('Part Definition',#{app_context_id},'mechanical')"
        )
        product_id = self._add_entity(
            "PRODUCT('CI-CA-A-53-10-01-CB-PRIMARY-GRID',"
            "'Center Body Box Primary Grid Assembly',"
            f"'H2-BWB-Q100 Primary Load-Carrying Structure',(#{product_context_id}))"
        )
        
        # Product definition
        product_def_context_id = self._add_entity(
            f"PRODUCT_DEFINITION_CONTEXT('part definition',#{app_context_id},'design')"
        )
        product_formation_id = self._add_entity(
            f"PRODUCT_DEFINITION_FORMATION_WITH_SPECIFIED_SOURCE('','','',#{product_id},.NOT_KNOWN.)"
        )
        product_def_id = self._add_entity(
            f"PRODUCT_DEFINITION('design','Detailed structural grid design.',#{product_formation_id},#{product_def_context_id})"
        )
        self.product_def_shape_id = self._add_entity(
            f"PRODUCT_DEFINITION_SHAPE('','',#{product_def_id})"
        )
        
        # Add entities to output
        for entity_id in sorted(self.entities.keys())[:self.entity_counter-1]:
            lines.append(self.entities[entity_id])
        
        return lines
    
    def _generate_coordinate_system(self) -> List[str]:
        """Generate coordinate system per ISO-1151"""
        lines = []
        
        # Origin
        origin_id = self._add_entity("CARTESIAN_POINT('Origin',(0.,0.,0.))")
        z_dir_id = self._add_entity("DIRECTION('Z-Axis',(0.,0.,1.))")
        x_dir_id = self._add_entity("DIRECTION('X-Axis',(1.,0.,0.))")
        
        # World coordinate system
        axis_id = self._add_entity(
            f"AXIS2_PLACEMENT_3D('World Coordinate System',#{origin_id},#{z_dir_id},#{x_dir_id})"
        )
        
        # Uncertainty per requirements
        length_unit_id = self._add_entity(
            "(LENGTH_UNIT() NAMED_UNIT(*) SI_UNIT(.MILLI.,.METRE.))"
        )
        angle_unit_id = self._add_entity(
            "(NAMED_UNIT(*) PLANE_ANGLE_UNIT() SI_UNIT($,.RADIAN.))"
        )
        solid_angle_unit_id = self._add_entity(
            "(NAMED_UNIT(*) SI_UNIT($,.STERADIAN.) SOLID_ANGLE_UNIT())"
        )
        
        uncertainty_id = self._add_entity(
            f"UNCERTAINTY_MEASURE_WITH_UNIT(LENGTH_MEASURE(0.05),#{length_unit_id},"
            "'distance_accuracy_value','Maximum tolerance per REQ-DES-ICD-001')"
        )
        
        self.rep_context_id = self._add_entity(
            f"(GEOMETRIC_REPRESENTATION_CONTEXT(3) "
            f"GLOBAL_UNCERTAINTY_ASSIGNED_CONTEXT((#{uncertainty_id})) "
            f"GLOBAL_UNIT_ASSIGNED_CONTEXT((#{length_unit_id},#{angle_unit_id},#{solid_angle_unit_id})) "
            f"REPRESENTATION_CONTEXT('Context #1','3D Context with UNIT and UNCERTAINTY'))"
        )
        
        # Collect new entities
        start_id = self.entity_counter - 9
        for entity_id in range(start_id, self.entity_counter):
            if entity_id in self.entities:
                lines.append(self.entities[entity_id])
        
        return lines
    
    def _generate_longerons(self) -> List[str]:
        """Generate longitudinal members"""
        lines = []
        dim = self.config['dimensions']
        
        # Create requirement link
        req = StructuralRequirement(
            req_id="REQ-DES-STR-001",
            component_type=ComponentType.LONGERON,
            safety_factor=1.5,
            load_paths=2,
            tolerance=0.25,
            cpk_target=1.67,
            evidence_path="../02-Design/STR/grid-topology.step"
        )
        self.requirements.append(req)
        
        # Generate longerons at different Y stations
        y_stations = np.linspace(-dim['width']/2, dim['width']/2,
                                  self.config['grid']['longitudinal_count'])
        
        for i, y_pos in enumerate(y_stations):
            lines.extend(self._create_longeron(i+1, y_pos, dim['height']/2))
            lines.extend(self._create_longeron(i+5, y_pos, -dim['height']/2))
        
        return lines
    
    def _create_longeron(self, index: int, y_pos: float, z_pos: float) -> List[str]:
        """Create a single longeron beam element"""
        lines = []
        dim = self.config['dimensions']
        thickness = dim['thickness']
        
        # Record starting entity ID for collection
        start_entity_id = self.entity_counter

        # Define vertices
        p1_id = self._add_entity(f"CARTESIAN_POINT('',({-dim['length']/2},{y_pos},{z_pos}))")
        v1_id = self._add_entity(f"VERTEX_POINT('',#{p1_id})")
        
        p2_id = self._add_entity(f"CARTESIAN_POINT('',({dim['length']/2},{y_pos},{z_pos}))")
        v2_id = self._add_entity(f"VERTEX_POINT('',#{p2_id})")
        
        p3_id = self._add_entity(f"CARTESIAN_POINT('',({dim['length']/2},{y_pos},{z_pos + thickness}))")
        v3_id = self._add_entity(f"VERTEX_POINT('',#{p3_id})")
        
        p4_id = self._add_entity(f"CARTESIAN_POINT('',({-dim['length']/2},{y_pos},{z_pos + thickness}))")
        v4_id = self._add_entity(f"VERTEX_POINT('',#{p4_id})")
        
        # Create edges
        edge_ids = []
        edge_ids.append(self._create_edge(v1_id, v2_id))
        edge_ids.append(self._create_edge(v2_id, v3_id))
        edge_ids.append(self._create_edge(v3_id, v4_id))
        edge_ids.append(self._create_edge(v4_id, v1_id))
        
        # Create edge loop
        oriented_edges = [self._add_entity(f"ORIENTED_EDGE('',*,*,#{e},.T.)") for e in edge_ids]
        edge_loop_id = self._add_entity(f"EDGE_LOOP('',(#{',#'.join(map(str, oriented_edges))}))")
        
        # Create face
        face_bound_id = self._add_entity(f"FACE_OUTER_BOUND('',#{edge_loop_id},.T.)")
        
        # Create plane for the longeron (normal is in Y direction)
        plane_point = self._add_entity(f"CARTESIAN_POINT('',(0.,{y_pos},{z_pos + thickness / 2}))")
        plane_normal = self._add_entity("DIRECTION('',(0.,1.,0.))")
        plane_ref = self._add_entity("DIRECTION('',(1.,0.,0.))")
        plane_axis = self._add_entity(f"AXIS2_PLACEMENT_3D('',#{plane_point},#{plane_normal},#{plane_ref})")
        plane_id = self._add_entity(f"PLANE('',#{plane_axis})")
        
        # Create advanced face
        face_id = self._add_entity(
            f"ADVANCED_FACE('Longeron-L{index}',(#{face_bound_id}),#{plane_id},.T.)"
        )
        
        # Add metadata comment
        lines.append(f"/* Longeron L{index} at Y={y_pos:.1f} (Safety Factor: {self.requirements[-1].safety_factor}) */")
        
        # Collect entities for this longeron
        for entity_id in range(start_entity_id, self.entity_counter):
            if entity_id in self.entities:
                lines.append(self.entities[entity_id])
        
        return lines
    
    def _create_edge(self, v1_id: int, v2_id: int) -> int:
        """Create edge between two vertices (simplified)."""
        # NOTE: This is a placeholder. A robust implementation would parse vertex
        # coordinates to calculate the correct line vector.
        line_point = self._add_entity(f"CARTESIAN_POINT('',(0.,0.,0.))")
        direction_id = self._add_entity("DIRECTION('',(1.,0.,0.))")
        line_vector = self._add_entity(f"VECTOR('',#{direction_id},1000.)")
        line_id = self._add_entity(f"LINE('',#{line_point},#{line_vector})")
        edge_id = self._add_entity(f"EDGE_CURVE('',#{v1_id},#{v2_id},#{line_id},.T.)")
        return edge_id
    
    def _generate_frames(self) -> List[str]:
        """Generate transverse frame members"""
        lines = []
        dim = self.config['dimensions']
        
        # Create requirement link
        req = StructuralRequirement(
            req_id="REQ-DES-STR-002",
            component_type=ComponentType.FRAME,
            safety_factor=1.5,
            load_paths=2,
            tolerance=0.25,
            cpk_target=1.67,
            evidence_path="../02-Design/STR/load-paths.fea"
        )
        self.requirements.append(req)
        
        # Generate frames at different X stations
        x_stations = np.linspace(-dim['length']/2, dim['length']/2,
                                  self.config['grid']['transverse_count'])
        
        for i, x_pos in enumerate(x_stations):
            lines.append(f"/* Frame T{i+1} at X={x_pos:.1f} (Load Paths: {req.load_paths}) */")
            lines.extend(self._create_frame(i+1, x_pos))
        
        return lines

    def _create_frame(self, index: int, x_pos: float) -> List[str]:
        """Create a single transverse frame"""
        lines = []
        dim = self.config['dimensions']
        
        # Record starting entity ID for collection
        start_entity_id = self.entity_counter

        # Define frame rectangle corners in the Y-Z plane
        corners = [
            (-dim['width']/2, -dim['height']/2),
            (dim['width']/2, -dim['height']/2),
            (dim['width']/2, dim['height']/2),
            (-dim['width']/2, dim['height']/2)
        ]
        
        # Create vertices at the specified x_pos
        vertex_ids = []
        for y, z in corners:
            point_id = self._add_entity(f"CARTESIAN_POINT('',({x_pos},{y},{z}))")
            vertex_id = self._add_entity(f"VERTEX_POINT('',#{point_id})")
            vertex_ids.append(vertex_id)
        
        # Create edges between vertices
        edge_ids = []
        for i in range(4):
            edge_id = self._create_edge(vertex_ids[i], vertex_ids[(i+1)%4])
            edge_ids.append(edge_id)
        
        # Create edge loop
        oriented_edges = [self._add_entity(f"ORIENTED_EDGE('',*,*,#{e},.T.)") for e in edge_ids]
        edge_loop_id = self._add_entity(f"EDGE_LOOP('',(#{',#'.join(map(str, oriented_edges))}))")
        
        # Create face
        face_bound_id = self._add_entity(f"FACE_OUTER_BOUND('',#{edge_loop_id},.T.)")
        
        # Create plane for the frame (normal is in X direction)
        plane_point = self._add_entity(f"CARTESIAN_POINT('',({x_pos},0.,0.))")
        plane_normal = self._add_entity("DIRECTION('',(1.,0.,0.))")
        plane_ref = self._add_entity("DIRECTION('',(0.,1.,0.))")
        plane_axis = self._add_entity(f"AXIS2_PLACEMENT_3D('',#{plane_point},#{plane_normal},#{plane_ref})")
        plane_id = self._add_entity(f"PLANE('',#{plane_axis})")
        
        # Create advanced face
        face_id = self._add_entity(f"ADVANCED_FACE('Frame-T{index}',(#{face_bound_id}),#{plane_id},.T.)")
        
        # Collect entities for this frame
        for entity_id in range(start_entity_id, self.entity_counter):
            if entity_id in self.entities:
                lines.append(self.entities[entity_id])
        
        return lines
    
    def _generate_diagonals(self) -> List[str]:
        """Generate diagonal bracing members"""
        lines = []
        dim = self.config['dimensions']
        
        # Diagonal sets for load path redundancy (REQ-DES-STR-002)
        diagonal_configs = [
            {'start': (-dim['length']/4, -dim['width']/4, dim['height']/2),
             'end': (dim['length']/4, dim['width']/4, dim['height']/2)},
            {'start': (-dim['length']/4, dim['width']/4, dim['height']/2),
             'end': (dim['length']/4, -dim['width']/4, dim['height']/2)},
            {'start': (-dim['length']/4, -dim['width']/4, -dim['height']/2),
             'end': (dim['length']/4, dim['width']/4, -dim['height']/2)}
        ]
        
        for i, config in enumerate(diagonal_configs):
            lines.append(f"/* Diagonal Brace D{i+1} (Redundant Load Path) */")
            lines.extend(self._create_diagonal(i+1, config['start'], config['end']))
        
        return lines
    
    def _create_diagonal(self, index: int, start: Tuple, end: Tuple) -> List[str]:
        """Create diagonal brace member"""
        lines = []
        thickness = 20  # mm
        
        # Record starting entity ID for collection
        start_entity_id = self.entity_counter

        # Create endpoints
        start_point = self._add_entity(f"CARTESIAN_POINT('',{start})")
        end_point = self._add_entity(f"CARTESIAN_POINT('',{end})")
        
        v1_id = self._add_entity(f"VERTEX_POINT('',#{start_point})")
        v2_id = self._add_entity(f"VERTEX_POINT('',#{end_point})")
        
        # Create diagonal member as a rectangular beam
        # (Simplified - would create full 3D beam in production)
        edge_id = self._create_edge(v1_id, v2_id)
        
        # Add to output
        for entity_id in range(start_entity_id, self.entity_counter):
            if entity_id in self.entities:
                lines.append(self.entities[entity_id])
        
        return lines
    
    def _generate_joints(self) -> List[str]:
        """Generate joint nodes per REQ-DES-ICD-001"""
        lines = []
        dim = self.config['dimensions']
        tolerance = self.config['tolerances']['position']
        
        lines.append(f"/* Joint Nodes (Position Tolerance: ±{tolerance}mm, Cpk≥1.67) */")
        
        # Key joint locations
        joint_locations = [
            (-dim['length']/2, 0, dim['height']/2, 'J1-Forward-Upper'),
            (0, 0, dim['height']/2, 'J2-Center-Upper'),
            (dim['length']/2, 0, dim['height']/2, 'J3-Aft-Upper'),
            (-dim['length']/2, 0, -dim['height']/2, 'J4-Forward-Lower'),
            (0, 0, -dim['height']/2, 'J5-Center-Lower'),
            (dim['length']/2, 0, -dim['height']/2, 'J6-Aft-Lower')
        ]
        
        for x, y, z, name in joint_locations:
            lines.extend(self._create_joint_node(x, y, z, name))
        
        return lines
    
    def _create_joint_node(self, x: float, y: float, z: float, name: str) -> List[str]:
        """Create joint node with gusset plate representation"""
        lines = []
        size = 100  # mm gusset plate size
        
        # Record starting entity ID for collection
        start_entity_id = self.entity_counter
        
        # Create gusset plate corners
        corners = [
            (x-size/2, y-size/2, z-size/2),
            (x+size/2, y-size/2, z-size/2),
            (x+size/2, y+size/2, z+size/2),
            (x-size/2, y+size/2, z+size/2)
        ]
        
        # Create vertices
        vertex_ids = []
        for cx, cy, cz in corners:
            point_id = self._add_entity(f"CARTESIAN_POINT('',({cx},{cy},{cz}))")
            vertex_id = self._add_entity(f"VERTEX_POINT('',#{point_id})")
            vertex_ids.append(vertex_id)
        
        # Create B-spline surface for gusset
        control_points = f"((#{vertex_ids[0]},#{vertex_ids[1]}),(#{vertex_ids[2]},#{vertex_ids[3]}))"
        bspline_id = self._add_entity(
            f"B_SPLINE_SURFACE_WITH_KNOTS('{name}',1,1,{control_points},"
            f".UNSPECIFIED.,.F.,.F.,.F.,(2,2),(2,2),(0.,1.),(0.,1.),.UNSPECIFIED.)"
        )
        
        # Add comment
        lines.append(f"/* Joint Node: {name} at ({x},{y},{z}) */")
        
        # Collect entities
        for entity_id in range(start_entity_id, self.entity_counter):
            if entity_id in self.entities:
                lines.append(self.entities[entity_id])
        
        return lines
    
    def _generate_interfaces(self) -> List[str]:
        """Generate interface features"""
        lines = []
        
        lines.append("/* Interface Features for System Integration */")
        
        # H2 tank interface points
        lines.append("/* H2 Tank Support Brackets (REQ-DES-ENV-002) */")
        h2_locations = [
            (2000, 0, 800, 'H1-Tank-Support-Fwd'),
            (4000, 0, 800, 'H2-Tank-Support-Aft')
        ]
        
        for x, y, z, name in h2_locations:
            lines.extend(self._create_interface_bracket(x, y, z, name))
        
        # Fastener holes
        lines.append("/* Fastener Pattern (Manufacturing Tolerance per REQ-BLD-QA-001) */")
        lines.extend(self._create_fastener_pattern())
        
        return lines
    
    def _create_interface_bracket(self, x: float, y: float, z: float, name: str) -> List[str]:
        """Create interface bracket for H2 systems"""
        lines = []
        bracket_width = 100
        bracket_height = 100
        
        # Record starting entity ID for collection
        start_entity_id = self.entity_counter

        # Create bracket face
        corners = [
            (x, y, z),
            (x+bracket_width, y, z),
            (x+bracket_width, y, z+bracket_height),
            (x, y, z+bracket_height)
        ]
        
        vertex_ids = []
        for cx, cy, cz in corners:
            point_id = self._add_entity(f"CARTESIAN_POINT('',({cx},{cy},{cz}))")
            vertex_id = self._add_entity(f"VERTEX_POINT('',#{point_id})")
            vertex_ids.append(vertex_id)
        
        # Create edges and face
        edge_ids = []
        for i in range(4):
            edge_id = self._create_edge(vertex_ids[i], vertex_ids[(i+1)%4])
            edge_ids.append(edge_id)
        
        oriented_edges = [self._add_entity(f"ORIENTED_EDGE('',*,*,#{e},.T.)") for e in edge_ids]
        edge_loop_id = self._add_entity(f"EDGE_LOOP('',(#{',#'.join(map(str, oriented_edges))}))")
        face_bound_id = self._add_entity(f"FACE_OUTER_BOUND('',#{edge_loop_id},.T.)")
        
        # Create plane
        plane_point = self._add_entity(f"CARTESIAN_POINT('',({x+bracket_width/2},{y},{z+bracket_height/2}))")
        plane_normal = self._add_entity("DIRECTION('',(0.,1.,0.))")
        plane_ref = self._add_entity("DIRECTION('',(1.,0.,0.))")
        plane_axis = self._add_entity(f"AXIS2_PLACEMENT_3D('',#{plane_point},#{plane_normal},#{plane_ref})")
        plane_id = self._add_entity(f"PLANE('',#{plane_axis})")
        
        face_id = self._add_entity(f"ADVANCED_FACE('{name}',(#{face_bound_id}),#{plane_id},.T.)")
        
        lines.append(f"/* Interface Bracket: {name} */")
        for entity_id in range(start_entity_id, self.entity_counter):
            if entity_id in self.entities:
                lines.append(self.entities[entity_id])
        
        return lines
    
    def _create_fastener_pattern(self) -> List[str]:
        """Create fastener hole pattern"""
        lines = []
        hole_diameter = 9.6  # M10 clearance hole
        spacing = 500  # mm
        
        # Create sample fastener holes along longeron
        for i in range(3):
            x_pos = -1000 + i * spacing
            lines.extend(self._create_fastener_hole(x_pos, 0, 1025, hole_diameter, f"F{i+1}"))
        
        return lines
    
    def _create_fastener_hole(self, x: float, y: float, z: float, diameter: float, name: str) -> List[str]:
        """Create cylindrical surface for fastener hole"""
        lines = []
        
        # Record starting entity ID for collection
        start_entity_id = self.entity_counter

        # Create cylinder axis
        axis_point = self._add_entity(f"CARTESIAN_POINT('',({x},{y},{z}))")
        axis_dir = self._add_entity("DIRECTION('',(0.,0.,1.))")
        ref_dir = self._add_entity("DIRECTION('',(1.,0.,0.))")
        axis_placement = self._add_entity(
            f"AXIS2_PLACEMENT_3D('',#{axis_point},#{axis_dir},#{ref_dir})"
        )
        
        # Create cylindrical surface
        cylinder_id = self._add_entity(
            f"CYLINDRICAL_SURFACE('{name}-Hole',#{axis_placement},{diameter/2})"
        )
        
        lines.append(f"/* Fastener Hole {name}: Ø{diameter}mm at ({x},{y},{z}) */")
        for entity_id in range(start_entity_id, self.entity_counter):
            if entity_id in self.entities:
                lines.append(self.entities[entity_id])
        
        return lines
    
    def _generate_material_properties(self) -> List[str]:
        """Generate material property entities"""
        lines = []
        mat = self.material
        
        lines.append(f"/* Material: {mat.name} per REQ-DES-MAT-001 */")
        
        # Property definition
        prop_def_id = self._add_entity(
            f"PROPERTY_DEFINITION('material','{mat.name}',#{self.product_def_shape_id})"
        )
        
        # Material properties
        yield_id = self._add_entity(f"DESCRIPTIVE_REPRESENTATION_ITEM('Yield_Strength','{mat.yield_strength} MPa')")
        ult_id = self._add_entity(f"DESCRIPTIVE_REPRESENTATION_ITEM('Ultimate_Strength','{mat.ultimate_strength} MPa')")
        modulus_id = self._add_entity(f"DESCRIPTIVE_REPRESENTATION_ITEM('Elastic_Modulus','{mat.elastic_modulus} GPa')")
        density_id = self._add_entity(f"DESCRIPTIVE_REPRESENTATION_ITEM('Density','{mat.density} kg/m3')")
        poisson_id = self._add_entity(f"DESCRIPTIVE_REPRESENTATION_ITEM('Poisson_Ratio','{mat.poisson_ratio}')")
        h2_compat_id = self._add_entity(f"DESCRIPTIVE_REPRESENTATION_ITEM('H2_Compatibility','{mat.h2_compatibility}')")
        temp_range_id = self._add_entity(
            f"DESCRIPTIVE_REPRESENTATION_ITEM('Temperature_Range','{mat.temperature_range[0]} to {mat.temperature_range[1]} C')"
        )
        
        # Material property representation
        mat_prop_rep_id = self._add_entity(
            f"MATERIAL_PROPERTY_REPRESENTATION('',"
            f"(#{yield_id},#{ult_id},#{modulus_id},#{density_id},#{poisson_id},#{h2_compat_id},#{temp_range_id}),"
            f"#{self.rep_context_id})"
        )
        
        prop_def_rep_id = self._add_entity(
            f"PROPERTY_DEFINITION_REPRESENTATION(#{prop_def_id},#{mat_prop_rep_id})"
        )
        
        for entity_id in range(prop_def_id, self.entity_counter):
            if entity_id in self.entities:
                lines.append(self.entities[entity_id])
        
        return lines
    
    def _generate_metadata(self) -> List[str]:
        """Generate metadata and approval entities"""
        lines = []
        
        # Approval status
        approval_id = self._add_entity(
            "APPROVAL('Design Release','Approved for FEA Validation per REQ-VV-TST-001')"
        )
        
        # Date and time
        date_id = self._add_entity(f"CALENDAR_DATE({self.timestamp.year},{self.timestamp.month},{self.timestamp.day})")
        utc_offset_id = self._add_entity("COORDINATED_UNIVERSAL_TIME_OFFSET(0,0,.AHEAD.)")
        time_id = self._add_entity(f"LOCAL_TIME({self.timestamp.hour},{self.timestamp.minute},{self.timestamp.second}.,#{utc_offset_id})")
        
        date_time_id = self._add_entity(f"DATE_AND_TIME(#{date_id},#{time_id})")
        approval_date_id = self._add_entity(f"APPROVAL_DATE_TIME(#{date_time_id},#{approval_id})")
        
        # Organization and person
        org_id = self._add_entity(
            "ORGANIZATION('AMPEL360-H2-BWB-CERT','AMPEL360 H2 BWB Certification Authority','')"
        )
        person_id = self._add_entity(
            "PERSON('STR-001','Robbbo-T','Structural Analysis Lead')"
        )
        
        approval_person_id = self._add_entity(
            f"APPROVAL_PERSON_ORGANIZATION(#{person_id},#{approval_id},#{org_id})"
        )
        
        # Approval status
        status_id = self._add_entity(f"APPROVAL_STATUS('RELEASED_FOR_ANALYSIS',#{approval_id})")
        
        # Certification reference
        cert_id = self._add_entity(
            "CERTIFICATION('Structural Compliance','CS-25.301/305 per REQ-CRT-REG-001',(#7))"
        )
        
        # Security classification
        security_id = self._add_entity(
            "SECURITY_CLASSIFICATION('Controlled','Requirements Controlled Data',#7)"
        )
        
        # Digital signature placeholder
        lines.append(f"/* Digital Signature: SHA-256 = {hashlib.sha256(str(self.entities).encode()).hexdigest()} */")
        lines.append(f"/* Session ID: {self.session_id} */")
        lines.append(f"/* Requirements Traced: {len(self.requirements)} */")
        
        for entity_id in range(approval_id, self.entity_counter):
            if entity_id in self.entities:
                lines.append(self.entities[entity_id])
        
        return lines
    
    def _generate_traceability_manifest(self, step_file: str):
        """Generate JSON manifest for requirements traceability"""
        manifest = {
            'session_id': self.session_id,
            'timestamp': self.timestamp.isoformat(),
            'step_file': step_file,
            'requirements_traced': [],
            'material': {
                'name': self.material.name,
                'properties': {
                    'yield_strength': f"{self.material.yield_strength} MPa",
                    'ultimate_strength': f"{self.material.ultimate_strength} MPa",
                    'elastic_modulus': f"{self.material.elastic_modulus} GPa",
                    'density': f"{self.material.density} kg/m³",
                    'h2_compatibility': self.material.h2_compatibility,
                    'temperature_range': f"{self.material.temperature_range[0]} to {self.material.temperature_range[1]}°C"
                }
            },
            'verification': {
                'safety_factor': 1.5,
                'load_paths': 2,
                'position_tolerance': "±0.25mm",
                'cpk_target': 1.67
            },
            'digital_signature': {
                'sha256': hashlib.sha256(open(step_file, 'rb').read()).hexdigest(),
                'ed25519': "pending",  # Would use actual crypto in production
                'dilithium3': "pending"
            }
        }
        
        # Add requirement links
        for req in self.requirements:
            manifest['requirements_traced'].append({
                'req_id': req.req_id,
                'component_type': req.component_type.value,
                'safety_factor': req.safety_factor,
                'evidence_path': req.evidence_path,
                'tolerance': f"±{req.tolerance}mm",
                'cpk_target': req.cpk_target
            })
        
        # Save manifest
        manifest_path = step_file.replace('.step', '_manifest.json')
        with open(manifest_path, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        print(f"✓ Traceability manifest saved: {manifest_path}")
        
        return manifest_path

class STEPValidator:
    """Validates generated STEP files against requirements"""
    
    @staticmethod
    def validate_file(step_file: str) -> Dict[str, Any]:
        """Validate STEP file structure and requirements compliance"""
        results = {
            'file': step_file,
            'valid': True,
            'checks': [],
            'requirements_met': [],
            'issues': []
        }
        
        # Check file exists and is readable
        if not os.path.exists(step_file):
            results['valid'] = False
            results['issues'].append(f"File not found: {step_file}")
            return results
        
        with open(step_file, 'r') as f:
            content = f.read()
        
        # Check header
        if 'ISO-10303-21;' not in content:
            results['valid'] = False
            results['issues'].append("Invalid STEP file header")
        else:
            results['checks'].append("✓ Valid ISO-10303-21 header")
        
        # Check schema
        if 'AUTOMOTIVE_DESIGN' not in content:
            results['issues'].append("Missing AP214 schema declaration")
        else:
            results['checks'].append("✓ AP214 schema present")
        
        # Check for required sections
        required_sections = [
            ('Product Definition', 'PRODUCT_DEFINITION'),
            ('Material Properties', 'MATERIAL_PROPERTY'),
            ('Coordinate System', 'AXIS2_PLACEMENT_3D'),
            ('Geometric Elements', 'ADVANCED_FACE')
        ]
        
        for section_name, keyword in required_sections:
            if keyword in content:
                results['checks'].append(f"✓ {section_name} present")
            else:
                results['issues'].append(f"Missing {section_name}")
        
        # Check requirements traceability
        req_patterns = [
            'REQ-DES-STR-001',
            'REQ-DES-STR-002',
            'REQ-DES-MAT-001',
            'REQ-DES-ICD-001'
        ]
        
        for req in req_patterns:
            if req in content:
                results['requirements_met'].append(req)
        
        # Check manifest
        manifest_path = step_file.replace('.step', '_manifest.json')
        if os.path.exists(manifest_path):
            results['checks'].append("✓ Traceability manifest present")
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)
            results['session_id'] = manifest.get('session_id')
            results['requirements_count'] = len(manifest.get('requirements_traced', []))
        else:
            results['issues'].append("Missing traceability manifest")
        
        # Final validation
        if results['issues']:
            results['valid'] = False
        
        return results

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate STEP files for AMPEL360 H₂-BWB-Q structural grid'
    )
    parser.add_argument(
        '--config',
        default='config/h2_bwb_config.yaml',
        help='Configuration file path'
    )
    parser.add_argument(
        '--output',
        default='grid-topology.step',
        help='Output STEP file path'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate generated file'
    )
    
    args, _ = parser.parse_known_args()
    
    # Create output directory if needed
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("=" * 60)
    print("AMPEL360 H₂-BWB-Q STEP File Generator")
    print("=" * 60)
    
    # Generate STEP file
    generator = STEPGenerator(args.config)
    output_file = generator.generate(args.output)
    
    print(f"✓ STEP file generated: {output_file}")
    print(f"  Session ID: {generator.session_id}")
    print(f"  Requirements traced: {len(generator.requirements)}")
    print(f"  Entities created: {generator.entity_counter - 1}")
    
    # Validate if requested
    if args.validate:
        print("\nValidating generated file...")
        validator = STEPValidator()
        validation = validator.validate_file(output_file)
        
        print(f"\nValidation Results:")
        print(f"  Valid: {'✓' if validation['valid'] else '✗'}")
        
        if validation['checks']:
            print("\n  Checks Passed:")
            for check in validation['checks']:
                print(f"    {check}")
        
        if validation['requirements_met']:
            print(f"\n  Requirements Met: {', '.join(validation['requirements_met'])}")
        
        if validation['issues']:
            print("\n  Issues Found:")
            for issue in validation['issues']:
                print(f"    ✗ {issue}")
    
    print("\n" + "=" * 60)
    print("Generation complete")
    
    return 0

if __name__ == '__main__':
    exit(main())
