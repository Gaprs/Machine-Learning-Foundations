import pandas as pd
import numpy as np
import math
import urllib.request as request
import random



def getdata(dataX, dataY): #取得跟整理訓練資料集
    src = "https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_18_train.dat"
    with request.urlopen(src) as response:
        data = response.read() #讀取
        datalist = data.split() #將data轉換成list type
        dataXY = np.zeros((int(len(datalist)/5),5)) #建立一個 資料_data(list)的總數，重組成每列五個資料的陣列
        for i in range(int(len(datalist)/5)):       #該陣列為 [ [X1 X2 X3 X4 Y1]
                                                    #          [...............]]
            dataXY[i, 0] = datalist[5 * i]
            dataXY[i, 1] = datalist[5 * i +1]
            dataXY[i, 2] = datalist[5 * i +2]
            dataXY[i, 3] = datalist[5 * i +3]
            dataXY[i, 4] = datalist[5 * i +4]
        np.random.shuffle(dataXY) #將整個陣列每列隨機互換

        for i in range(int(len(dataXY))): #將隨機互換完的陣列拆分成 dataX, dataY
            dataX[i, 0] = 1
            dataX[i, 1] = dataXY[i, 0]
            dataX[i, 2] = dataXY[i, 1]
            dataX[i, 3] = dataXY[i, 2]
            dataX[i, 4] = dataXY[i, 3]
            dataY[i, 0] = dataXY[i, 4]

        return dataX, dataY

def getTestdata(TestdataX, TestdataY): #取得測試資料集, 邏輯同上
    src = "https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_18_test.dat"
    with request.urlopen(src) as response:
        data = response.read()
        datalist = data.split()
        dataXY = np.zeros((int(len(datalist)/5),5))
        for i in range(int(len(datalist)/5)):
            dataXY[i, 0] = datalist[5 * i]
            dataXY[i, 1] = datalist[5 * i +1]
            dataXY[i, 2] = datalist[5 * i +2]
            dataXY[i, 3] = datalist[5 * i +3]
            dataXY[i, 4] = datalist[5 * i +4]
        # np.random.shuffle(dataXY)

        for i in range(int(len(dataXY))):
            TestdataX[i, 0] = 1
            TestdataX[i, 1] = dataXY[i, 0]
            TestdataX[i, 2] = dataXY[i, 1]
            TestdataX[i, 3] = dataXY[i, 2]
            TestdataX[i, 4] = dataXY[i, 3]
            TestdataY[i, 0] = dataXY[i, 4]
        # print("dataX:", dataX)
        return TestdataX, TestdataY



def pocket():

    for i in range(trainTimes):
        perfect_W = np.zeros(5) #錯誤率最低的W向量
        test_W = np.zeros(5) #測試用W向量
        error_perfect = 0

        for train_times in range(50):
            flag = True
            getdata(dataX, dataY)
            error_test = 0
            for j in range((len(dataX))):#計算 w 在dataX中的錯誤次數

                if (np.dot(test_W, dataX[j]) * dataY[j]) <= 0:
                    # w += dataX[j] * dataY[j]
                    error_test += 1
                    flag = False
                    test_W += dataX[j] * dataY[j]
                    # print("trainTime:", i, "error_test:", error_test)
                    # print("test_W:", test_W)

            if flag == True:#在這次訓練中的w是完美的，因為在dataX中零錯誤
                perfect_W = test_W
                print("w:", test_W)
                print(np.dot(test_W, dataX[j]) * dataY[j])
                print("times:", times)
                break

            elif error_perfect > error_test or error_perfect == 0:
                # 第一次training的error_perfect應該為零 或 test_W的錯誤率比先前的perfect_W更低，因此更新為最佳W與紀錄錯誤次數
                error_perfect = error_test
                perfect_W = test_W
                print("times:", i, "update_error:", error_perfect)
                print("times:", i, "update_perfect_W:", perfect_W)


        for test_times in range(len(TestdataX)): #在重複2000次過程中，將每次訓練完50 or 100次的perfect_W套用在test data set中，並計算該W所造成的錯誤次數

            if (np.dot(perfect_W, TestdataX[test_times]) * TestdataY[test_times]) <= 0:
                error_set[i] += 1 #紀錄最佳W所造成的失誤次數
        w_set[i] = perfect_W #紀錄最佳W
        print("times:", i) #用來表示目前程式Run到第幾次
    print("error_set:", error_set) #執行完重複兩千次後，依序print各個最佳W的總錯誤次數
    print("w_set:", w_set) #執行完重複兩千次後，依序print各個最佳的W
    print("mean_error%:", np.mean(error_set)/len(TestdataX)) #用np.mean取錯誤次數的平均值並除以repeat times

def PLA():
    cycle = np.zeros(50)
    times = 0
    flag = True
    w = np.zeros(5)
    times = 0
    dataX = np.zeros((500, 5))
    dataY = np.zeros((500, 1))
    TestdataX = np.zeros((500, 5))
    TestdataY = np.zeros((500, 1))
    getdata(dataX, dataY)
    getTestdata(TestdataX, TestdataY)
    test_error = np.zeros(len(TestdataX))
    for i in range(50):


        CC = True

        flag = True
        for j in range((len(dataX))):
            print("j:", j)
            if (np.dot(w, dataX[j]) * dataY[j]) <= 0:
                w += dataX[j] * dataY[j]
                times += 1
                flag = False

        if flag == True:
            print("w:", w)
            print(np.dot(w, dataX[j]) * dataY[j])
            print("times:", times)
            CC = False
            break
    for test in range(len(TestdataX)):
        if (np.dot(w, TestdataX[test]) * TestdataY[test]) <= 0:
            test_error[test] += 1
    print("mean error by PLA:", np.mean(test_error))

    cycle[i] = times
    print(cycle)
    print(np.mean(cycle))
    print("i:", i)
    w = np.zeros(5)

trainTimes = 2000
error_set = np.zeros(trainTimes)
w_set = np.zeros((trainTimes,5))
times = 0
flag = True

dataX = np.zeros((500, 5))
dataY = np.zeros((500, 1))
TestdataX = np.zeros((500, 5))
TestdataY = np.zeros((500, 1))

getTestdata(TestdataX, TestdataY)
pocket()
