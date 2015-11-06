from flask import Flask, render_template, request, redirect, url_for, Blueprint
from blockchain import exchangerates, statistics
import urllib2, json, requests, datetime
import pandas as pd
import numpy as np
import scipy.stats

chart = Blueprint('chart',__name__)

#For statistics
stats = statistics.get()
actualtimelist = []
actualtimelist_rev = []
ticker = exchangerates.get_ticker()

#Chart section
jsonfilein = 'https://blockchain.info/charts/market-price?showDataPoints=false&timespan=&show_header=true&daysAverageString=1&scale=0&format=json&address='
r = requests.get(jsonfilein)
j = r.json()
entries = j['values']

def ccylists():
	return ticker

def ccyprice():
	for k in ticker:
		yield ticker[k].p15min

def ccysymbol():
	for s in ticker:
		yield ticker[s].symbol

def ccydrop():
	for s in ticker:
		yield s

def ccyset():
	for k in ticker:
		yield k, ticker[k].symbol, ticker[k].p15min

def ccysymamo():
	for sa in ticker:
		yield sa, ticker[sa].p15min

def actualprice():
	for e in entries:
		yield e['y']

def actualtime():
	for e in entries:
		yield datetime.datetime.fromtimestamp(int(e['x'])).strftime('%Y-%m-%d')

def predictionprice():
	for e in entries:
		yield e['y']

def predictiontime():
	for e in entries:
		yield e['x']

@chart.route('/')

def c1():
#Var
	actualpricelist = []
	actualpricelist_rev = []
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	ccysetlist = []
	for ccys in ccyset():
		ccysetlist.append(ccys)
	ccysetlist.sort(key=lambda x:x[0])

	symbollist = []
	pricelist = []
	for sym in ccysymbol():
		symbollist.append(sym)
	for pl in ccyprice():
		pricelist.append(pl)

	ccydroplist = []
	for ccyd in ccydrop():
		ccydroplist.append(ccyd)

	ccysymamolist = []
	for ccysa in ccysymamo():
		ccysymamolist.append(ccysa)
	ccysymamolist.sort(key=lambda x:x[0])

#General stock infos
	price15min = sorted(['%s%d'%(a,b) for a,b in zip(symbollist, pricelist)], key=lambda symbols:symbols[0])

#Statistics tab
	btctradevolume = stats.trade_volume_btc
	usdtradevolume = stats.trade_volume_usd
	estvolusd = stats.estimated_transaction_volume_usd
	totalfeebtc = stats.total_fees_btc

#array for numpy
	actualpricelist_rev.sort(reverse=True)
	aplrev = actualpricelist_rev

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = len(aplrev)
	divresult = scipy.stats.chisquare(aplrev)
	statpval = divresult[0]
	statchi = divresult[1]

	return render_template('index.html', btctradevolume=btctradevolume, usdtradevolume=usdtradevolume, estvolusd=estvolusd, totalfeebtc=totalfeebtc, ccysymamolist=ccysymamolist, ccydroplist=ccydroplist, ccysetlist=ccysetlist, price15min=price15min, symbollist=symbollist, pricelist=pricelist, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur)

@chart.route('/3days')
def c3():
	chartnum = 3
#Var
	actualpricelist = []
	actualpricelist_rev = []
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	ccysetlist = []
	for ccys in ccyset():
		ccysetlist.append(ccys)
	ccysetlist.sort(key=lambda x:x[0])

	symbollist = []
	pricelist = []
	for sym in ccysymbol():
		symbollist.append(sym)
	for pl in ccyprice():
		pricelist.append(pl)

	ccydroplist = []
	for ccyd in ccydrop():
		ccydroplist.append(ccyd)

	ccysymamolist = []
	for ccysa in ccysymamo():
		ccysymamolist.append(ccysa)
	ccysymamolist.sort(key=lambda x:x[0])

#General stock infos
	price15min = sorted(['%s%d'%(a,b) for a,b in zip(symbollist, pricelist)], key=lambda symbols:symbols[0])

#Statistics tab
	btctradevolume = stats.trade_volume_btc
	usdtradevolume = stats.trade_volume_usd
	estvolusd = stats.estimated_transaction_volume_usd
	totalfeebtc = stats.total_fees_btc

