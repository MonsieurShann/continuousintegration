import subprocess

def check_xhci_hcd():
    try:
        # Exécutez la commande 'lsmod' pour lister les modules chargés et recherchez 'xhci_hcd'
        output = subprocess.check_output(['lsmod']).decode('utf-8')
        archives = subprocess.check_output(["ls /var/cache/apt/archives"], shell=True).decode('utf-8')
        installed_packages = subprocess.check_output(["apt list --installed"], shell=True)
        if archives != "" :
            print("archives = ", archives)
        else:
            raise Exception("Aucune archives...")
    except Exception as e:
        print(f"Erreur : {e}")
        exit(1)

if __name__ == "__main__":
    check_xhci_hcd()
