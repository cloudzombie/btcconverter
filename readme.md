~~BTC Simple Converter and Predictor~~
# BTCStats

![](./images/btconv.tiff)

## 0. About this program
Yes... This **was** just a converter, but actually this is NOT a converter anymore. Yup, this shows BTC statistics from the point of view of finance.

So this program **NEVER** provides you a conversion rate of bitcoin to the other major currencies. Also this will help you to buy/sell bitcoins by prediction chart.

I might fix all of these problems... someday.

## 1. Run

1. Uncomment below #Conf on app.py
2. Change directory to `path/to/btcconverter/app.py` on Terminal
3. `python app.py`

## 2. About statistics
- Min, Max, Mean, Variance, Skewness and Kurtosis
- Trade amount of BTC & USD, 24-hour Transaction Volume, and Fee Volume
- Relative Strength Index Chart - 14 days
- Linear regression
- Chi-squared & p-value
- Time series (someday)

All datas are collected from [Blockchain](https://blockchain.info).

**Warning : Please note that I won't be responsible for any loss, damages and troubles.**

## 3. Required modules
Blockchain, Flask, Blueprint, Numpy, Pandas, Scikit-learn, Blockchain, C3.js

## 4. Sample
[Here](https://btcconverter.herokuapp.com)

This system will be down between 3AM and 9AM PDT. Powered by Heroku.

Donate by Bitcoin : 182AK1UUgwNNur2g3h1vaY7b41MDax2C2v



## 日本語
ビットコインの通貨変換アプリケーションでしたが、チャート予測機能がメインになってしまいました。むしろ、現在はこの通貨変換機能を一時無効としておりますが、修正予定です。
他にも現在は不都合な箇所が残っていますが、順次アップデート予定です。

と、ほざいておりましたが、飽きたのでいつか近いうちに直すことにしました。多分。

現在では以下の機能を搭載しています。

- 最小値、最大値、中央値、算術平均、尖度、歪度
- 米ドル/BTC取引量、24時間の取引量、合計手数料
- 相対力指数(RSI) 14日
- 線形回帰
- カイ二乗検定値、p値
- 時系列分析(いつか搭載予定)

[サンプルアプリケーションはこちら](https://btcconverter.herokuapp.com)

このシステムは、Herokuの無料枠の都合上、アメリカ西海岸時間の午前3時〜午前9時までの6時間は起動しません。ご了承下さい。

Bitcoinでの寄付をお待ちしております : 182AK1UUgwNNur2g3h1vaY7b41MDax2C2v
