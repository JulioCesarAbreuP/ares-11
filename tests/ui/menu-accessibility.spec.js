// tests/ui/menu-accessibility.spec.js
// Prueba automatizada: accesibilidad y funcionamiento del menú hamburguesa
const { test, expect } = require('@playwright/test');

test.describe('Menú hamburguesa ARES-11', () => {
  test('Debe abrir y cerrar con teclado y mouse', async ({ page }) => {
    await page.goto('/docs/index.html');
    // El menú debe estar oculto inicialmente
    await expect(page.locator('.ares-menu')).toBeHidden();
    // Abrir menú con click
    await page.click('.ares-menu-icon');
    await expect(page.locator('.ares-menu')).toBeVisible();
    // Cerrar menú con click en icono
    await page.click('.ares-menu-icon');
    await expect(page.locator('.ares-menu')).toBeHidden();
    // Abrir menú con Enter
    await page.focus('.ares-menu-icon');
    await page.keyboard.press('Enter');
    await expect(page.locator('.ares-menu')).toBeVisible();
    // Cerrar menú con Escape
    await page.keyboard.press('Escape');
    await expect(page.locator('.ares-menu')).toBeHidden();
  });

  test('Debe navegar con flechas y enfocar items', async ({ page }) => {
    await page.goto('/docs/index.html');
    await page.click('.ares-menu-icon');
    const firstItem = page.locator('.ares-menu a').first();
    await expect(firstItem).toBeFocused();
    // Flecha abajo
    await page.keyboard.press('ArrowDown');
    const secondItem = page.locator('.ares-menu a').nth(1);
    await expect(secondItem).toBeFocused();
    // Flecha arriba
    await page.keyboard.press('ArrowUp');
    await expect(firstItem).toBeFocused();
  });
});
