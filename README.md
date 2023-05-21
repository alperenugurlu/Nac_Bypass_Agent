# Nac Bypass Agent

This piece of code is a script written in Python and designed to run on Kali Linux. Here is a summary explaining what each function does:

# run_command(command): 
This function runs the command it takes as input and returns its output.

# kill_network_services(): 
This function stops the dhclient and NetworkManager services.

# get_network_info(): 
This function listens for network traffic using tcpdump and returns the first captured IP and MAC address. If these addresses are not captured, None returns None.

# spoof_ip_address(interface, ip_address, netmask): 
This function replaces the IP address of the specified network interface with the specified IP address and netmask.

# spoof_mac_address(interface, mac_address): 
This function replaces the MAC address of the specified network interface with the specified MAC address.

# start_responder(interface): 
This function starts the responder tool on the specified network interface.

# start_tcpdump(interface): 
This function starts the tcpdump tool on the specified network interface.

# nbtscan(ip_range): 
This function runs the nbtscan tool in the specified IP range.

# main(): 
This function combines all the above functions and takes necessary information from the user to change the IP and MAC address, start the responder and tcpdump tools, and run the nbtscan tool.

All of the above code must be contained in a Python script and the script must be run with root privileges. Because this piece of code contains commands that change the network configuration and tools that listen for network traffic. These operations usually require root privileges. Also, the use of this script may be subject to the law and unauthorized use may lead to legal problems. Therefore, it is important to check local laws and policies before using the script.

![image](https://github.com/alperenugurlu/Nac_Bypass_Agent/assets/64872731/9ff0e710-706e-4ddc-b4c3-d1b09ab5e39b)

In apt and Ransomware group scenarios, when they infiltrate the enterprise from the outside, it tries to bypass nac security solutions in enterprise structures. If it can achieve this, it starts to discover users in the whole network. It also listens to the network with wireshark or tcpdump. If voip is used in your structure, it can decode all calls over SIP. In the scenario I have described below, it decodes your voip calls over SIP after success.

This is a tool that aims to automatically bypass the nac bypass method at the basic level in the tool I have made. With this tool, it helps you to interpret your nac security product configuration in your organization with or without attack protection at a basic level. Example usage and explanation are as follows.

# Step 1

The first step is to run this tool when you connect to the inside network.

![Ekran-Kaydı-2023-05-21-12 39 51](https://github.com/alperenugurlu/Nac_Bypass_Agent/assets/64872731/dc51a2bc-157c-4312-9c0c-6a7e77d75a97)

If the nac bypass is successful, listen to the network with wireshark. And here, filter the Voip calls from the #SIPFlows tab from the #Telephony tab with the data you collected over wireshark, and if the call is available instantly, you can listen to the VOIP calls according to a certain order.

# Step 2

![image](https://github.com/alperenugurlu/Nac_Bypass_Agent/assets/64872731/3e55ab83-6237-4be7-a4cb-0674c3d11eae)

# Step 3

![test2](https://github.com/alperenugurlu/Nac_Bypass_Agent/assets/64872731/00a1d1a5-546b-4e7b-8f10-34b0ffe58e94)


The purpose of this tool and this scenario is to increase security awareness for your institutions. In addition, the perspective of an APT group has been tried to be reflected.

# Everyone is looking at what you are looking at; But can everyone see what he can see? You are the only difference between them… 
By Mevlânâ Celâleddîn-i Rûmî



