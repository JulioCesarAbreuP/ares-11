import requests

def get_cisa_kev():
    # Descarga la lista de vulnerabilidades que CISA dice que están siendo explotadas
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    r = requests.get(url)
    return r.json()['vulnerabilities']

def correlate_findings(scan_results):
    kev_list = get_cisa_kev()
    critical_alerts = []
    
    for asset in scan_results:
        # Si el asset tiene un CVE que está en la lista KEV de CISA...
        # ... generamos una alerta de "Prioridad Máxima de Combate"
        pass # Aquí va la lógica de cruce de IDs (CVE-202X-XXXX)
    
    return critical_alerts
