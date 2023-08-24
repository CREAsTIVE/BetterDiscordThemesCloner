import requests

r = requests.get('https://api.betterdiscord.app/v1/store/themes')

f = open("themes.json", "w")
f.write(r.content)
f.close()