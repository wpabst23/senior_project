##William Pabst
##Eastern Connecticut State University
#Senior Research
##
##A program to organize the relevant auction data produced by the scraper.

import os
import json

fileList = os.listdir("C:\\Users\\epicf\\PycharmProjects\\WoW_API_Scraper")

file = open(fileList[1], "r").read()

data = json.loads(file)

priceList = []

##Compute average asking price per file
for auc in data:
    price = auc["buyout"]
    quantity = auc["quantity"]
    priceList.append(price/quantity)
averagePrice = sum(priceList)/len(priceList)

print(data)
print(priceList)
print("The average auction price in this file is: " + str(averagePrice))

##When data collection is complete, this file will be modified to loop through all the files gathered,
##and produce averages and basis for analysis
##
##
##Methods will also be added to determine the price of SOLD auctions.
##While data for SOLD auctions is not provided my Blizzard, a methodology can be produced to extrapolate that data.
##To do this, I will compare a given file with the file that was produced IMMEDIATELY PRIOR to the given file,
##to produce a list of auctions that have lapsed between the two data captures.
##Now, auctions can lapse for 3 reasons; The timer has expired, and the item was returned to the seller,
##the item was prematurely pulled from the auction house,
##or it was sold.
##
##To ensure the most accurate results, the method for SOLD auctions will not consider differences, if the auction
##that disappeared had a 'SHORT' time designation before it disappeared.


