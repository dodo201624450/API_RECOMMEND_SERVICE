import pickle
from hyperparams import *
from random_APT import *
import numpy as np
import pandas as pd


def check(pdA: object, rand_apt) -> object:
    rst = np.where(pdA == 1)
    apt_list = ""
    X = []

    for i in rst:
        temp = rand_apt[i-1]
        apt_list = ""

        f = open(PAIRS_PATH["recommend"], 'w')

        for j in temp:
            tmp = np.array_str(j)
            tmp = tmp.split(" ")
            apt = ''.join(tmp[1])
            apt = apt.translate({ord(i): None for i in ']'})
            apt = apt.translate({ord(i): None for i in '\''})
            X.append(apt)
            f.write(str(j) + ',' + apt + '\n')
        f.close()

    return X

def recommend():
    RFC_A = pickle.load(open(PIC_PATH["mix_randomForests"], 'rb'))
    positive = -2

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

    return X
""""
for i in range(10):
    Train_A = np.load(NPZ_PATH["rand"][i])
    Train_P = np.load(NPZ_PATH["protein"])

    X_A = Train_A['XA']
    X_P = Train_P['XP']

    Train = np.concatenate((X_P, X_A), axis=-1)

    pdA = RFC_A.predict(Train)

    print("A {}".format(pdA))
for j in range(100):
    for i in range(100):
        print(str(pdA[j*100+1]), end=' ')
    print(" ")


"""

if __name__ == '__main__':
    recommend()