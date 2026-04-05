
// KEV Client — integración enterprise
export async function loadKEV() {
  // En producción: fetch a CISA KEV
  // Aquí: placeholder estático
  return [
    {
      cve: "CVE-2023-12345",
      vendor: "ExampleVendor",
      product: "ExampleProduct",
      exploited: true,
      dateAdded: "2023-10-01"
    },
    {
      cve: "CVE-2024-00001",
      vendor: "ExampleVendor",
      product: "ExampleService",
      exploited: true,
      dateAdded: "2024-01-15"
    }
  ];
}

export function matchKevByCve(cves, kevEntries) {
  if (!Array.isArray(cves)) return [];
  const kevMap = new Map(kevEntries.map(k => [k.cve, k]));
  return cves
    .map(cve => kevMap.get(cve))
    .filter(Boolean);
}

export function kevSeverityBoost(kevMatches) {
  if (!Array.isArray(kevMatches) || kevMatches.length === 0) return 0;
  // Simple: cada KEV suma 3 puntos
  return kevMatches.length * 3;
}
  
