// playwright.config.js
// Configuración básica para pruebas UI con Playwright
// npm install --save-dev @playwright/test

/** @type {import('@playwright/test').PlaywrightTestConfig} */
const config = {
  testDir: './tests/ui',
  timeout: 20000,
  retries: 1,
  use: {
    headless: true,
    baseURL: 'http://localhost:8080', // Cambia si usas otro puerto
    viewport: { width: 1280, height: 800 },
  },
};

module.exports = config;
