#coding:utf-8
from flask import Flask, render_template, request, redirect, url_for
import urllib2, json, requests, datetime
from blockchain import exchangerates, statistics

#Global variables
app = Flask(__name__)
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
	aplrev = actualpricelist_rev[:4]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:4]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart7')
def chart7():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:8]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:8]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart15')
def chart15():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:16]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:16]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart30')
def chart30():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:31]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:31]
	atl = date + atrev

	return render_template('chart.js', actualtime=atl, actualprice=apl)

@app.route('/chart60')
def chart60():
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:61]
	apl = actual + aplrev

	for t in actualtime():
		actualtimelist_rev.append(t)

	actualtimelist_rev.reverse()
	atrev = actualtimelist_rev[:61]
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

@app.route('/3days')
def c3():
	chartnum = 3
	return render_template('index.html', chartnum=chartnum)

@app.route('/7days')
def c7():
	chartnum = 7
	return render_template('index.html', chartnum=chartnum)

@app.route('/15days')
def c15():
	chartnum = 15
	return render_template('index.html', chartnum=chartnum)

@app.route('/30days')
def c30():
	chartnum = 30
	return render_template('index.html', chartnum=chartnum)

@app.route('/60days')
def c60():
	chartnum = 60
	return render_template('index.html', chartnum=chartnum)

@app.route('/90days')
def c90():
	chartnum = 90
	return render_template('index.html', chartnum=chartnum)

#Conf
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
