'use client';

import React from 'react';
import { useSuccessReport } from './useSuccessReport';

export default function SuccessLiveReport() {
  const report = useSuccessReport();

  return (
    <div className="bg-slate-900 text-white p-6 rounded-lg shadow-lg border border-slate-700">
      <h2 className="text-2xl font-bold mb-4">🧠 Reporte en Tiempo Real – Robbbo-T</h2>
      <pre className="whitespace-pre-wrap text-sm font-mono">{report}</pre>
    </div>
  );
}
