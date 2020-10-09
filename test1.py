import os
import time
import cv2 as cv
import numpy as np
import serial

import json

configMsg = []


def readConf(configPath="config.json"):
    r""" 读取配置文件
        configPath 文件绝对路径
     """
    data = []
    with open("config.json", "r")as f:
        data = json.load(f)

    configMsg = data


def saveConf(configPath="config.json"):
    r""" 保存配置文件
        手动重置配置文件，调试用
    """
    data = {
        "isDbg": True,
        "isLockEs": False,
        "confFileName": configPath,

    }
    # data = json.loads(str(data).encode("utf8"))
    with open(configPath, 'w') as f:
        json.dump(data,f)


# infor
def infoWriter(obj, pos, width, height):
    r""" detector获取信息后写入 """
    with open('obRec') as f:
        msg = str(time.asctime()) + ' ' + obj + ' ' + pos + '\n'

        f.write(msg)


if __name__ == "__main__":

    saveConf()
    readConf()
    pass
