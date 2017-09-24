Python. version 3.x
# Python 3 proxy example
# http://www.geosurf.com/resources/residential-ips-integration-guide

import urllib.request as req

# Our gateway’s hosthname + port, check your dashboard for full gateways list
gs_proxy_addr = ‘gw1.geosurf.io:8081’

proxy = req.ProxyHandler({‘http’: gs_proxy_addr,
                          ‘https’: gs_proxy_addr})

opener = req.build_opener(proxy)
req.install_opener(opener)

req.urlopen(‘http://www.google.com’)
req.urlopen(‘https://www.google.com’)
