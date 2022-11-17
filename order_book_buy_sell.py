import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import clear_output
import time

n=1

def is_get_quantity():
    r = requests.get("https://api.binance.com/api/v3/depth",
                     params=dict(symbol="BTCBUSD"))
    results = r.json()
    frames = {side: pd.DataFrame(data=results[side], columns=["price", "quantity"],
                                 dtype=float)
              for side in ["bids", "asks"]}
    print(frames['bids']['quantity'])
    qur=0 #bids quantity
    pur=0 #bids price
    for i in frames['bids']['quantity']:
        qur+=float(i)
    print(qur)
    for i in frames['bids']['price']:
        pur+=float(i)
    qur1=0 #ask quantity
    pur1=0 #ask price
    for i in frames['asks']['quantity']:
        qur1+=float(i)
    for i in frames['asks']['price']:
        pur1+=float(i)
    print(qur1)

    frames_list = [frames[side].assign(side=side) for side in frames]
    data = pd.concat(frames_list, axis="index",
                     ignore_index=True, sort=True)
    price_summary = data.groupby("side").price.describe()
    price_summary.to_markdown()
    frames["bids"].price.max()
    frames["asks"].price.min()

    r = requests.get("https://api.binance.com/api/v3/ticker/bookTicker", params=dict(symbol="BTCBUSD"))
    book_top = r.json()
    name = book_top.pop("symbol")  # get symbol and also delete at the same time
    s = pd.Series(book_top, name=name, dtype=float)
    s.to_markdown()
    fig, ax = plt.subplots()



    sns.scatterplot(x="price", y="quantity", hue="side", data=data, ax=ax)

    ax.set_xlabel("Price")
    ax.set_ylabel("Quantity")


    pur=frames["bids"].price.max()
    pur1=frames["asks"].price.min()
    print([pur,qur,pur1,qur1])

    return [pur,qur,pur1,qur1]

is_get_quantity()


