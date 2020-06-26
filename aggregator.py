import urllib, os, requests, datetime, subprocess


import pprint

# pip install feedparser
import feedparser

# stockexchange
from nsetools import Nse



class News:
    def Nigerian_News(self):
        newsfeed = feedparser.parse(
            "http://feeds.feedburner.com/naijalive"
        )
        print("Today's News: ")
        for i in range(0, 20):
            entry = newsfeed.entries[i]
            print(entry.title)
            print(entry.summary)
            print("------News Link--------")
            print(entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')


class Medium:
    def medium_programming(self):
        feed = feedparser.parse(
            "https://medium.com/feed/tag/programming"
        )

        print("Programming Today: ")
        for i in range(10):
            entry = feed.entries[i]
            print(entry.title)
            print("URL: " + entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')

    def medium_python(self):
        feed_python = feedparser.parse(
            "https://medium.com/feed/tag/python"
        )
        print("Python Today: ")
        for i in range(0,10):
            entry = feed_python.entries[i]
            print(entry.title)
            print("URL: " + entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')

    def medium_developer(self):
        feed_developer = feedparser.parse(
            "https://medium.com/feed/tag/developer"
        )
        print("Developer News Today: ")
        for i in range(5):
            entry = feed_developer.entries[i]
            print(entry.title)
            print("URL: " + entry.link)
            print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')


class StockExchange:
    def nse_stock(self):
        nse = Nse()
        print("TOP GAINERS OF YESTERDAY")
        pprint.pprint(nse.get_top_gainers())
        print("###########################################")
        print("TOP LOSERS OF YESTERDAY")
        pprint.pprint(nse.get_top_losers())
        print("###########################################")
        print('-------------------------------------------------------------------------------------------------------')


# objects inititalization

News_object = News()
Medium_object = Medium()
StockExchange_object = StockExchange()

if __name__ == "__main__":
    # Functions call of each class
    News_object.Nigerian_News()
    Medium_object.medium_python()
    Medium_object.medium_programming()
    Medium_object.medium_developer()
    StockExchange_object.nse_stock()

