"""获取IP地址"""

from urllib import request
import ssl
import re
import os, sys

# ip: 49.70.17.90

ssl._create_default_https_context = ssl._create_unverified_context


def request_web():
    url_str = 'https://www.xicidaili.com'

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

    headers = {
        'User-Agent': user_agent
    }

    url = request.Request(url_str, headers=headers)

    request_web = request.urlopen(url)

    html = str(request_web.read(), encoding='utf-8')

    with open('./source_web.html', 'w') as f:
        f.write(html)


def getIP():
    with open('./source_web.html', 'r') as f:
        for each in f:
            # ip = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", each)
            # ip = re.findall(r"([0-9]{1,3}\.)", each)
            ip = re.findall(r'(([01]\d{0,1}\d{0,1}|2[0-5]\d{0,1}|25[0-5])\.){3}([01]\d{0,1}\d{0,1}|2[0-5]\d{0,1}|[25[0-5])', each)
            if ip:
                print(ip)


if __name__ == '__main__':
    getIP()
