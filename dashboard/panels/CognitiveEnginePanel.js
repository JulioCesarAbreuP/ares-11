// CognitiveEnginePanel.js
// Panel avanzado para Cognitive Engine (KPIs, rrss, IA, navegación táctica)
import React from 'react';

export default function CognitiveEnginePanel({ insights, kpis, onSimulateAttack }) {
  return (
    <div className="cognitive-engine-panel">
      <h2>Cognitive Engine</h2>
      <div className="kpi-row">
        <KPI title="Detecciones IA" value={kpis.aiDetections} />
        <KPI title="Simulaciones Ofensivas" value={kpis.offensiveSimulations} />
        <KPI title="Alertas RRSS" value={kpis.rrssAlerts} />
        <KPI title="Acciones Defensivas" value={kpis.defensiveActions} />
      </div>
      <div className="insights-list">
        <h3>Insights Recientes</h3>
        <ul>
          {insights.map((insight, idx) => (
            <li key={idx}>
              <strong>{insight.severity.toUpperCase()}:</strong> {insight.description}
              <br />
              <em>Recomendación:</em> {insight.recommendation}
              <span className="origin">{insight.origin}</span>
            </li>
          ))}
        </ul>
      </div>
      <div className="actions">
        <button onClick={onSimulateAttack}>Simular Ataque Ofensivo</button>
        <button>Exportar Insights</button>
      </div>
      <nav className="enterprise-nav">
        <a href="/dashboard">Dashboard</a>
        <a href="/cognitive-engine">Cognitive Engine</a>
        <a href="/remediation">Remediation</a>
        <a href="/compliance">Compliance</a>
      </nav>
    </div>
  );
}
// KPI, Insights, y navegación empresarial alineados con doctrina ARES-11