#array for numpy
	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = len(aplrev)
	divresult = scipy.stats.chisquare(aplrev)
	statpval = divresult[0]
	statchi = divresult[1]

	return render_template('index.html', chartnum=chartnum, btctradevolume=btctradevolume, usdtradevolume=usdtradevolume, estvolusd=estvolusd, totalfeebtc=totalfeebtc, ccysymamolist=ccysymamolist, ccydroplist=ccydroplist, ccysetlist=ccysetlist, price15min=price15min, symbollist=symbollist, pricelist=pricelist, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur)

@chart.route('/7days')
def c7():
	chartnum = 7
#Var
	actualpricelist = []
	actualpricelist_rev = []
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	ccysetlist = []
	for ccys in ccyset():
		ccysetlist.append(ccys)
	ccysetlist.sort(key=lambda x:x[0])

	symbollist = []
	pricelist = []
	for sym in ccysymbol():
		symbollist.append(sym)
	for pl in ccyprice():
		pricelist.append(pl)

	ccydroplist = []
	for ccyd in ccydrop():
		ccydroplist.append(ccyd)

	ccysymamolist = []
	for ccysa in ccysymamo():
		ccysymamolist.append(ccysa)
	ccysymamolist.sort(key=lambda x:x[0])

#General stock infos
	price15min = sorted(['%s%d'%(a,b) for a,b in zip(symbollist, pricelist)], key=lambda symbols:symbols[0])

#Statistics tab
	btctradevolume = stats.trade_volume_btc
	usdtradevolume = stats.trade_volume_usd
	estvolusd = stats.estimated_transaction_volume_usd
	totalfeebtc = stats.total_fees_btc

#array for numpy
	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = len(aplrev)
	divresult = scipy.stats.chisquare(aplrev)
	statpval = divresult[0]
	statchi = divresult[1]

	return render_template('index.html', chartnum=chartnum, btctradevolume=btctradevolume, usdtradevolume=usdtradevolume, estvolusd=estvolusd, totalfeebtc=totalfeebtc, ccysymamolist=ccysymamolist, ccydroplist=ccydroplist, ccysetlist=ccysetlist, price15min=price15min, symbollist=symbollist, pricelist=pricelist, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur)

@chart.route('/15days')
def c15():
	chartnum = 15
#Var
	actualpricelist = []
	actualpricelist_rev = []
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	ccysetlist = []
	for ccys in ccyset():
		ccysetlist.append(ccys)
	ccysetlist.sort(key=lambda x:x[0])

	symbollist = []
	pricelist = []
	for sym in ccysymbol():
		symbollist.append(sym)
	for pl in ccyprice():
		pricelist.append(pl)

	ccydroplist = []
	for ccyd in ccydrop():
		ccydroplist.append(ccyd)

	ccysymamolist = []
	for ccysa in ccysymamo():
		ccysymamolist.append(ccysa)
	ccysymamolist.sort(key=lambda x:x[0])

#General stock infos
	price15min = sorted(['%s%d'%(a,b) for a,b in zip(symbollist, pricelist)], key=lambda symbols:symbols[0])

#Statistics tab
	btctradevolume = stats.trade_volume_btc
	usdtradevolume = stats.trade_volume_usd
	estvolusd = stats.estimated_transaction_volume_usd
	totalfeebtc = stats.total_fees_btc

#array for numpy
	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = len(aplrev)
	divresult = scipy.stats.chisquare(aplrev)
	statpval = divresult[0]
	statchi = divresult[1]

	return render_template('index.html', chartnum=chartnum, btctradevolume=btctradevolume, usdtradevolume=usdtradevolume, estvolusd=estvolusd, totalfeebtc=totalfeebtc, ccysymamolist=ccysymamolist, ccydroplist=ccydroplist, ccysetlist=ccysetlist, price15min=price15min, symbollist=symbollist, pricelist=pricelist, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur)

@chart.route('/30days')
def c30():
	chartnum = 30
#Var
	actualpricelist = []
	actualpricelist_rev = []
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	ccysetlist = []
	for ccys in ccyset():
		ccysetlist.append(ccys)
	ccysetlist.sort(key=lambda x:x[0])

	symbollist = []
	pricelist = []
	for sym in ccysymbol():
		symbollist.append(sym)
	for pl in ccyprice():
		pricelist.append(pl)

	ccydroplist = []
	for ccyd in ccydrop():
		ccydroplist.append(ccyd)

	ccysymamolist = []
	for ccysa in ccysymamo():
		ccysymamolist.append(ccysa)
	ccysymamolist.sort(key=lambda x:x[0])

