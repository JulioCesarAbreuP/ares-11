# AI Assistant para ARES-11

Este microservicio permite conectar ARES-11 con modelos de IA locales (Ollama, LM Studio) y en línea (Azure OpenAI, HuggingFace) para análisis de eventos, generación de recomendaciones y playbooks automáticos.

## Funcionalidades
- Análisis de eventos/logs con LLM local (Ollama/LM Studio)
- Análisis con Azure OpenAI (requiere API Key)
- Generación de recomendaciones defensivas y ofensivas
- Sugerencia de playbooks automatizados

## Uso
```js
import { aiAssistant } from './aiAssistant.js';

const evento = { type: 'alert', details: 'Intento de lateral movement detectado' };
aiAssistant.recommendAction(evento).then(console.log);
```

## Configuración
- Para IA local: tener Ollama o LM Studio corriendo en `http://localhost:11434`
- Para Azure OpenAI: definir variables de entorno `AZURE_OPENAI_URL` y `AZURE_OPENAI_KEY`

## Ejemplo de integración
- Llamar a `aiAssistant.recommendAction(evento)` desde cualquier módulo (remediation, threat-mapper, dashboard)
- Usar la respuesta para enriquecer alertas, playbooks o reportes

---

**Extensible:** Puedes agregar soporte para HuggingFace, Google Gemini, etc. siguiendo el mismo patrón.
