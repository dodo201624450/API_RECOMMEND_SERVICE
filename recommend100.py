import RNA
import pickle
from hyperparams import *
from random_APT import *
import numpy as np
import pandas as pd

imsi = []
results = []

RFC_A = pickle.load(open(PIC_PATH["mix_randomForests"], 'rb'))
positive = 0

def check(pdA: object, rand_apt) -> object:
    rst = np.where(pdA == 1)
    apt_list = ""
    X = []

    for i in rst:
        temp = rand_apt[i-1]
        apt_list = ""
        for j in temp:
            tmp = np.array_str(j)
            tmp = tmp.split(" ")
            apt = ''.join(tmp[1])
            apt = apt.translate({ord(i): None for i in ']'})
            apt = apt.translate({ord(i): None for i in '\''})
            X.append(apt)

    return X


for i in range(10):
    Train_A = np.load(NPZ_PATH["genetic"][i+10])
    Train_P = np.load(NPZ_PATH["protein"])
    rand_apt = pd.read_csv(PAIRS_PATH["genetic"][i+10])
    rand_apt_arr = rand_apt.to_numpy()

    X_A = Train_A['XA']
    X_P = Train_P['XP']

    Train = np.concatenate((X_P, X_A), axis=-1)

    pdA = RFC_A.predict(Train)

    X = check(pdA, rand_apt_arr)
    print(X)
    positive += len(X)
    #print("A {}".format(pdA))

print(positive)

def recommend100(imsi):
    rand_apt = pd.read_csv(PAIRS_PATH["genetic"][11])
    rand_apt_arr = rand_apt.to_numpy()
    scores = np.zeros(len(rand_apt_arr))
    for i in range(len(rand_apt_arr)):
        str_len = len(rand_apt_arr[i][1])
        (ss, mfe) = RNA.fold(rand_apt_arr[i][1])
        # cond#1 3 consecutive base pairs
        if ss[0] == ".":
            if ss[1] == "(" and ss[2] == "(" and ss[3] == "(":
                if ss[-1] == "." and ss[-2] == ")" and ss[-3] == ")" and ss[-4] == ")":
                    scores[i] += 1
                if ss[-1] == ")" and ss[-2] == ")" and ss[-3] == ")":
                    scores[i] += 1
        if ss[0] == "(":
            if ss[1] == "(" and ss[2] == "(":
                if ss[-1] == "." and ss[-2] == ")" and ss[-3] == ")" and ss[-4] == ")":
                    scores[i] += 1
                if ss[-1] == ")" and ss[-2] == ")" and ss[-3] == ")":
                    scores[i] += 1

        # cond#2 free Energy <= -5.7
        if mfe <= -5.7:
            scores[i] += 1

        # cond#3 11 unpaired base
        for i in range(str_len):
            base = 0
            if ss[i] == ".":
                base += 1
        if base >= 11:
            scores[i] += 1


    for i in range(len(rand_apt_arr)):
        imsi.append((rand_apt_arr[i][1], scores[i]))
    imsi = sorted(imsi, key=lambda imsi : imsi[1], reverse=True)

    for i in range(100):
        results.append(imsi[i][0])
    print(results)



if __name__ == '__main__':
    recommend100(imsi)