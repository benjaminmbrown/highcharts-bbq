#!/usr/bin/env python2.7
import json
import random
from tornado import websocket, web, ioloop
import datetime
from time import time

# Random number generator
r = lambda: random.randint(0,255)

# Boilerplate WebSocket code
class WebSocketHandler(websocket.WebSocketHandler):
  def open(self):
    print 'Connection established.'
    # Set up a call to send_data in 5 seconds
    ioloop.IOLoop.instance().add_timeout(datetime.       
    timedelta(seconds=1), self.send_data)

  def on_message(self, message):
    print 'Message received {0}.'.format(message)

  def on_close(self):
    print 'Connection closed.'

  # Our function to get new (random) data for charts
  def send_data(self):
    point_data = {
      'x': int(time()),
      'y': r(),
      'color': '#%02X%02X%02X' % (r(), r(), r())
    }
    print self
    self.write_message(json.dumps(point_data))
    timeout = r() / 15
    
    # Call this again within the next 0-25 seconds
    ioloop.IOLoop.instance().add_timeout(datetime.
    timedelta(seconds=timeout), self.send_data)
    
application = web.Application([
  (r'/websocket', WebSocketHandler)
])

if __name__ == "__main__":
  application.listen(8001)
  ioloop.IOLoop.instance().start()