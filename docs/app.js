document.addEventListener('DOMContentLoaded', function () {
  // Internacionalización básica
  const langSelect = document.getElementById('lang-select');
  const translations = {
    es: {
      'Motor de Razonamiento': 'Motor de Razonamiento',
      'CIS Auditor': 'CIS Auditor',
      'TAXII Client': 'TAXII Client',
      'Risk Engine': 'Risk Engine',
      'Remediation Engine': 'Remediation Engine',
      'Tactical Dashboard': 'Tactical Dashboard',
      'Quick Triage': 'Quick Triage',
      'Exporter': 'Exporter',
      'Notifier': 'Notifier',
      'Live Monitor': 'Live Monitor',
      'Remediation Script Generator': 'Remediation Script Generator',
      'Whitelist': 'Whitelist',
      'Shodan Check': 'Shodan Check',
      'Forensics Packager': 'Forensics Packager',
      'Módulos Principales': 'Módulos Principales',
      'Plataforma de Defensa Proactiva y Auditoría Táctica.\nÍndice general de módulos y herramientas.': 'Plataforma de Defensa Proactiva y Auditoría Táctica.\nÍndice general de módulos y herramientas.'
    },
    en: {
      'Motor de Razonamiento': 'Reasoning Engine',
      'CIS Auditor': 'CIS Auditor',
      'TAXII Client': 'TAXII Client',
      'Risk Engine': 'Risk Engine',
      'Remediation Engine': 'Remediation Engine',
      'Tactical Dashboard': 'Tactical Dashboard',
      'Quick Triage': 'Quick Triage',
      'Exporter': 'Exporter',
      'Notifier': 'Notifier',
      'Live Monitor': 'Live Monitor',
      'Remediation Script Generator': 'Remediation Script Generator',
      'Whitelist': 'Whitelist',
      'Shodan Check': 'Shodan Check',
      'Forensics Packager': 'Forensics Packager',
      'Módulos Principales': 'Main Modules',
      'Plataforma de Defensa Proactiva y Auditoría Táctica.\nÍndice general de módulos y herramientas.': 'Proactive Defense Platform and Tactical Audit.\nGeneral index of modules and tools.'
    }
  };
  function translateUI(lang) {
    document.querySelectorAll('.ares-subtitle').forEach(el => {
      el.textContent = translations[lang]['Motor de Razonamiento'];
    });
    document.querySelectorAll('.ares-menu a').forEach(el => {
      const txt = el.textContent.trim();
      if (translations[lang][txt]) el.textContent = translations[lang][txt];
    });
    const h2 = document.querySelector('h2');
    if (h2 && translations[lang][h2.textContent.trim()]) h2.textContent = translations[lang][h2.textContent.trim()];
    const desc = document.querySelector('.description');
    if (desc && translations[lang][desc.textContent.replace(/\s+/g,' ').trim()]) desc.textContent = translations[lang][desc.textContent.replace(/\s+/g,' ').trim()];
  }
  if (langSelect) {
    langSelect.value = localStorage.getItem('ares-lang') || 'es';
    translateUI(langSelect.value);
    langSelect.addEventListener('change', function () {
      localStorage.setItem('ares-lang', langSelect.value);
      translateUI(langSelect.value);
    });
  }
  // Modo claro/oscuro
  const themeToggle = document.getElementById('theme-toggle');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  function setTheme(theme) {
    document.body.setAttribute('data-theme', theme);
    themeToggle.textContent = theme === 'dark' ? '🌙' : '☀️';
    localStorage.setItem('ares-theme', theme);
  }
  // Inicializar
  const savedTheme = localStorage.getItem('ares-theme');
  setTheme(savedTheme || (prefersDark ? 'dark' : 'light'));
  themeToggle.addEventListener('click', function () {
    const current = document.body.getAttribute('data-theme');
    setTheme(current === 'dark' ? 'light' : 'dark');
  });
  // Fade-in para tarjetas
  const fadeEls = document.querySelectorAll('.card');
  fadeEls.forEach((el, i) => {
    el.style.opacity = 0;
    el.style.transition = 'opacity 0.7s cubic-bezier(.4,0,.2,1)';
    setTimeout(() => {
      el.style.opacity = 1;
    }, 150 + i * 120);
  });

  // Accesibilidad y teclado para menú hamburguesa ARES-11
  const menuToggle = document.getElementById('ares-menu-toggle');
  const menuIcon = document.querySelector('.ares-menu-icon');
  const menu = document.getElementById('ares-menu');
  if (menuToggle && menuIcon && menu) {
    // Sincronizar aria-expanded
    menuToggle.addEventListener('change', function () {
      menuToggle.setAttribute('aria-expanded', menuToggle.checked ? 'true' : 'false');
      if (menuToggle.checked) {
        // Enfocar primer item accesible
        const firstItem = menu.querySelector('a[role="menuitem"]');
        if (firstItem) firstItem.focus();
      }
    });

    // Abrir/cerrar con Enter/Espacio en el icono
    menuIcon.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        menuToggle.checked = !menuToggle.checked;
        menuToggle.dispatchEvent(new Event('change'));
      }
    });

    // Cerrar menú con Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menuToggle.checked) {
        menuToggle.checked = false;
        menuToggle.dispatchEvent(new Event('change'));
        menuIcon.focus();
      }
    });

    // Navegación con flechas dentro del menú
    menu.addEventListener('keydown', function (e) {
      const items = Array.from(menu.querySelectorAll('a[role="menuitem"]'));
      const current = document.activeElement;
      const idx = items.indexOf(current);
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (idx >= 0 && idx < items.length - 1) items[idx + 1].focus();
        else if (idx === items.length - 1) items[0].focus();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (idx > 0) items[idx - 1].focus();
        else if (idx === 0) items[items.length - 1].focus();
      }
    });
  }
});