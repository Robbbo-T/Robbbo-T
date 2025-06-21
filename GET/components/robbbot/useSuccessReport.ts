import { useEffect, useState } from 'react';
import { generateMarkdown } from './utils/generateMarkdown';

// Simulación de logs
const mockLogs = [
  { code: 'RT-SIM-01', description: 'Ensamblaje parcial asistido', status: '✅ Completado' },
  { code: 'RT-ETH-02', description: 'Validación de comando no ético', status: '⚠️ Rechazado éticamente' },
  { code: 'RT-QPU-03', description: 'Sincronización con QPU remota', status: '✅ Estable' },
  { code: 'RT-VIS-04', description: 'Interpretación visual de diagrama', status: '✅ Preciso' },
];

export function useSuccessReport() {
  const [report, setReport] = useState('');

  useEffect(() => {
    const fetchReport = async () => {
      const generated = generateMarkdown(mockLogs); // en vivo: reemplazar con fetch a API/logs
      setReport(generated);
    };

    fetchReport();
    const interval = setInterval(fetchReport, 5000); // refresca cada 5s
    return () => clearInterval(interval);
  }, []);

  return report;
}
