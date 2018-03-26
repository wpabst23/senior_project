##William Pabst
##Eastern Connecticut State University
##Senior Research
##
##A Program to pull JSON files from the World of Warcraft API
##
##Request URL:
##https://us.api.battle.net/wow/auction/data/blackrock?locale=en_US&apikey=gf56d57h4ryrcwsm5rwrxwara8e4txk2
##Leystone Ore Item ID: 123918

import os
import json
import time
from pip._vendor import requests


fileList = os.listdir("C:\\Users\\epicf\\PycharmProjects\\WoW_API_Scraper")

##The JSON file is given as a dictionary that contains 2 lists of dictionaries. the first is the header, containing
##context data for the auction information, namely, the server name. The other is a list of auctions, stored as dictionary objects.
##We are only interested in Leystone Ore, so further down we will need to filter the data by item ID, which is a key in each auction dictionary.
class APICall():
    timeStamp = str(int(time.time()))
    fileNameTemp = "AHDATA" + timeStamp + ".json"
    file = open(fileNameTemp, "w+")
    fileList.append(fileNameTemp)
    ##first request returns the URL for the JSON file
    response = requests.get("https://us.api.battle.net/wow/auction/data/blackrock?locale=en_US&jsonp=AHDATA&apikey=gf56d57h4ryrcwsm5rwrxwara8e4txk2")
    print(str(response.content))
    fileURL = str(response.content)[27:-36]
    print(fileURL) ##crop out the JSON file URL from the request response.
    content = requests.get(fileURL) ##second request returns the JSON file at the returned URL
    data = content.json()
    ##print(str(data["auctions"]))
    ##print(type(data))
    print(data["auctions"][1])
    print(type(data["auctions"][1]))
    print(data["auctions"][2])


    ##The following code filters all Leystone Auctions for the given JSON file.*
    itemID = 123918
    leystoneAuctions = []
    for auc in data["auctions"]:
        if auc["item"] == itemID:
            leystoneAuctions.append(auc)
    print(leystoneAuctions[1])


    ##print(data)
    file.write(json.dumps(data))
    file.close


##class fileParse():
    ##json_data = open(fileURL)
    ##data = json.load(json_data)
    ##pprint(data)
    ##json_data.close()


def main():
    APICall()
    ##fileParse()

if __name__ == '__main__': main()



