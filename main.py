import requests

print("""
██╗██████╗░░░░░░░██████╗░██╗██████╗░░█████╗░████████╗███████╗
██║██╔══██╗░░░░░░██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║██████╔╝█████╗██████╔╝██║██████╔╝███████║░░░██║░░░█████╗░░
██║██╔═══╝░╚════╝██╔═══╝░██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
██║██║░░░░░░░░░░░██║░░░░░██║██║░░██║██║░░██║░░░██║░░░███████╗
╚═╝╚═╝░░░░░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
""")
ip = input("Enter IP To Scan: ")
url = f"https://ipinfo.io/{ip}?token=89eb984d917dd5"
response = requests.get(url).json()

print("\nScanning " + ip + ", please wait.\n----------------------------------------------")

try:
    print("IP:", response['ip'])
    print("\n")
    print("ADDRESS:")
    print("Country Code:", response['country'])
    print("Region Name:", response['region'])
    print("City:", response['city'])
    print("\n")
    print("POSTAL/TIMEZONE:")
    print("Postal Code:", response['postal'])
    print("Timezone:", response['timezone'])
    print("\n")
    print("LAT/LONG")
    print("Location:", response['loc'])

except requests.ConnectionError as e:
    print("Connection Error. Make sure you are connected to Internet. Details given below.\n")
    print(str(e))
except requests.Timeout as e:
    print("The request timed out, please try again.")
    print(str(e))
except requests.RequestException as e:
    print("General Error")
    print(str(e))
except KeyboardInterrupt:
    print("Program interrupted by User.")

input("----------------------------------------------\nPress any key to exit...")
