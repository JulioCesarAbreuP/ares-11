// tests/ui/assets.spec.js
// Prueba automatizada: carga de favicon y recursos principales
const { test, expect } = require('@playwright/test');

test('Favicon y recursos principales deben cargar sin errores', async ({ page }) => {
  await page.goto('/docs/index.html');
  // Favicon
  const favicon = await page.$('link[rel="icon"]');
  expect(favicon).not.toBeNull();
  // CSS
  const css = await page.$('link[href="style.css"]');
  expect(css).not.toBeNull();
  // JS
  const js = await page.$('script[src="app.js"]');
  expect(js).not.toBeNull();
  // No errores 404 en recursos
  const errors = [];
  page.on('response', response => {
    if (response.status() === 404) errors.push(response.url());
  });
  // Esperar un poco para capturar errores
  await page.waitForTimeout(1000);
  expect(errors).toEqual([]);
});
