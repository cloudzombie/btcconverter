from flask import Flask, render_template, request, redirect, url_for, Blueprint
from blockchain import exchangerates, statistics
from flask import Blueprint
import urllib2, json, requests, datetime

chart = Blueprint('chart',__name__)

@chart.route('/3days')
def c3():
	chartnum = 3
	return render_template('index.html', chartnum=chartnum)

@chart.route('/7days')
def c7():
	chartnum = 7
	return render_template('index.html', chartnum=chartnum)

@chart.route('/15days')
def c15():
	chartnum = 15
	return render_template('index.html', chartnum=chartnum)

@chart.route('/30days')
def c30():
	chartnum = 30
	return render_template('index.html', chartnum=chartnum)

@chart.route('/60days')
def c60():
	chartnum = 60
	return render_template('index.html', chartnum=chartnum)

@chart.route('/90days')
def c90():
	chartnum = 90
	return render_template('index.html', chartnum=chartnum)
