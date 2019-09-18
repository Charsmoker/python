#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import sys
import re

def test_news(name, Str_value, Curl, Call):
    Str = f'{name}的客户端版本打包完了！'
    if jenkins_name[1] == 'update8090client':
        Str = Str_value
        Curl = project_Url['dzsg']
    headers = {'Content-Type':'application/json'}   ##网络推包的头文件
    ##json用的data
    data = {
        "msgtype": "text",
        "text": {
            "content":Str,
            "mentioned_mobile_list":Call
        }
    }
    ##开始推包
    r = requests.post(
        Curl, headers = headers, json = data
    )
    ##看看有没有回包，有就代表推包成功
    print(r.text,Str)

project_name = {
    'dzsg_Cross':'跨服国战',
    'dzsg_fanti_External':'繁体版本',
    'dzsg_External':'主干',
    'update8090client':'体验服',
    'xy_HongKong':'西游港澳台',
    'xy_bt_jitan':'西游飞升版本',
    'xy_bt':'西游变态',
    'xy_webmobile':'西游联运'
}

project_Url = {
    'dzsg':'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=8d9990c7-4f34-4b9f-9b31-e776bbb0a21c',
    'xy':'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=572a7fd4-4985-4364-b48f-530600a592b6'
}

project_Call = {
    'dzsg':[""],
    'xy':['']
}

if __name__ == '__main__':
    jenkins_name = [1,'xy_webmobile']  #调用脚本时，接受传进来的值
    j_name = '某个项目'  ##这几个是给个默认名字
    Str = '体验服已更完客户端'
    first_name = 'dzsg'
    ##特殊处理的体验服更新
    if jenkins_name[1] != 'update8090client':
        first_name = re.match(r'(\w+?)\_',jenkins_name[1]).group(1)
    ##判断是哪个工程
    j_name = project_name[jenkins_name[1]]
    ##确定用哪个机器人
    pro_url = project_Url[first_name]
    ##确定@谁
    pro_call = project_Call[first_name]

    test_news(j_name, Str, pro_url, pro_call)  #传包给机器人的函数
