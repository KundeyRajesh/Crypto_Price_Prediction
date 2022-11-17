# Import Dependencies

import praw
import configy, pprint
from textblob import TextBlob
# import binance
# from binance.client import Client
# from binance.enums import *
# import configy

# Order Function
#
# def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
#     try:
#         print("sending order")
#         order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
#         print(order)
#     except Exception as e:
#         print("an exception occured - {}".format(e))
#         return False
#     return True


# Connect to API

reddit = praw.Reddit(
    client_id=configy.REDDIT_ID,
    client_secret=configy.REDDIT_SECRET,
    password=configy.REDDIT_PASS,
    user_agent="USERAGENT",
    username=configy.REDDIT_USER,
)
#
# client = Client(configy.API_KEY, configy.API_SECRET)

# Variables for Bot

lst = []
neededSentiments = 50
in_position = False
# TRADE_SYMBOL = 'BTCUSDT'
# TRADE_QUANTITY = 0.000010


def Average(lst):
    if len(lst) == 0:
        return len(lst)
    else:
        return sum(lst[-neededSentiments:]) / neededSentiments


# Connect to Reddit Stream for comments
yui=0
hgu=0
for comment in reddit.subreddit("ethereum").stream.comments():
    if yui>50:
        break
    yui+=1

    redditComment = comment.body
    blob = TextBlob(redditComment)
    sent = blob.sentiment

    print(redditComment)

    print(" ********** Sentiment is " + str(sent.polarity))

    if sent.polarity != 0.0:
        lst.append(sent.polarity)
        avg = round(Average(lst), 2)
        hgu=round(Average(lst),4)
        print(" ********** Total Sentiment is currently: " + str(round(Average(lst), 4)) + " and there are " + str(
            len(lst)) + " elements")


def tru():
    return hgu

        # if round(Average(lst)) > 0.5 and len(lst) > neededSentiments:
        #     if in_position:
        #         print("***** BUY ***** but we own!")
        #     else:
        #         print("***** BUY *****")
        #         order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
        #         if order_succeeded:
        #             in_position = True
        # elif round(Average(lst)) < -0.5 and len(lst) > neededSentiments:
        #     if in_position:
        #         order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
        #         if order_succeeded:
        #             in_position = False
        #     else:
        #         print("***** SELL ***** but we dont own!")