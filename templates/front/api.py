import requests

#x = requests.get('https://data.covid19.go.id/public/api/prov.json')
a = requests.get('https://data.covid19.go.id/public/api/update.json')
#data = x.json()
data_update = a.json()
print(data_update['update']['penambahan']['tanggal'])
#print("----------------------------------------------------------")
#print(data_update['update']['total'])