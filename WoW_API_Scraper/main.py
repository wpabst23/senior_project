##William Pabst
##Eastern Connecticut State University
##Senior Research
##
##A Program to pull JSON files from the World of Warcraft API
##
##Request URL:
##https://us.api.battle.net/wow/auction/data/blackrock?locale=en_US&apikey=gf56d57h4ryrcwsm5rwrxwara8e4txk2

import os
import json
import time
from pip._vendor import requests


fileList = os.listdir("C:\\Users\\epicf\\PycharmProjects\\WoW_API_Scraper")


class APICall():
    timeStamp = str(int(time.time()))
    fileNameTemp = "AHDATA" + timeStamp + ".json"
    file = open(fileNameTemp, "w+")
    fileList.append(fileNameTemp)
    ##first request returns the URL for the JSON file
    response = requests.get("https://us.api.battle.net/wow/auction/data/blackrock?locale=en_US&jsonp=AHDATA&apikey=gf56d57h4ryrcwsm5rwrxwara8e4txk2")
    print(str(response.content))
    fileURL = str(response.content)[27:-36]
    print(fileURL)
    content = requests.get(fileURL) ##second request returns JSON data
    data = content.json()
    ##print(str(data["auctions"]))
    ##print(type(data))
    print(data["auction"])
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



