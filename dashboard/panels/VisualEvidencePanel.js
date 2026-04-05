// VisualEvidencePanel.js
// Panel React para mostrar hallazgos visuales y acciones tomadas en el dashboard ARES-11
import React, { useEffect, useState } from 'react';

export default function VisualEvidencePanel() {
  const [evidence, setEvidence] = useState([]);

  useEffect(() => {
    fetch('/reports/FORENSIC_SUMMARY.md')
      .then(res => res.text())
      .then(text => {
        // Extrae bloques de evidencia visual del markdown
        const lines = text.split('\n');
        const evidencias = [];
        for (let i = 0; i < lines.length; i++) {
          if (lines[i].includes('## Evidencia Visual Analizada')) {
            let block = { timestamp: lines[i], items: [] };
            for (let j = i + 1; j < lines.length && lines[j].startsWith('- '); j++) {
              block.items.push(lines[j].slice(2));
              i = j;
            }
            evidencias.push(block);
          }
        }
        setEvidence(evidencias);
      });
  }, []);

  return (
    <div className="visual-evidence-panel">
      <h3>Evidencia Visual y Acciones</h3>
      {evidence.length === 0 ? (
        <p>No hay evidencia visual reciente.</p>
      ) : (
        evidence.map((block, idx) => (
          <div key={idx} className="evidence-block">
            <div className="evidence-timestamp">{block.timestamp}</div>
            <ul>
              {block.items.map((item, i) => (
                <li key={i}>{item}</li>
              ))}
            </ul>
          </div>
        ))
      )}
    </div>
  );
}
