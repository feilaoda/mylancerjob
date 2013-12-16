# -*- coding: utf-8 -*-
#!/usr/bin/env python

import gevent
from gevent import monkey, queue
monkey.patch_all()
from time import sleep
import os
import sys
import pyaudio
import wave
import time
import sys
import logging
import traceback
import threading
import json
import urllib2
import redis
import tornadoredis

#tc = tornadoredis.Client()
#tc.connect()
tc =  redis.Redis()



logger = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)

OKCOIN_URL = "http://www.okcoin.com/api/ticker.do?symbol=ltc_cny"

def create_request(url, headers=None):
    request = urllib2.Request(url)
    if headers:
        for k,v in headers.items():
            request.add_header(k, v)
    return request



class WavePlayer(threading.Thread) :
    """
    A simple class based on PyAudio to play wave loop.

    It's a threading class. You can play audio while your application
    continues to do its stuff. :)
    """

    CHUNK = 2048

    def __init__(self,filepath,loop=True) :
        """
        Initialize `WavePlayerLoop` class.

        PARAM:
            -- filepath (String) : File Path to wave file.
            -- loop (boolean)    : True if you want loop playback. 
                                   False otherwise.
        """
        super(WavePlayer, self).__init__()
        self.filepath = os.path.abspath(filepath)
        self.loop = loop

    def callback(self, in_data, frame_count, time_info, status):
        data = self.wf.readframes(frame_count)
        if data == '' : # If file is over then rewind.
            print "callback data is ''"
            self.wf.rewind()
            data = self.wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    def run(self):
        # Open Wave File and start play!
        self.wf = wave.open(self.filepath, 'rb')
        player = pyaudio.PyAudio()

        # Open Output Stream (basen on PyAudio tutorial)
        stream = player.open(format = player.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True,
            stream_callback = self.callback)

        stream.start_stream()
        while self.loop:
            if stream.is_active():
                time.sleep(0.1)
            else:
                #self.wf.rewind()
                stream.stop_stream()
                self.wf.setpos(0)
                stream.start_stream()

        stream.stop_stream()
        stream.close()
        player.terminate()
        self.wf.close()


    def play(self) :
        """
        Just another name for self.start()
        """
        self.start()

    def stop(self) :
        """
        Stop playback. 
        """
        self.loop = False


class EasyWorker:
    def __init__(self, min_val, max_val):
        self.qin = queue.Queue(0)
        self.jobs = [gevent.spawn(self.do_fetch_data)]
        self.jobs += [gevent.spawn(self.do_alarmer)]
        self.job_count = len(self.jobs)
        self.headers = dict()
        self.headers['Accept'] = 'application/json;q=0.9,image/webp,*/*;q=0.8'
        self.min = min_val
        self.max = max_val
        self.alarming = False

    def start(self):
        gevent.joinall(self.jobs)


    def start_alarm(self):
        self.player = WavePlayer("alarm.wav", True)
        self.player.play()
        self.alarming = True

    def stop_alarm(self):
        self.player.stop()
        self.alarming = False



    def do_fetch_data(self):
        try:
            count = 0
            while True:
                #fetch data from okcoin
                res = self.fetch_data(OKCOIN_URL)
                try:
                    if res['code'] == 200:
                        last = float(res['last'])
                        tc.publish('okcoin_ltc', last)
                        print "last value:", last, self.min, self.max
                        if last >= self.max and self.alarming == False:
                            self.qin.put("startalarm")
                            print "start max alarm"

                        if last <= self.min and self.alarming == False:
                            self.qin.put("startalarm")
                            print "start min alarm"

                        if last < self.max and last > self.min and self.alarming == True:
                            self.qin.put("stopalarm")
                            print( "stop alarm")

                except Exception, e:
                    pass
                
                

                sleep(8)

        except Exception, e:
            logging.error("Scheduler Error!\n%s" % traceback.format_exc())
        finally:
            for i in range(self.job_count - 2):
                self.qin.put(StopIteration)
            self.job_count -= 1
            logging.debug("Scheduler done, job count: %s" % self.job_count)

    def fetch_data(self, url):
        logging.debug("Download starting...\n[%s]" % url)
        request = create_request(url, self.headers)
        try:
            response = urllib2.urlopen(request, timeout=10)
            html = response.read()
            if ('Content-Encoding' in response.headers and response.headers['Content-Encoding']) or \
                    ('content-encoding' in response.headers and response.headers['content-encoding']):
                    import gzip
                    import StringIO
                    data = StringIO.StringIO(html)
                    gz = gzip.GzipFile(fileobj=data)
                    html = gz.read()
                    gz.close()

            if 'Set-Cookie' in response.headers:
                cookies = response.headers['Set-Cookie']
                self.headers['Cookie'] = cookies

            response.close()
            logging.debug("Download end\n[%s]" % html)
            print html
            try:
                res = json.loads(html)
                low = res['ticker']['low']
                high = res['ticker']['high']
                last = res['ticker']['last']
                return dict(code=200, url=url, html=html, low=low, high=high, last=last)
            except Exception, e:
                logging.error("load error html json %s\n%s" % (html, traceback.format_exc()))
            

        except urllib2.HTTPError, e:
            logging.error('you got an error with the http code %s' % traceback.format_exc()) 
            return dict(code = e.code)
        except urllib2.URLError, e:
            logging.error('you got an error with the url code %s' % traceback.format_exc())
            return dict(code = 500)

        return dict(code=-1)


    def do_alarmer(self):
        try:
            item = self.qin.get()
            while item != StopIteration:
                try:
                    if item == "startalarm":
                        logging.debug( "get start")
                        
                        self.start_alarm()
                    elif item == "stopalarm":
                        logging.debug( "get stop")
                        self.stop_alarm()
                        
                except:
                    logging.error("Worker error!\n%s" % traceback.format_exc())
                item = self.qin.get()
        finally:
            self.job_count -= 1
            logging.debug("Worker done, job count: %s" % self.job_count)



if __name__ == "__main__":
    logger.debug("start bitfrom") 
    minval = float(sys.argv[1])
    maxval = float(sys.argv[2])

    worker = EasyWorker(minval, maxval)
    worker.start()
    # res = worker.fetch_data('https://www.okcoin.com/api/ticker.do?symbol=ltc_cny')
    # print 'last = %s' % res['last']


