// tests/ui/seo.spec.js
// Prueba automatizada: metadatos y SEO básicos
const { test, expect } = require('@playwright/test');

test('Debe tener metadatos SEO y descripción', async ({ page }) => {
  await page.goto('/docs/index.html');
  const title = await page.title();
  expect(title).toMatch(/ARES-11/);
  const desc = await page.$('meta[name="description"]');
  expect(desc).not.toBeNull();
  const ogTitle = await page.$('meta[property="og:title"]');
  const ogDesc = await page.$('meta[property="og:description"]');
  expect(ogTitle).not.toBeNull();
  expect(ogDesc).not.toBeNull();
});
