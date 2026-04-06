# interfaces/cli/ares11.py
"""
CLI principal de ARES-11. Orquesta el pipeline desde línea de comandos.
Formalizado para arquitectura enterprise.
"""

import argparse
from core.orchestrator import run_pipeline
from core.utils import log_event, trace, retry, sanitize_input

@trace(stage="cli")
@retry(retries=2, delay=1.0)
def main():
    parser = argparse.ArgumentParser(description="ARES-11 CLI - Auditoría y Defensa Enterprise")
    parser.add_argument('--input', type=str, help='Archivo de entrada o datos de red en JSON')
    parser.add_argument('--stage', type=str, choices=['full', 'anomaly', 'correlation', 'ai', 'execution'], default='full', help='Etapa del pipeline a ejecutar')
    args = parser.parse_args()

    # Cargar y sanitizar datos de entrada
    input_data = sanitize_input(args.input or '{}')
    log_event("cli.start", {"stage": args.stage, "input": input_data})
    if args.stage == 'full':
        result = run_pipeline(input_data)
        print("[ARES-11] Pipeline completo ejecutado. Resultado:", result)
    else:
        print(f"[ARES-11] Ejecución parcial de etapa: {args.stage}")
        # Punto de extensión: integración con API REST, SIEM, colas
    log_event("cli.end", {"stage": args.stage})

if __name__ == "__main__":
    main()
