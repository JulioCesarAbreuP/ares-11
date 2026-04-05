# visual_forensics.py
# Capturador de Evidencia Visual Remota (PowerShell + SMB/RPC)
# Integra captura, descarga y análisis OCR con IA local

import subprocess
import os

def capture_remote_screen(target_ip, admin_user, admin_pass):
    print(f"[*] ARES-11: Iniciando Captura Visual en {target_ip}...")
    ps_command = (
        "$Path = 'C:\\Windows\\Temp\\evidence.png';"
        "Add-Type -AssemblyName System.Windows.Forms;"
        "$Screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds;"
        "$Bitmap = New-Object System.Drawing.Bitmap($Screen.Width, $Screen.Height);"
        "$Graphic = [System.Drawing.Graphics]::FromImage($Bitmap);"
        "$Graphic.CopyFromScreen(0, 0, 0, 0, $Bitmap.Size);"
        "$Bitmap.Save($Path);"
    )
    # Ejecución remota vía crackmapexec (requiere WinRM/SMB habilitado)
    cmd = f"crackmapexec smb {target_ip} -u {admin_user} -p {admin_pass} --powershell \"{ps_command}\""
    subprocess.run(cmd, shell=True)
    # Descargar evidencia
    download_cmd = f"smbclient //{target_ip}/C$ -c 'get Windows/Temp/evidence.png ../reports/evidence_{target_ip}.png'"
    subprocess.run(download_cmd, shell=True)
    print(f"[!] EVIDENCIA CAPTURADA: Ver ../reports/evidence_{target_ip}.png")

# OCR y análisis IA local (Llama 3)
def analyze_visual_evidence(image_path):
    import pytesseract
    from PIL import Image
    import ollama
    text = pytesseract.image_to_string(Image.open(image_path))
    prompt = f"""
    Analiza el siguiente texto extraído de una captura de pantalla forense:
    {text}
    1. ¿Detectas portales de Azure, AWS, banca o consolas de administración?
    2. ¿Hay comandos de PowerShell o credenciales visibles?
    3. ¿Recomiendas alguna acción inmediata? (bloqueo, aislamiento, rotación de claves)
    Responde en formato JSON técnico.
    """
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    print("[IA OCR] Análisis de evidencia visual:", response['message']['content'])
    return response['message']['content']

if __name__ == "__main__":
    # Ejemplo de uso
    # capture_remote_screen('192.168.1.101', 'admin', 'password123')
    # analyze_visual_evidence('../reports/evidence_192.168.1.101.png')
    pass
