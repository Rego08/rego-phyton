#KT Vastamine
#Rego Märk

import requests

url = "https://dummy-json.mock.beeceptor.com/companies"

response = requests.get(url)

valik = input("Sisesta ettevõtte nimi: ").lower()

if response.status_code == 200:
    data = response.json()
    for andmed in data:
        if valik in andmed["name"].lower():
            print(f"Ettevõtte nimi: {andmed['name']}")
            print(f"Asukoht: {andmed['address']}")
            print(f"Zip code on: {andmed['zip']}")
            print(f"Riik: {andmed['country']}")
            print(f"Töötajate arv: {andmed['employeeCount']}")
            print(f"Tegeleb: {andmed['industry']}")
            print(f"Marketcap: {andmed['marketCap']}")
            print(f"Domain: {andmed['domain']}")
            print(f"CEO: {andmed['ceoName']}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")