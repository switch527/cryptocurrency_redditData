import demjson
import requests
import pandas as pd

currencies = ("litecoin","bitcoin","ethereum","nem","dashpay","monero","neo")
def Scrape_redditMetrics(currencies):
    for currency in currencies :
        print("Waiting for the data of " + currency + "..")
        r = requests.get('http://www.redditmetrics.com/r/'+ currency)

        json_data = r.text.split('data: ')[1].split('pointSize')[0].strip()[:-1].replace('\n', '')
        growth = demjson.decode(json_data)
        growth_df = pd.DataFrame(growth)
        growth_df.to_csv("/home/fmerizzi/Desktop/scrapingBuffer/" + currency + "_redditGrowth.csv")

        json_data = r.text.split('data: ')[2].split('pointSize')[0].strip()[:-1].replace('\n', '')
        total = demjson.decode(json_data)
        total_df = pd.DataFrame(total)
        total_df.to_csv("/home/fmerizzi/Desktop/scrapingBuffer/" + currency + "_redditSubscriber.csv")
##Scrape_redditMetrics(currencies);