#General stock infos
	price15min = sorted(['%s%d'%(a,b) for a,b in zip(symbollist, pricelist)], key=lambda symbols:symbols[0])

#Statistics tab
	btctradevolume = stats.trade_volume_btc
	usdtradevolume = stats.trade_volume_usd
	estvolusd = stats.estimated_transaction_volume_usd
	totalfeebtc = stats.total_fees_btc

#array for numpy
	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = len(aplrev)
	divresult = scipy.stats.chisquare(aplrev)
	statpval = divresult[0]
	statchi = divresult[1]

	return render_template('index.html', chartnum=chartnum, btctradevolume=btctradevolume, usdtradevolume=usdtradevolume, estvolusd=estvolusd, totalfeebtc=totalfeebtc, ccysymamolist=ccysymamolist, ccydroplist=ccydroplist, ccysetlist=ccysetlist, price15min=price15min, symbollist=symbollist, pricelist=pricelist, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur)

@chart.route('/60days')
def c60():
	chartnum = 60
#Var
	actualpricelist = []
	actualpricelist_rev = []
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	ccysetlist = []
	for ccys in ccyset():
		ccysetlist.append(ccys)
	ccysetlist.sort(key=lambda x:x[0])

	symbollist = []
	pricelist = []
	for sym in ccysymbol():
		symbollist.append(sym)
	for pl in ccyprice():
		pricelist.append(pl)

	ccydroplist = []
	for ccyd in ccydrop():
		ccydroplist.append(ccyd)

	ccysymamolist = []
	for ccysa in ccysymamo():
		ccysymamolist.append(ccysa)
	ccysymamolist.sort(key=lambda x:x[0])

#General stock infos
	price15min = sorted(['%s%d'%(a,b) for a,b in zip(symbollist, pricelist)], key=lambda symbols:symbols[0])

#Statistics tab
	btctradevolume = stats.trade_volume_btc
	usdtradevolume = stats.trade_volume_usd
	estvolusd = stats.estimated_transaction_volume_usd
	totalfeebtc = stats.total_fees_btc

#array for numpy
	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = len(aplrev)
	divresult = scipy.stats.chisquare(aplrev)
	statpval = divresult[0]
	statchi = divresult[1]

	return render_template('index.html', chartnum=chartnum, btctradevolume=btctradevolume, usdtradevolume=usdtradevolume, estvolusd=estvolusd, totalfeebtc=totalfeebtc, ccysymamolist=ccysymamolist, ccydroplist=ccydroplist, ccysetlist=ccysetlist, price15min=price15min, symbollist=symbollist, pricelist=pricelist, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur)

@chart.route('/90days')
def c90():
	chartnum = 90
#Var
	actualpricelist = []
	actualpricelist_rev = []
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	ccysetlist = []
	for ccys in ccyset():
		ccysetlist.append(ccys)
	ccysetlist.sort(key=lambda x:x[0])

	symbollist = []
	pricelist = []
	for sym in ccysymbol():
		symbollist.append(sym)
	for pl in ccyprice():
		pricelist.append(pl)

	ccydroplist = []
	for ccyd in ccydrop():
		ccydroplist.append(ccyd)

	ccysymamolist = []
	for ccysa in ccysymamo():
		ccysymamolist.append(ccysa)
	ccysymamolist.sort(key=lambda x:x[0])

#General stock infos
	price15min = sorted(['%s%d'%(a,b) for a,b in zip(symbollist, pricelist)], key=lambda symbols:symbols[0])

#Statistics tab
	btctradevolume = stats.trade_volume_btc
	usdtradevolume = stats.trade_volume_usd
	estvolusd = stats.estimated_transaction_volume_usd
	totalfeebtc = stats.total_fees_btc

#array for numpy
	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = len(aplrev)
	divresult = scipy.stats.chisquare(aplrev)
	statpval = divresult[0]
	statchi = divresult[1]

	return render_template('index.html', chartnum=chartnum, btctradevolume=btctradevolume, usdtradevolume=usdtradevolume, estvolusd=estvolusd, totalfeebtc=totalfeebtc, ccysymamolist=ccysymamolist, ccydroplist=ccydroplist, ccysetlist=ccysetlist, price15min=price15min, symbollist=symbollist, pricelist=pricelist, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur)
