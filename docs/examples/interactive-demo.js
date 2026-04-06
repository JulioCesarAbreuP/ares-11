// docs/examples/interactive-demo.js
// Ejemplo interactivo para documentación doctrinal
window.addEventListener('DOMContentLoaded', function () {
  const btn = document.createElement('button');
  btn.textContent = 'Ejecutar demo ARES-11';
  btn.style = 'margin:1rem;padding:0.7rem 1.5rem;font-size:1rem;';
  btn.onclick = function () {
    alert('¡Demo interactiva de ARES-11 ejecutada!');
  };
  document.body.appendChild(btn);
});
