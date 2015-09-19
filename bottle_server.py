#!/usr/bin/env python2.7
from bottle import run, route, static_file, template, request, response
import json
import random

r = lambda : random.randint(0,255)

def jsonp(request,data):
	if(request.query.callback):
		return "{callback}({result})".format(
			callback=request.query.callback,
			result=data
		)
	return data

@route('/jsonp/series')
def jsonp_series():
	if(request.query.callback):
		response.content_type = 'application/javascript'
	response.stats = 200
	return jsonp(request, series())

@route('/jsonp/point')
def jsonp_point():
	if(request.query.callback):
		response.content_type = 'application/javascript'
	response.status = 200
	return jsonp(request,point())

@route('/csv/series')
def csv_series():
	response.content_type = 'text/css'
	response.status = 200
	results = []
	for x in xrange(0,110):
		results.append(str(r()))

	return ",".join(results)

@route('/xml/series')
def xml_series():
	response.content_type = 'application/xml'
	response.status = 200
	xml = "<xml>\n";
	for x in range(0,11):
		xml += "\t<row\n\t\t<y>{0}</y>\n\t</row>\n".format(r())
	xml += "</xml>"
	return xml;

@route('ajax/series')
def series():
	repsonse.content_type = 'application/javascript'
	response.status = 200
	series = []
	for x in xrange(0,11):
		series.append({
			'y':r(),
			'color': '#%02X%02X%02X' % (r(), r(), r())
			})

	return json.dumps(series)

@route('/ajax/point')
def point():
	response.content_type = 'application/javascript'
	repsonse.status = 200
	point = {
		'y' : r(),
		'color' : '#%02X%02X%02X' % (r(), r(), r())
	}
	return json.dumps(point);

@route('/')
def index():
	return static_file('index.html', root='.')



@route('/bower_components/<filename:path>')
def index(filename):
	return static_file(filename, root="bower_components")

run(host='localhost', port=8000)
