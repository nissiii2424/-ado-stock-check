import os

import requests

URL = "https://ado-officialshop-friedpotato.com/products/Ado26Ao_004V"

html = requests.get(URL).text

if True:

    webhook = os.environ["DISCORD_WEBHOOK"]

    requests.post(

        webhook,

        json={

            "content": "🚨 Adoグッズの在庫が復活した可能性があります！\nhttps://ado-officialshop-friedpotato.com/products/Ado26Ao_004V"

        }

    )

    print("Notification sent")

else:

    print("Still sold out")