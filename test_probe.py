import subprocess

def check_xhci_hcd():
    try:
        # Exécutez la commande 'lsmod' pour lister les modules chargés et recherchez 'xhci_hcd'
        output = subprocess.check_output(['lsmod']).decode('utf-8')
        subprocess.run(["cd /"], shell=True)
        directories = subprocess.check_output(["ls"]).decode('utf-8')
        if directories != "" :
            print("directories = ", directories)
        else:
            raise Exception("Aucun directories...")
    except Exception as e:
        print(f"Erreur : {e}")
        exit(1)

if __name__ == "__main__":
    check_xhci_hcd()
