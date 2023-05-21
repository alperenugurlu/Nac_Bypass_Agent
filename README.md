# Nac Bypass Agent

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



