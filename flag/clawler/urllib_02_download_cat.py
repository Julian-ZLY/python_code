"""爬取图片"""

from urllib import request
import os
from time import sleep

# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def save_image(file_name, html_byte):
    file_name = './bigFaceCat/' + file_name
    with open(file_name, 'wb') as f:
        f.write(html_byte)
    f.close()


# url = 'http://image.biaobaiju.com/uploads/20180803/20/1533300579-gnUBlQZPbt.jpg'
# url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1577378615116&di=1cdaa34ad5ab21558740e6738d27729e&imgtype=0&src=http%3A%2F%2Fimage.biaobaiju.com%2Fuploads%2F20180803%2F20%2F1533300497-rVRKEFjhPt.jpg'
# url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1577379111953&di=4c5743b0f180cf07bc18a24941d48f41&imgtype=0&src=http%3A%2F%2Fgss0.baidu.com%2F7Po3dSag_xI4khGko9WTAnF6hhy%2Fzhidao%2Fpic%2Fitem%2F7c1ed21b0ef41bd572ea367f5ada81cb38db3d84.jpg'

def get_url():
    # url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%A8%DF%E4&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
    # url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1577374605608_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E5%B0%8F%E7%8B%97'
    # url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1577375701881_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E7%B1%B3%E5%A5%87'
    url = 'https://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs4&word=%E5%A4%A7%E8%84%B8%E7%8C%AB%E5%9B%BE%E7%89%87%E5%91%86%E8%90%8C&oriquery=%E5%91%86%E8%90%8C%E5%A4%A7%E8%84%B8%E7%8C%AB%E5%A4%B4%E5%83%8F&ofr=%E5%91%86%E8%90%8C%E5%A4%A7%E8%84%B8%E7%8C%AB%E5%A4%B4%E5%83%8F&hs=2&sensitive=0'
    request_web = request.urlopen(url)

    html = str(request_web.read(), encoding='utf8')

    html_list = html.split('\n')

    for each in html_list:
        if '.jpg' in each:

            all_jpg_list = each.split()

            cat_dict = dict()
            cat_num = 1
            for image_url in all_jpg_list:
                if 'objURL' in image_url:
                    # print(image_url)
                    image_url = image_url.split('\"')[3]
                    cat_name = 'big_face_cat_' + str(cat_num) + '.jpg'
                    cat_dict[cat_name] = image_url
                    cat_num += 1
            return cat_dict


def request_html():
    cat_dict = get_url()

    for cat_name in cat_dict:
        # sleep(2)
        try:
            print('请求中...', cat_dict[cat_name])
            request_web = request.urlopen(cat_dict[cat_name], timeout=15)
        except Exception as e:
            print('Error:', e)
        else:
            html = request_web.read()
            print('请求成功', cat_name)
            sleep(1)
            save_image(cat_name, html)
            # print(html)


if __name__ == '__main__':
    request_html()
    # print(get_url())

