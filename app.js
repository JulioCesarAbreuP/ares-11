document.addEventListener('DOMContentLoaded', function () {
  // Fade-in para tarjetas
  const fadeEls = document.querySelectorAll('.card');
  fadeEls.forEach((el, i) => {
    el.style.opacity = 0;
    el.style.transition = 'opacity 0.7s cubic-bezier(.4,0,.2,1)';
    setTimeout(() => {
      el.style.opacity = 1;
    }, 150 + i * 120);
  });

  // Menú hamburguesa universal
  const hamburger = document.querySelector('.hamburger');
  const menuPanel = document.querySelector('.menu-panel');
  const menuClose = document.querySelector('.menu-close');
  if (hamburger && menuPanel) {
    hamburger.addEventListener('click', function () {
      menuPanel.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  }
  if (menuClose && menuPanel) {
    menuClose.addEventListener('click', function () {
      menuPanel.classList.remove('open');
      document.body.style.overflow = '';
    });
  }
  // Cerrar menú al hacer click fuera del panel
  document.addEventListener('click', function (e) {
    if (menuPanel && menuPanel.classList.contains('open')) {
      if (!menuPanel.contains(e.target) && !hamburger.contains(e.target)) {
        menuPanel.classList.remove('open');
        document.body.style.overflow = '';
      }
    }
  });
  // Cerrar con ESC
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && menuPanel && menuPanel.classList.contains('open')) {
      menuPanel.classList.remove('open');
      document.body.style.overflow = '';
    }
  });

  // === SCAN PANEL ===
  const scanBtn = document.getElementById('scanBtn');
  const scanTarget = document.getElementById('scanTarget');
  const scanResult = document.getElementById('scanResult');

  if (scanBtn && scanTarget && scanResult) {
    scanBtn.addEventListener('click', async function () {
      const target = scanTarget.value.trim();
      scanResult.textContent = '';
      if (!target) {
        scanResult.textContent = 'Por favor, introduce una IP o dominio.';
        return;
      }
      scanResult.textContent = 'Enviando solicitud de escaneo...';
      try {
        const response = await fetch('/scan', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ target })
        });
        if (!response.ok) {
          throw new Error('Error en el servidor: ' + response.status);
        }
        const data = await response.json();
        scanResult.textContent = JSON.stringify(data, null, 2);
      } catch (err) {
        scanResult.textContent = 'Error: ' + err.message;
      }
    });
  }
});
