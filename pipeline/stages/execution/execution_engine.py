# Renombrado de Annihilator → execution_engine

# execution_engine (antes Annihilator)
from core.events import EventBus
from core.contracts import ExecutionRequest
from enforcer.vlan_shifter import isolate_port

def add_block_rule(ip):
	# Simulación: Bloqueo en Azure Firewall o router local
	print(f"[FIREWALL] Regla de bloqueo aplicada para IP: {ip}")

class ExecutionEngine:
	def execute(self, target_data: dict) -> ExecutionRequest:
		# 1. Bloqueo de Capa 2 (Switch)
		isolate_port(target_data['switch_ip'], target_data['port'])
		# 2. Bloqueo de Capa 3 (Azure Firewall / Router)
		add_block_rule(target_data['ip'])
		# 3. Notificación
		print(f"[✓] Atacante {target_data.get('user_real_name', 'Desconocido')} neutralizado y documentado.")
		# Publicar evento
		EventBus().publish("execution.completed", target_data)
		return ExecutionRequest(target=target_data['ip'], action="block", parameters=target_data)