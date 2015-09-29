from flask import Flask, render_template, request, redirect, url_for, Blueprint
from blockchain import exchangerates, statistics
from flask import Blueprint
import urllib2, json, requests, datetime
import pandas as pd
import numpy as np
import scipy.stats

chart = Blueprint('chart',__name__)

#For statistics
stats = statistics.get()
actualtimelist = []
actualtimelist_rev = []

#Chart section
jsonfilein = 'https://blockchain.info/charts/market-price?showDataPoints=false&timespan=&show_header=true&daysAverageString=1&scale=0&format=json&address='
r = requests.get(jsonfilein)
j = r.json()
entries = j['values']


def actualprice():
	for e in entries:
		yield e['y']

@chart.route('/')
def c1():
	actualpricelist = []
	actualpricelist_rev = []
	for ap in actualprice():
		actualpricelist_rev.append(ap)

#array for numpy
	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev

#RSI - 5days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist5 = aplrev[:6]

	for i in xrange(5):
		rsia = rsilist5[rsix]
		rsib = rsilist5[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 5.0
	avgloss = sum(minuslist) / 5.0
	rs = avggain / avgloss
	rsi5 = 100 - 100 / (1 + rs)

#RSI - 14days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist14 = aplrev[:15]

	for i in xrange(14):
		rsia = rsilist14[rsix]
		rsib = rsilist14[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 14.0
	avgloss = sum(minuslist) / 14.0
	rs = avggain / avgloss
	rsi14 = 100 - 100 / (1 + rs)

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

	return render_template('index.html', rsi14=rsi14, rsi5=rsi5, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur)


@chart.route('/3days')
def c3():
	chartnum = 3
	actualpricelist = []
	actualpricelist_rev = []

	for ap in actualprice():
		actualpricelist_rev.append(ap)

#array for numpy
	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:3]
	rsi5 = "Not enough data"
	rsi14 = "Not enough data"

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

	return render_template('index.html', rsi14=rsi14, rsi5=rsi5, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)

@chart.route('/7days')
def c7():
	chartnum = 7
	actualpricelist = []
	actualpricelist_rev = []

	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:7]

#RSI - 5days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist5 = aplrev[:6]

	for i in xrange(5):
		rsia = rsilist5[rsix]
		rsib = rsilist5[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 5.0
	avgloss = sum(minuslist) / 5.0
	rs = avggain / avgloss
	rsi5 = 100 - 100 / (1 + rs)
	rsi14 = "Not enough data"

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


	return render_template('index.html', rsi14=rsi14, rsi5=rsi5, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)

@chart.route('/15days')
def c15():
	chartnum = 15
	actualpricelist = []
	actualpricelist_rev = []

	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:15]

#RSI - 5days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist5 = aplrev[:6]

	for i in xrange(5):
		rsia = rsilist5[rsix]
		rsib = rsilist5[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 5.0
	avgloss = sum(minuslist) / 5.0
	rs = avggain / avgloss
	rsi5 = 100 - 100 / (1 + rs)

#RSI - 14days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist14 = aplrev[:15]

	for i in xrange(14):
		rsia = rsilist14[rsix]
		rsib = rsilist14[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 14.0
	avgloss = sum(minuslist) / 14.0
	rs = avggain / avgloss
	rsi14 = 100 - 100 / (1 + rs)

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

	return render_template('index.html', rsi14=rsi14, rsi5=rsi5, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)

@chart.route('/30days')
def c30():
	chartnum = 30
	actualpricelist = []
	actualpricelist_rev = []

	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:30]

#RSI - 5days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist5 = aplrev[:6]

	for i in xrange(5):
		rsia = rsilist5[rsix]
		rsib = rsilist5[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 5.0
	avgloss = sum(minuslist) / 5.0
	rs = avggain / avgloss
	rsi5 = 100 - 100 / (1 + rs)

#RSI - 14days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist14 = aplrev[:15]

	for i in xrange(14):
		rsia = rsilist14[rsix]
		rsib = rsilist14[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 14.0
	avgloss = sum(minuslist) / 14.0
	rs = avggain / avgloss
	rsi14 = 100 - 100 / (1 + rs)

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

	return render_template('index.html', rsi14=rsi14, rsi5=rsi5, statpval=statpval, statchi=statchi, statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)


@chart.route('/60days')
def c60():
	chartnum = 60
	actualpricelist = []
	actualpricelist_rev = []

	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:60]

#RSI - 5days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist5 = aplrev[:6]

	for i in xrange(5):
		rsia = rsilist5[rsix]
		rsib = rsilist5[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 5.0
	avgloss = sum(minuslist) / 5.0
	rs = avggain / avgloss
	rsi5 = 100 - 100 / (1 + rs)

#RSI - 14days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist14 = aplrev[:15]

	for i in xrange(14):
		rsia = rsilist14[rsix]
		rsib = rsilist14[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 14.0
	avgloss = sum(minuslist) / 14.0
	rs = avggain / avgloss
	rsi14 = 100 - 100 / (1 + rs)

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

	return render_template('index.html', rsi14=rsi14, rsi5=rsi5, statnum=statnum, statpval=statpval, statchi=statchi, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)

@chart.route('/90days')
def c90():
	chartnum = 90
	actualpricelist = []
	actualpricelist_rev = []

	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:90]

#RSI - 5days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist5 = aplrev[:6]

	for i in xrange(5):
		rsia = rsilist5[rsix]
		rsib = rsilist5[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 5.0
	avgloss = sum(minuslist) / 5.0
	rs = avggain / avgloss
	rsi5 = 100 - 100 / (1 + rs)

#RSI - 14days
	pluslist = []
	minuslist = []
	rsix = 0
	rsiy = 1
	rsilist14 = aplrev[:15]

	for i in xrange(14):
		rsia = rsilist14[rsix]
		rsib = rsilist14[rsiy]
		rsiz = rsib - rsia
		if rsiz > 0.0:
			pluslist.append(rsiz)
		else:
			minuslist.append(-rsiz)
		rsix += 1
		rsiy += 1
	avggain = sum(pluslist) / 14.0
	avgloss = sum(minuslist) / 14.0
	rs = avggain / avgloss
	rsi14 = 100 - 100 / (1 + rs)

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

	return render_template('index.html', rsi14=rsi14, rsi5=rsi5, statnum=statnum, statpval=statpval, statchi=statchi, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)
