// ForensicAlertsPanel.js
// Panel React para mostrar alertas forenses críticas en el dashboard ARES-11
import React, { useEffect, useState } from 'react';

export default function ForensicAlertsPanel() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetch('/reports/FORENSIC_SUMMARY.md')
      .then(res => res.text())
      .then(text => {
        // Extrae las líneas de alertas críticas del markdown
        const lines = text.split('\n');
        const start = lines.findIndex(l => l.includes('## Alertas Críticas'));
        let extracted = [];
        if (start !== -1) {
          for (let i = start + 1; i < lines.length; i++) {
            if (lines[i].startsWith('- ')) extracted.push(lines[i].slice(2));
            if (lines[i].startsWith('##') && i > start + 1) break;
          }
        }
        setAlerts(extracted);
      });
  }, []);

  return (
    <div className="forensic-alerts-panel">
      <h3>Alertas Forenses Críticas</h3>
      {alerts.length === 0 ? (
        <p>No hay alertas críticas recientes.</p>
      ) : (
        <ul>
          {alerts.map((alert, idx) => (
            <li key={idx}>{alert}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
