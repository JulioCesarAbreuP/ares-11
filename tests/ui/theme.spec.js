// tests/ui/theme.spec.js
// Prueba automatizada: modo claro/oscuro y persistencia
const { test, expect } = require('@playwright/test');

test('Debe alternar entre modo claro y oscuro y recordar preferencia', async ({ page }) => {
  await page.goto('/docs/index.html');
  // Por defecto debe estar en dark o light
  const theme = await page.evaluate(() => document.body.getAttribute('data-theme'));
  expect(['dark', 'light']).toContain(theme);
  // Alternar
  await page.click('#theme-toggle');
  const newTheme = await page.evaluate(() => document.body.getAttribute('data-theme'));
  expect(newTheme).not.toBe(theme);
  // Recargar y debe persistir
  await page.reload();
  const persisted = await page.evaluate(() => document.body.getAttribute('data-theme'));
  expect(persisted).toBe(newTheme);
});
