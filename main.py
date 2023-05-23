import os
import requests
import ipaddress

def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ip_lookup(ip):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,continent,country,regionName,city,zip,lat,lon,timezone,isp,org,as,reverse,mobile,proxy,hosting,query,continentCode,countryCode,region,regionCode,asname,zipCode,elevation,usageType"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        print(f"IP: {data['query']}")
        print(f"Continent: {data['continent']} ({data['continentCode']})")
        print(f"Country: {data['country']} ({data['countryCode']})")
        print(f"Region: {data['regionName']} ({data['region']})")
        print(f"City: {data['city']}")
        print(f"ZIP Code: {data.get('zip')}") 
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"Timezone: {data['timezone']}")
        print(f"ISP: {data['isp']}")
        print(f"Organization: {data['org']}")
        print(f"AS: {data['as']} ({data['asname']})")
        print(f"Reverse DNS: {data['reverse']}")
        print(f"Mobile: {data['mobile']}")
        print(f"Proxy: {data['proxy']}")
        print(f"Hosting: {data['hosting']}")
    else:
        print(f"Error occurred: {data['message']}")
        
while True:
    ip = input("Enter the IP address (or 'exit' to quit): ")
    if ip.lower() == "exit":
        break
    
    clear_console()
    
    try:
        ip_obj = ipaddress.ip_address(ip)
        ip_type = ip_obj.version  # Get IP version (4 for IPv4, 6 for IPv6)
        ip_lookup(str(ip_obj))
    except ValueError:
        print("Invalid IP address.")

    input("Press any key to continue...")
    clear_console()
