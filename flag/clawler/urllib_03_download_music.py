# -*- coding:utf-8 -*- 
"""下载mp3""" 

import ssl
from urllib import request


ssl._create_default_https_context = ssl._create_unverified_context
# ssl._create_default_https_context = ssl._create_unverified_context


def download_music():
    while True:
        url_str = str(input('请输入url:'))
        new_url = url_str.strip()

        if new_url:
            url = request.Request(new_url)

            request_web = request.urlopen(url)
            html = request_web.read()
        else:
            break

        print('请求成功!')
        file_name = str(input('请输入文件名称:'))
        file_name = './music/' + file_name

        new_file_name = file_name.strip()
        with open(new_file_name, 'wb') as f:
            print('写入文件中....')
            f.write(html)
        f.close()
        print('下载成功:\t', new_file_name)


if __name__ == '__main__':
    download_music()
