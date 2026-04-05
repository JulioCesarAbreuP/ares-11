// AI Assistant Microservice for ARES-11
// Integrates with local Ollama/LM Studio and online LLMs (Azure OpenAI, HuggingFace)
// Provides analysis, recommendations, and automated playbook generation

import fetch from 'node-fetch';
import { logger } from '../../utils/logger.js';

const LOCAL_OLLAMA_URL = 'http://localhost:11434/api/generate'; // Ollama/LM Studio REST endpoint
const AZURE_OPENAI_URL = process.env.AZURE_OPENAI_URL || '';
const AZURE_OPENAI_KEY = process.env.AZURE_OPENAI_KEY || '';

export const aiAssistant = {
  /**
   * Analyze event/log with local LLM (Ollama/LM Studio)
   */
  async analyzeWithLocalLLM(prompt) {
    try {
      const res = await fetch(LOCAL_OLLAMA_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt, stream: false })
      });
      const data = await res.json();
      return data.response || '';
    } catch (err) {
      logger.error('Ollama/LM Studio error: ' + err.message);
      return '';
    }
  },

  /**
   * Analyze event/log with Azure OpenAI (online)
   */
  async analyzeWithAzureOpenAI(prompt) {
    if (!AZURE_OPENAI_URL || !AZURE_OPENAI_KEY) return '';
    try {
      const res = await fetch(AZURE_OPENAI_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'api-key': AZURE_OPENAI_KEY
        },
        body: JSON.stringify({ messages: [{ role: 'user', content: prompt }], max_tokens: 512 })
      });
      const data = await res.json();
      return data.choices?.[0]?.message?.content || '';
    } catch (err) {
      logger.error('Azure OpenAI error: ' + err.message);
      return '';
    }
  },

  /**
   * Recommend playbook or action based on event
   */
  async recommendAction(event) {
    const prompt = `Evento: ${JSON.stringify(event)}\nRecomienda una acción defensiva u ofensiva, justifica y sugiere un playbook.`;
    // Prefer local LLM, fallback to Azure
    let response = await this.analyzeWithLocalLLM(prompt);
    if (!response) response = await this.analyzeWithAzureOpenAI(prompt);
    return response;
  }
};

// Example usage:
// const rec = await aiAssistant.recommendAction({ type: 'alert', details: 'Intento de lateral movement detectado' });
// console.log(rec);
