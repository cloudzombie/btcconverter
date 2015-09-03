#coding:utf-8
from flask import Flask, render_template, request, redirect, url_for, Blueprint
from blockchain import exchangerates, statistics
from chart import chart
import urllib2, json, requests, datetime

#Global variables
app = Flask(__name__)
app.register_blueprint(chart)
ticker = exchangerates.get_ticker()
stats = statistics.get()
actualpricelist = []
actualtimelist = []
actualpricelist_rev = []
actualtimelist_rev = []
actual = ['Actual Price']
date = ['Date']

#Chart section
jsonfilein = 'https://blockchain.info/charts/market-price?showDataPoints=false&timespan=&show_header=true&daysAverageString=1&scale=0&format=json&address='
r = requests.get(jsonfilein)
j = r.json()
entries = j['values']

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
	for e in entries:
		yield e['y']

def actualtime():
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
	apl = actual + actualpricelist

	for t in actualtime():
		actualtimelist.append(t)
	atl = date + actualtimelist

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart3')
def chart3():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:3]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:3]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart7')
def chart7():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:7]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:7]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart15')
def chart15():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:15]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:15]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart30')
def chart30():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:30]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:30]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart60')
def chart60():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:60]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:60]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart90')
def chart90():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:91]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:91]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

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
