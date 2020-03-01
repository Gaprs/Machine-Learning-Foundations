import pandas as pd
import numpy as np
import math
import urllib.request as request
import random


def getdata(dataX, dataY):
    src = "https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_15_train.dat"
    with request.urlopen(src) as response:
        data = response.read()
        datalist = data.split()
        dataSet = np.zeros((int(len(datalist)/5),5))
        dataXY = np.zeros((int(len(datalist)/5),5))
        for i in range(int(len(datalist)/5)):
            dataXY[i, 0] = datalist[5 * i]
            dataXY[i, 1] = datalist[5 * i +1]
            dataXY[i, 2] = datalist[5 * i +2]
            dataXY[i, 3] = datalist[5 * i +3]
            dataXY[i, 4] = datalist[5 * i +4]
        np.random.shuffle(dataXY)

        for i in range(int(len(dataXY))):
            dataX[i, 0] = 1
            dataX[i, 1] = dataXY[i, 0]
            dataX[i, 2] = dataXY[i, 1]
            dataX[i, 3] = dataXY[i, 2]
            dataX[i, 4] = dataXY[i, 3]
            dataY[i, 0] = dataXY[i, 4]
        print("dataX:", dataX)
        return dataX
        return dataY

cycle = np.zeros(2000)
times = 0
flag = True

for i in range(2000):
    w = np.zeros(5)
    times = 0
    dataX = np.zeros((400, 5))
    dataY = np.zeros((400, 1))
    getdata(dataX, dataY)

    CC = True

    while CC:
        flag = True
        for j in range((len(dataX))):

            if (np.dot(w, dataX[j]) * dataY[j]) <= 0:
                w += dataX[j] * dataY[j] *0.5
                times += 1
                flag = False

        if flag == True:
            print("w:", w)
            print(np.dot(w, dataX[j]) * dataY[j])
            print("times:", times)
            CC = False
            break
    cycle[i] = times
    print(cycle)
    print(np.mean(cycle))
    print("i:", i)
    w = np.zeros(5)




    # for i in range(2000):
    #     w = np.zeros(5)
    #     times = 0
    #     # np.random.shuffle(dataX)
    #     # for j in range(int(len(datalist)/5)):
    #     #     dataX[j] = np.random.shuffle(dataX[j])
    #     CC = True
    #     while CC:
    #         flag = True
    #         for j in range(len(dataX)):
    #             if (np.dot(w, dataX[j]) * dataY[j]) <= 0:
    #                 # print(np.dot(w, dataX[j]), dataY[j])
    #                 # print("w1:", w)
    #                 w += dataX[j] * dataY[j]
    #                 # print("w2:", w)
    #                 times += 1
    #                 flag = False
    #                 # print("flag:", flag, "w:", w)
    #         if flag == True:
    #             # cycle[i] = times
    #             # print("times:", i)
    #             print("w:", w)
    #             print(np.dot(w, dataX[j]) * dataY[j])
    #             print("times:", times)
    #             CC = False
    #             break
    #     cycle[i] = times
    #     print(np.mean(cycle))

