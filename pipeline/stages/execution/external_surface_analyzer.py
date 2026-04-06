# Renombrado de SoulCrusher → external_surface_analyzer

# external_surface_analyzer (antes SoulCrusher)
from core.events import EventBus
from core.contracts import AnomalyOutput
import shodan
import requests

class ExternalSurfaceAnalyzer:
	def __init__(self, api_key_shodan):
		self.api = shodan.Shodan(api_key_shodan)

	def analyze(self, target_ip) -> AnomalyOutput:
		print(f"[!] ARES-11: Iniciando análisis externo de {target_ip}...")
		host = self.api.host(target_ip)
		details = {
			"location": f"{host.get('city', 'N/A')}, {host.get('country_name', 'N/A')}",
			"org": host.get('org', 'N/A'),
			"vpn_tunnel": not any('google.com' in str(d) for d in host.get('data', [])),
		}
		if details["vpn_tunnel"]:
			print("[!!!] ALERTA: El dispositivo está usando un túnel VPN/Tor para evadir el proxy.")
		# Simulación OSINT
		details["osint"] = "Simulación de búsqueda en redes y brechas"
		# Publicar evento
		EventBus().publish("external_surface.analyzed", details)
		return AnomalyOutput(anomaly_type="external_surface", score=1.0, details=details)