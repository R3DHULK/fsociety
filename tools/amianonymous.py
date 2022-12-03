from ip2geotools.databases.noncommercial import DbIpCity
import requests
logo = '''
                                                             _____ 
               _                                            |___  |
  ___ _____   |_|   ___ ___ ___ ___ _ _ _____ ___ _ _ ___     |  _|
 | .'|     |  | |  | .'|   | . |   | | |     | . | | |_ -|    |_|  
 |__,|_|_|_|  |_|  |__,|_|_|___|_|_|_  |_|_|_|___|___|___|    |_|  
                                   |___|               
     code from R3DHULK       github page : https://github.com/R3DHULK
'''
print(logo)
ANSI_COLOR_SAFE     = '\033[92m'
ANSI_COLOR_NOTSAFE  = '\033[91m'

def fetch_public_ip():
    fetch_adress = 'https://checkip.amazonaws.com'
    return requests.get(fetch_adress).text.strip()

def resolve_city(ip):
    response = DbIpCity.get(ip, api_key='free')
    return response.city

def resolve_country(ip):
    response = DbIpCity.get(ip, api_key='free')
    return response.country

def main():
    public_ip = fetch_public_ip()
    city = resolve_city(public_ip)
    country = resolve_country(public_ip)

    # Setting font color depending on country
    if country != 'DE':
        safe = True
        print(f'{ANSI_COLOR_SAFE}', end='')
    else:
        safe = False
        print(f'{ANSI_COLOR_NOTSAFE}', end='')

    print('///////////////////////////////////////////////')
    print('Public IP:   {}'.format(public_ip))
    print('Location:    {}, {}'.format(city, country))
    print('\n')

    if safe:
        print("  [!] It seems, that you're safe!\n")
    else:
        print('  [!] Hmmm... Check the VPN one more time!\n')
    
    print('///////////////////////////////////////////////')
    
if __name__ == '__main__':
    main()
input(" press close to exit ")