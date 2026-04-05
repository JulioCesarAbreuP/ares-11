// web/attack-map.js
// Estructura de ejemplo para visualización D3.js
const attackPath = [
    { from: "IoT_Coffee", to: "Office_Router", method: "Default_Creds" },
    { from: "Office_Router", to: "Admin_PC", method: "ARP_Spoofing" },
    { from: "Admin_PC", to: "Azure_AD", method: "Token_Theft" }
];

// Aquí iría la lógica D3.js para dibujar el grafo y resaltar rutas críticas
// (Integración con el dashboard principal)

// Ejemplo de exportación para uso en el dashboard
export default attackPath;
