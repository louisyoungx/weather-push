# -*- coding: utf8 -*-
import requests
import json
import yaml
import time

from Logger.logger import logger
from Message.message import message


def getApi(name, url, params):
    '''
    get方式调用api
    :param name: api名称
    :param url: api链接
    :param params: api参数（dict）
    :return: api返回值
    '''
    res = json.loads(requests.get(url, params).text)
    logger.info('【{}】接口测试正常✔'.format(name))
    return res


def getWeather(dirItem):
    '''
    调用api获取天气信息
    :param dirId: 地区编码
    :return: 今日天气信息
    '''
    weatherUrl = "https://v0.yiketianqi.com/api"
    weatherParams = {'key': 'c369a5115a88fe279e8c6de3ba5fd8c7',
                     'extensions': 'all',
                     'version': 'v61',
                     'appid': '89242654',
                     'appsecret': 'xWUqH42f ',
                     'province': dirItem[0],
                     'city': dirItem[1],
                     }
    return getApi('天气api', weatherUrl, weatherParams)


def getInfo(res):
    '''
    从获取的天气信息中筛选要发送的数据
    :param res: 天气信息
    :return: 要发送的数据
    '''
    print(res)
    dataList = []
    date = res['date']
    week = res['week']
    wea = res['wea']
    wea_img = res['wea_img']
    tem = res['tem']
    tem1 = res['tem1']
    tem2 = res['tem2']
    win = res['win']
    win_speed = res['win_speed']
    visibility = res['visibility']
    air_level = res['air_level']
    air_tips = res['air_tips']
    pm25_desc = res['aqi']['pm25_desc']
    yundong = res['aqi']['yundong']

    dataList.extend(
        [date, week, wea, wea_img, tem, tem1, tem2, win, win_speed, visibility, air_level, air_tips, pm25_desc,
         yundong])  # python同时添加多个元素
    return dataList


def QQPusher(qqNum, dataList):
    '''
    调用QQPusher接口，给指定qq发送消息
    :param qqNum: qq
    :param dataList: 要发送的数据列表
    '''
    mes = '今日天气推送🍀 \n---\n{}，{}\n{} ， {}\n{}  {}，{}/{} ℃\n{}，{}\n空气质量：{}，pm2.5：{}\n运动指数：{}\n---\n{}\n---\n当前气温：{}℃，能见度：{}\n温馨提示：疫情期间，外出请佩戴口罩！'.format(
            dataList[0], dataList[1], dataList[14], dataList[15], dataList[2], dataList[16], dataList[6], dataList[5],
            dataList[7], dataList[8], dataList[10], dataList[12], dataList[13], dataList[11], dataList[4], dataList[9])
    message.sendFriendMessage(mes, qqNum)


def QQGroupPusher(qqNum, dataList):
    '''
    调用QQPusher接口，给指定qq群发送消息
    :param qqNum: qq群
    :param dataList: 要发送的数据列表
    '''
    mes = '今日天气推送 🍀 \n---\n{}，{}\n{} ， {}\n{}  {}，{}/{} ℃\n{}，{}\n空气质量：{}，pm2.5：{}\n运动指数：{}\n---\n{}\n---\n当前气温：{}℃，能见度：{}\n温馨提示：疫情期间，外出请佩戴口罩！'.format(
        dataList[0], dataList[1], dataList[14], dataList[15], dataList[2], dataList[16], dataList[6], dataList[5],
        dataList[7], dataList[8], dataList[10], dataList[12], dataList[13], dataList[11], dataList[4], dataList[9])
    message.sendGroupMessage(mes, qqNum)