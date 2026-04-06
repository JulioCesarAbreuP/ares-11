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
});