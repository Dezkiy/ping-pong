
import time
import http.client

while True:
    conn = http.client.HTTPConnection("server")
    conn.request("GET", "/ping")
    res = conn.getresponse()
    print(res.read().decode())

    time.sleep(5)
