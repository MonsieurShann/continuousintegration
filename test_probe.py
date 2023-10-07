import sys
import subprocess

size = len(sys.argv)

searched_drivers = ["xhci_hcdfzepofj", "crc64"]

def search_string_in_dmesg(searched_drivers):
    dmesg_output = subprocess.check_output(["sudo", "lsmod"]).decode("utf-8")
    if searched_drivers[0] in dmesg_output:
        print("Trouve!!!")
    else:
        return -1

search_string_in_dmesg(searched_drivers)

