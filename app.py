#coding:utf-8
from flask import Flask, render_template, request, redirect, url_for
import urllib2, json, requests, datetime
from blockchain import exchangerates, statistics

#Global variables
app = Flask(__name__)
ticker = exchangerates.get_ticker()
stats = statistics.get()
actualpricelist = ['Actual']
actualtimelist = ['Date']

#JSON data
#www
jsonfilein = 'https://blockchain.info/ja/charts/market-price?showDataPoints=false&timespan=&show_header=true&daysAverageString=1&scale=0&format=json&address='
#local
#jsonfilein = './static/json/chart-data.json'

'''
r = requests.get(jsonfilein)
j = r.json()
entries = j['values']
for e in entries:
	actualpricelist.append(e['y'])
'''

#havent use this api below
bcchartapi = "https://blockchain.info/ja/charts/market-price?showDataPoints=false&timespan=&show_header=true&daysAverageString=1&scale=0&format=json&address="

#Def
def ccylists():
	return ticker

def ccyprice():
	for k in ticker:
		yield ticker[k].p15min

def ccysymbol():
	for s in ticker:
		yield ticker[s].symbol

def ccyset():
	for k in ticker:
		return k, ticker[k].symbol, ticker[k].p15min

def actualprice():
	r = requests.get(jsonfilein)
	j = r.json()
	entries = j['values']
	for e in entries:
		yield e['y']


def actualtime():
	r = requests.get(jsonfilein)
	j = r.json()
	entries = j['values']
	for e in entries:
		yield datetime.datetime.fromtimestamp(int(e['x'])).strftime('%Y-%m-%d')




#Flask view
@app.route('/')
def index():
	title = 'BTC Simple Converter'
	symbolList = []
	for sym in ccysymbol():
		symbolList.append(sym)
	priceList = []
	for item in ccyprice():
		priceList.append(item)
	price15min = ['%s%d'%(a,b) for a,b in zip(symbolList, priceList)]

	return render_template('index.html', price15min=price15min, ccysymbol=symbolList, ccyprice=priceList, ccylists=ccylists(), title=title)


@app.route('/chart')
def chart():
	for ap in actualprice():
		actualpricelist.append(ap)

	for t in actualtime():
		actualtimelist.append(t)

	return render_template('chart.js', actualtime=actualtimelist, actualprice=actualpricelist)


@app.route('/jpy', methods=['GET', 'POST'])
def jpy():
	title = 'JPY Simple Converter'
	name = request.form['name']
	btc_amo = exchangerates.to_btc('JPY', name)
	home = redirect(url_for('index'))
	excsym = ticker['JPY'].symbol
	excrat = ticker['JPY'].p15min
	priceList = []
	for item in ccyprice():
		priceList.append(item)
	usdmktprice = stats.market_price_usd
	return render_template('index.html', usdmktprice=usdmktprice, excrat=excrat, excsym=excsym, home=home, name=name, btc_amo=btc_amo, ccyprice=priceList, ccylists=ccylists(), title=title)

#Conf
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
