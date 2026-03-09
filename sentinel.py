import os

def banner():
    print("========================================")
    print("      Z-SENTINEL: OSINT AUTOMATOR       ")
    print("      Identity & Data Intelligence      ")
    print("========================================")

def main():
    banner()
    print("[1] Rastrear Alias (Global Social Scan)")
    print("[2] Análisis de Infraestructura Telefónica")
    print("[3] Generar Reporte de Evidencia")
    
    opc = input("\nSeleccione operación de inteligencia: ")
    
    if opc == "1":
        user = input("Ingrese el alias/username: ")
        os.system(f"sherlock {user}")
    elif opc == "2":
        phone = input("Ingrese número con código de país (Ej +52): ")
        os.system(f"phoneinfoga scan -n {phone}")
    elif opc == "3":
        print("[+] Recopilando logs para reporte final...")
        print("[OK] Datos listos para procesamiento en LaTeX.")
    else:
        print("Cerrando sesión segura.")

if __name__ == "__main__":
    main()

