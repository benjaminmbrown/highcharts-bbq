#!/user/bin/env python2.7
import json
import random
from tornado import websocket, web, ioloop
import datetime
from time import time

#rando number
r = lambda: random.randint(0,255)

class WebSocketHandler(websocket.WebSocketHandler):
	def open(self):
		print 'Connection established'
		#set up call to send_data in 5 seconds
		ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=1), self.send_data)

	def on_message(self, message):
		print 'Message received {0}.'.format(message)

	def on_close(self):
		print "Connection closed"

	#get new random data for charting
	def send_data(self):
		point_data = {
		'x' : int(time()),
		'y' : r(),
		'color' : '#%02X%02X%02X' % (r(), r(), r())
		}

		self.write.message(json.dumps(point_data))
		timeout = r() / 10

		#Call this again within the next 0-25 seconds
		ioloop.IOLoop.instance().add_timeout(datetime.timedelta(seconds=timeout), self.send_data)

application = web.Application([
	(r'/websocket', WebSocketHandler)
	])

if __name__ == "__main__":
	application.listen(8001)
	ioloop.IOLoop.instance().start()