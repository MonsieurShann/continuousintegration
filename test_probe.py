import subprocess

def check_xhci_hcd():
    try:
        # Exécutez la commande 'lsmod' pour lister les modules chargés et recherchez 'xhci_hcd'
        output = subprocess.check_output(['lsmod']).decode('utf-8')
        subprocess.run(["cd /"], shell=True)
        directories = subprocess.check_output(["ls"]).decode('utf-8')
        installed_packages = subprocess.check_output(["apt list --installed"], shell=True)
        if installed_packages != "" :
            print("installed_packages = ", installed_packages)
        else:
            raise Exception("Aucun installed_packages...")
    except Exception as e:
        print(f"Erreur : {e}")
        exit(1)

if __name__ == "__main__":
    check_xhci_hcd()
