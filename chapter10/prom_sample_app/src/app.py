import prometheus_client as prom
import random
import time

req_summary = prom.Summary('devops_sample_app', 'Sample Metrics for Learning')


@req_summary.time()
def sample_request(t):
   time.sleep(t)


if __name__ == '__main__':

   counter = prom.Counter('devops_app_counter', 'DevOps app counter')
   gauge = prom.Gauge('devops_app_gauge', 'DevOps app gauge')
   histogram = prom.Histogram('devops_app_histogram', 'DevOps app histogram')
   summary = prom.Summary('devops_app_summary', ' DevOps app summary')
   prom.start_http_server(8080)

   while True:
       counter.inc(random.random())
       histogram.observe(random.random() * 7)
       gauge.set(random.random() * 8)
       sample_request(random.random() * 9)
       summary.observe(random.random() * 10)
       

       time.sleep(1)
