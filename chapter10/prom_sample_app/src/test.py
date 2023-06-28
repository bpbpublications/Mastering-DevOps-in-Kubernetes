import concurrent.futures, os, requests
from prometheus_client import Gauge, make_wsgi_app
from wsgiref.simple_server import make_server

state = Gauge('httpstat_url_up',
                    'httpstat URL state', ['url'])

class verify_url:
    def __init__(self,urls,timeoutSec,state):
        self.urls = urls
        self.state = state
        self.timeoutSec = timeoutSec

    def request_loop(self):
         for url in self.urls:
             r = requests.get(url, timeout=self.timeoutSec)
             if r.status_code == 200:
                self.state.labels(self.urls).set(1)
             else:
                self.state.labels(self.urls).set(0)

def my_app(environ, start_fn):
    if environ['PATH_INFO'] == '/metrics':
        global verifyUrlObj
        verifyUrlObj.request_loop()
        metrics_app = make_wsgi_app()
        return metrics_app(environ, start_fn)
    start_fn('200 OK', [])
    return [b'The httpstat server is reachable !! ']

if __name__ == '__main__':
    urls = os.getenv('URLS').split(',')
    timeoutSec = int(os.getenv('TIMEOUT'))
    verifyUrlObj = verify_url(urls,state,timeoutSec)

    port = int(os.getenv('PORT') or 8000)
    httpd = make_server('0.0.0.0', port, my_app)
    print("Serving on port {}".format(port))
    httpd.serve_forever()
