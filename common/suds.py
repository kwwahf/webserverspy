# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 0028 下午 4:21
# @Author  : K
# @Email   : kwwahf@163.com
# @File    : suds.py
# @Software: PyCharmc

from suds.client import Client


user_url = "http://120.24.235.105:8080/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"  # 这里是你的webservice访问地址
client = Client(user_url)  # Client里面直接放访问的URL，可以生成一个webservice对象

print(client)
