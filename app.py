#coding:utf-8
from flask import Flask, render_template, request, redirect, url_for
import urllib2
from blockchain import exchangerates, statistics

#Global variables
app = Flask(__name__)
ticker = exchangerates.get_ticker()
stats = statistics.get()

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
