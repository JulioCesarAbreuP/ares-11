# ARES-11 — Núcleo Hexagonal (Ports & Adapters)

## Resumen de Arquitectura

- **Dominio (core_engine/domain/):**
  - `interfaces.py`: Contratos ISurveillanceEngine, IExecutionOrchestrator.
  - `models.py`: TacticalInference, MitigationPriority.
- **Adaptadores (core_engine/adapters/):**
  - `advanced_scanner.py`: Motor de escaneo asíncrono, banner grabbing, resiliencia.
  - `execution_orchestrator.py`: Orquestador de acciones, microsegmentación, circuit breaker.
  - `vlan_adapter.py`: Adaptador de aislamiento físico.
  - `worm_storage.py`: Persistencia forense WORM.
- **API (core_engine/api/):**
  - `api.py`: Exposición de endpoints, orquestación, canal WebSocket.
  - `ws.py`: Gestión de conexiones WebSocket.
- **Middleware:**
  - `middleware.py`: DLP_Interceptor (anonimización PII), anti_prompt_injection.

## Flujo de Datos
1. **/scan** recibe target →
2. AdvancedScanner ejecuta escaneo sigiloso y banner grabbing →
3. Banners pasan por anti_prompt_injection →
4. Se genera TacticalInference (simulado) →
5. ExecutionOrchestrator decide microsegmentación y persistencia forense →
6. Evento enviado por WebSocket a /ws/tactical-feed →
7. Todos los eventos críticos se almacenan en WORM.

## Resiliencia y Seguridad
- **Circuit Breaker:** Si falla la microsegmentación, se activa fallback de log forense.
- **DLP:** Todo payload POST pasa por DLP_Interceptor.
- **Anti-Prompt Injection:** Banners filtrados antes de IA.
- **WORM:** Evidencia forense inmutable.

## SRP (Responsabilidad Única)
Cada módulo está documentado y cumple una única función, permitiendo intercambiar adaptadores sin modificar el dominio.

---

**Este núcleo está listo para escalar, integrar AI Gateway real, y soportar despliegues de misión crítica.**
