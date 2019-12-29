#!/usr/bin/env python
# -*- coding: utf-8 -*-

# /config/game/redpacket/游戏名/server_type

import sys
from kazoo.client import KazooClient
import json
import time
from kazoo.client import DataWatch
import os
import re

exlude_list = ['match_score_table.csv', 'match_relive_table.csv', 'match_hf_score_table.csv',
               'match_final_score_table.csv', 'match_preliminary_score_table.csv', 'online_award_data.csv',
               'round_award_data.csv', 'dila_config.csv', 'game_level_data.csv', 'advantage.csv',
               'mahjong_quick_achieve_data.csv', 'private_room_data.csv', 'private_card_cost_config.csv',
               'server_version', 'game_version.csv', 'vip_data.csv', 'item_data.csv', 'achieve_data.csv',
               'bad_word.csv', 'login_award_data.csv  ', 'sign_award_data.csv', 'game_item_list.csv',
               'game_item_desc_list.csv', 'turntable_config.csv', 'player_level_data.csv']

# 获取参数
host = "%s" % sys.argv[5]
port = "2181"
timeout = 100

# 连接 zookeeper; 格式 127.0.0.1:2181; 超时时间为 100 秒
zkc = KazooClient(hosts=host + ':' + port, timeout=timeout)
# 启动 zookeeper
zkc.start()

# zookeeper 内路径; /config
path_1 = '/config'

tem_path_1 = '/node'

# 如果参数为 4 个; 路径为 '/config' 打头
if len(sys.argv) == 4:
    # path2 = '/config/game'
    path_2 = path_1 + '/' + sys.argv[1]
    # path3 = '/config/game/redpacket'
    path_3 = path_2 + '/' + sys.argv[2]

    # 查看 path3 中是否有 lobby 关键字; lobby 为中央服务器存储位置
    if path_3.find('lobby') == -1:
        # 如果没有, 退出脚本
        sys.exit('error!!!!,参数输入错误,路径%s不存在' % path_3)

    # ######
    tem_path_3 = tem_path_1 + '/' + sys.argv[1] + '/' + sys.argv[2]

    # 指定游戏工作目录为'/ops'
    file_dir = '/ops'



# 如果参数为 6 时; 意味着路径为 '/node' 打头
elif len(sys.argv) == 6:

    path_2 = path_1 + '/' + sys.argv[1]
    path_3 = path_2 + '/' + sys.argv[2]
    path_4 = path_3 + '/' + sys.argv[3]
    path_5 = path_4 + '/' + sys.argv[4]
    if path_5.find('game') == -1:
        sys.exit('error!!!!,参数输入错误,路径%s不存在' % path_5)
    tem_path_5 = tem_path_1 + '/' + sys.argv[1] + '/' + sys.argv[2] + '/' + sys.argv[3] + '/' + sys.argv[4]
    file_dir = '/ops'
else:
    sys.exit('error!!!!,请输入3个或5个参数')



# 调用系统模块 os; 查看 /ops 文件夹是否存在; 不存在则创建
if not os.path.exists(file_dir):
    os.mkdir(file_dir)


# 函数 01; 参数为 zookeeper 路径
def file_exists(path):
    # 获取第一个元素
    content = zkc.get(path)[0]

    # 如果元素不为空
    if content:
        # key 为文件名; values 为该文件的内容
        for k, v in eval(content).items():
            print(k, v)

            # 排除文件
            if k in exlude_list:
                continue

            #
            content = v
            if k.find('csv') == -1:
                k = k.replace('_xml', '.xml')
            else:
                k = k.replace('_csv', '.csv')
            with open('%s/%s' % (file_dir, k), 'w') as f:
                # f.write(str(content).decode("unicode_escape").encode('utf8'))
                f.write(str(content))


def change_robot_data(severid, port):
    with open('/ops/robotconfig.xml', 'r') as fr:
        data = fr.read()
    s_len = len(str(severid))
    zero_len = 15 - s_len - 2 - 1
    robotagentid = '99' + str(severid) + '0' * zero_len + '1'
    robotbeginid = '99' + str(severid) + '0' * zero_len + '2'
    listen_port = re.compile(r'listenport *= *"(\d+)"')
    robotagent_id = re.compile(r'robotagentid *= *"(\d+)"')
    robotbegin_id = re.compile(r'robotbeginid *= *"(\d+)"')
    content = re.sub(robotagent_id, 'robotagentid="%s"' % robotagentid, data)
    content_1 = re.sub(robotbegin_id, 'robotbeginid="%s"' % robotbeginid, content)
    content_2 = re.sub(listen_port, 'listenport="%s"' % port, content_1)
    print(content_2)
    with open('/ops/robotconfig.xml', 'w') as fw:
        fw.write(content_2)


def change_server_data(severid):
    with open('/ops/serverconfig.xml', 'r') as fr:
        data = fr.read()
    s_len = len(str(severid))
    zero_len = 15 - s_len - 2 - 1
    robotagentid = '99' + str(severid) + '0' * zero_len + '1'
    robot_agent_id = re.compile(r'robot_agent_id *= *"(\d+)"')
    server_id = re.compile(r'server_id *= *"(\d+)"')
    content = re.sub(server_id, 'server_id="%s"' % severid, data)
    content_1 = re.sub(robot_agent_id, 'robot_agent_id="%s"' % robotagentid, content)
    print(content_1)
    with open('/ops/serverconfig.xml', 'w') as fw:
        fw.write(content_1)


def listen_node(node_path):
    if zkc.exists(node_path):
        print(node_path)
        print('-----------')
        file_exists(node_path)
    else:
        print(node_path, '节点不存在')


listen_node(path_1)
listen_node(path_2)
listen_node(path_3)

if len(sys.argv) == 6:
    listen_node(path_4)
    listen_node(path_5)

file_test = '/ops/robotconfig.xml'
if os.path.exists(file_test):
    server_info = eval(zkc.get(path_5)[0])
    serverid = server_info['server_id']
    port = server_info['port']
    change_robot_data(serverid, port)
    change_server_data(serverid)
    print(server_info)

zkc.stop()