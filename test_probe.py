import subprocess

def check_xhci_hcd():
    try:
        # Exécutez la commande 'lsmod' pour lister les modules chargés et recherchez 'xhci_hcd'
        output = subprocess.check_output(['lsmod']).decode('utf-8')
        if 'xhci_hcd' in output:
            print("Le module xhci_hcd a été chargé.")
        else:
            raise Exception("Le module xhci_hcd n'a pas été chargé.")
    except Exception as e:
        print(f"Erreur : {e}")
        exit(1)

if __name__ == "__main__":
    check_xhci_hcd()
