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
actualpricelist = []
actualtimelist = []
actualpricelist_rev = []
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

	for ap in actualprice():
		actualpricelist_rev.append(ap)

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

	return render_template('index.html', statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur)


@chart.route('/3days')
def c3():
	chartnum = 3

	for ap in actualprice():
		actualpricelist_rev.append(ap)

#array for numpy
	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:3]

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = np.num(statsample)


	return render_template('index.html', statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)

@chart.route('/7days')
def c7():
	chartnum = 7

	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:7]

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = np.num(statsample)


	return render_template('index.html', statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)

@chart.route('/15days')
def c15():
	chartnum = 15

	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:15]

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = np.num(statsample)

	return render_template('index.html', statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)

@chart.route('/30days')
def c30():
	chartnum = 30
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:30]

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = np.num(statsample)

	return render_template('index.html', statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)


@chart.route('/60days')
def c60():
	chartnum = 60
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:60]

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = np.num(statsample)

	return render_template('index.html', statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)

@chart.route('/90days')
def c90():
	chartnum = 90
	for ap in actualprice():
		actualpricelist_rev.append(ap)

	actualpricelist_rev.reverse()
	aplrev = actualpricelist_rev[:90]

#stats datas
	statsample = np.array(aplrev)
	statmin = np.min(statsample)
	statmax = np.max(statsample)
	statvar = np.var(statsample)
	statmean = np.mean(statsample)
	statskew = scipy.stats.skew(statsample)
	statkur = scipy.stats.kurtosis(statsample)
	statnum = np.num(statsample)

	return render_template('index.html', statnum=statnum, statmean=statmean, statmin=statmin, statmax=statmax, statvar=statvar, statskew=statskew, statkur=statkur, chartnum=chartnum)
