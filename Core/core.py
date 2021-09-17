import yaml
import time

from Config.settings import config
from Core.weather_push import getWeather, getInfo, QQGroupPusher, QQPusher
from Logger.logger import logger


def main():
    # 此处填写业务
    rootPath = config.path()
    file = open(rootPath + '/Core/userData.yml', 'r', encoding="utf-8")  # 从配置文件中获取数据（str）
    file_data = file.read()
    file.close()

    data = yaml.load(file_data, Loader=yaml.FullLoader)  # str转dict

    userData = data['userData']

    dataDict = []  # 存放用户数据（地区，qq）
    for key, value in userData.items():
        dict = {'province': value[0], 'city': value[1], 'qq': str(value[2])}
        dataDict.append(dict)

    for i in range(len(dataDict)):
        logger.info("---正在获取【{},{}】的天气！---".format(dataDict[i]['province'], dataDict[i]['city']))
        res = getWeather((dataDict[i]['province'], dataDict[i]['city']))  # 获取天气信息

        dataList = getInfo(res)  # 存放从api中获取的天气天气数据
        dataList.append(dataDict[i]['province'])
        dataList.append(dataDict[i]['city'])
        dataList.append(
            dataList[3].replace('xue', '❄').replace('lei', '⚡').replace('shachen', '🌪').replace('wu', '🌫').replace(
                'bingbao', '🌨').replace('yun', '☁').replace('yu', '🌧').replace('yin', '🌥').replace('qing', '☀'))
        time.sleep(2)

        # dataList.append(getYiyan())  # 一言
        # time.sleep(2)

        if 'g' in dataDict[i]['qq']:
            dataDict[i]['qq'] = dataDict[i]['qq'][1:]
            QQGroupPusher(dataDict[i]['qq'], dataList)
        else:
            QQPusher(dataDict[i]['qq'], dataList)
        logger.info("---天气推送成功！---")
        time.sleep(20)
