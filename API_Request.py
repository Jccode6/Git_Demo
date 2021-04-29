"""
Quick and dirty way to pull data via api.
Not recommended for prod due to API token being visible
"""

import requests 
import json 




#Makes call to server to retrieve data
api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=b7b03ddc-7bea-4816-868e-4a2926addbad")
#Loads data into json
api = json.load(api_request.content)
#returns data in json format
print(api)
#Return specific parts of data. You can drill down to the exact data by putting json keys into a list
# print(api["data"][0]["symbol"])
# print(api["data"][0]["quote"]["USD"]["price"])

#Create dictionaries to calculate current price 
# coins = [
#     {
#         "symbol":"BTC",
#         "amount_owned": 2,
#         "price_per_coin": 3200
#     },
#     {
#         "symbol":"ETH",
#         "amount_owned": 100,
#         "price_per_coin": 2.05

#     },
#     {
#        "symbol":"USDT",
#        "amount_owned": 3,
#        "price_per_coin": 1000
#     }
    
# ]
# """
# loop through index to pull multiple data points for specified coins.
# Specified coins are in list. Loop below will run through list
# And only return data related to values in list
# """

# for i in range(0,5):
#     for coin in coins:
#         if api["data"][i]["symbol"] == coin["symbol"]:
#             total_paid = coin["amount_owned"] * coin["price_per_coin"]
#             current_value = coin["amount_owned"] * api["data"][i]["quote"]["USD"]["price"]
#             pl_percoin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
#             print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
#             print("Number of Coin:", coin["amount_owned"])
#             print("{0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
#             print("Current Value", "${0:.2f}".format(current_value))
#             print("P/L Per Coin", "${0:.2f}".format(pl_percoin))
           
#             print(("-------------"))

        