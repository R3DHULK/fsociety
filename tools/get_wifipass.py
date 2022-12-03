import subprocess
import os
import re
from collections import namedtuple
import configparser

print ('''\033[93m
    ***************************************************************
    *    ___     _ __      ___  __ _ ___                          *
    *   / __|___| |\ \    / (_)/ _(_) _ \__ _ ______              *
    *  | (_ / -_)  _\ \/\/ /| |  _| |  _/ _` (_-<_-<              *
    *   \___\___|\__|\_/\_/ |_|_| |_|_| \__,_/__/__/              *
    *                                                             *
    *   powerful tool to get all wifi-passwords in seconds        *
    *   code from R3dHULK                                         *
    *   download link : https://github.com/R3DHULK/getwifipass    *
    *                                                             *
    ***************************************************************
  ''')
                                              
def get_windows_saved_ssids():
    """Returns a list of saved SSIDs in a Windows machine using netsh command"""
    # get all saved profiles in the PC
    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = []
    profiles = re.findall(r"All User Profile\s(.*)", output)
    for profile in profiles:
        # for each SSID, remove spaces and colon
        ssid = profile.strip().strip(":").strip()
        # add to the list
        ssids.append(ssid)
    return ssids


def get_windows_saved_wifi_passwords(verbose=1):
    """Extracts saved Wi-Fi passwords saved in a Windows machine, this function extracts data using netsh
    command in Windows
    Args:
        verbose (int, optional): whether to print saved profiles real-time. Defaults to 1.
    Returns:
        [list]: list of extracted profiles, a profile has the fields ["ssid", "ciphers", "key"]
    """
    ssids = get_windows_saved_ssids()
    Profile = namedtuple("Profile", ["ssid", "ciphers", "key"])
    profiles = []
    for ssid in ssids:
        ssid_details = subprocess.check_output(f"""netsh wlan show profile "{ssid}" key=clear""").decode()
        # get the ciphers
        ciphers = re.findall(r"Cipher\s(.*)", ssid_details)
        # clear spaces and colon
        ciphers = "/".join([c.strip().strip(":").strip() for c in ciphers])
        # get the Wi-Fi password
        key = re.findall(r"Key Content\s(.*)", ssid_details)
        # clear spaces and colon
        try:
            key = key[0].strip().strip(":").strip()
        except IndexError:
            key = "None"
        profile = Profile(ssid=ssid, ciphers=ciphers, key=key)
        if verbose >= 1:
            print_windows_profile(profile)
        profiles.append(profile)
    return profiles


def print_windows_profile(profile):
    """Prints a single profile on Windows"""
    print(f"{profile.ssid:25}{profile.ciphers:15}{profile.key:50}")


def print_windows_profiles(verbose):
    """Prints all extracted SSIDs along with Key on Windows"""
    print("\033[94m SSID                     CIPHER(S)      KEY")
    get_windows_saved_wifi_passwords(verbose)


def get_linux_saved_wifi_passwords(verbose=1):   
    """Extracts saved Wi-Fi passwords saved in a Linux machine, this function extracts data in the
    `/etc/NetworkManager/system-connections/` directory
    Args:
        verbose (int, optional): whether to print saved profiles real-time. Defaults to 1.
    Returns:
        [list]: list of extracted profiles, a profile has the fields ["ssid", "auth-alg", "key-mgmt", "psk"]
    """
    network_connections_path = "/etc/NetworkManager/system-connections/"
    fields = ["ssid", "auth-alg", "key-mgmt", "psk"]
    Profile = namedtuple("Profile", [f.replace("-", "_") for f in fields])
    profiles = []
    for file in os.listdir(network_connections_path):
        data = { k.replace("-", "_"): None for k in fields }
        config = configparser.ConfigParser()
        config.read(os.path.join(network_connections_path, file))
        for _, section in config.items():
            for k, v in section.items():
                if k in fields:
                    data[k.replace("-", "_")] = v
        profile = Profile(**data)
        if verbose >= 1:
            print_linux_profile(profile)
        profiles.append(profile)
    return profiles


def print_linux_profile(profile):
    """Prints a single profile on Linux"""
    print(f"{str(profile.ssid):25}{str(profile.auth_alg):5}{str(profile.key_mgmt):10}{str(profile.psk):50}") 


def print_linux_profiles(verbose):
    """Prints all extracted SSIDs along with Key (PSK) on Linux"""
    print("SSID                     AUTH KEY-MGMT  PSK")
    get_linux_saved_wifi_passwords(verbose)
    
    
def print_profiles(verbose=1):
    if os.name == "nt":
        print_windows_profiles(verbose)
    elif os.name == "posix":
        print_linux_profiles(verbose)
    else:
        raise NotImplemented("Code only works for either Linux or Windows")
    
print ('''\033[91m
       
    ***************************************************************
    *                                                             *
    *   🔴NOTE : '' THIS TOOL ONLY GRABS THE PASSWORDS            *
    *              WHICH WAS INPUTED IN THE COMPUTER EARLIER      *
    *              IF THE PASSWORD IS CHANGED BY OWNER,           *
    *              THIS TOOL CAN'T HELP YOU TO HACK THE SSID      *
    *              OR LET YOU KNOW THE AFTER RESULTS ''           *
    *                                                             *
    ***************************************************************   
       ''')    
print ('''\033[92m
       [*] Hulk starts to catch ssid   cipher and key ...
       
       [!] Hulk came up with :::
       ''')
if __name__ == "__main__":
    print_profiles()
input("Enter To Continue")

