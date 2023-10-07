import subprocess

def check_xhci_hcd():
    try:
        # Exécutez la commande 'lsmod' pour lister les modules chargés et recherchez 'xhci_hcd'
        output = subprocess.check_output(['lsmod']).decode('utf-8')
        if output != "" :
            print("output = ", output)
        else:
            raise Exception("Aucun drivers...")
    except Exception as e:
        print(f"Erreur : {e}")
        exit(1)

if __name__ == "__main__":
    check_xhci_hcd()
