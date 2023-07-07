import requests
import json
import sys

def get_ip_details(ip):
    url = "http://ip-api.com/json/" + ip
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python ip.py <ip>")
        sys.exit(1)
    ip = sys.argv[1]
    details = get_ip_details(ip)
    if details is None:
        print("Error: Could not get ip details")
        sys.exit(1)
    print("IP: " + details['query'])
    print("Country: " + details['country'])
    print("Region: " + details['regionName'])
    print("City: " + details['city'])
    print("ISP: " + details['isp'])
    print("Organization: " + details['org'])
    print("AS: " + details['as'])
    print("Lat: " + str(details['lat']))
    print("Lon: " + str(details['lon']))
    print("Timezone: " + details['timezone'])
    print("Zip: " + details['zip'])
    print("Status: " + details['status'])

main()