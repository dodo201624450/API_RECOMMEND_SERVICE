import random
from hyperparams import *
import RNA

APT_pool = "ACGU"
imsi = []
result = ""
results = []
length=27
def Number1(ss):
    if ss[0] == ".":
        if ss[1] == "(" and ss[2] == "(" and ss[3] == "(":
            if ss[-1] == "." and ss[-2] == ")" and ss[-3] == ")" and ss[-4] == ")":
                return 0
            if ss[-1] == ")" and ss[-2] == ")" and ss[-3] == ")":
                return 0
            else:
                return 1
    if ss[0] == "(":
        if ss[1] == "(" and ss[2] == "(":
            if ss[-1] == "." and ss[-2] == ")" and ss[-3] == ")" and ss[-4] == ")":
                return 0
            if ss[-1] == ")" and ss[-2] == ")" and ss[-3] == ")":
                return 0
            else:
                return 1
    else:
        return 1
def Number2(mfe):
    if mfe<=-5.7:
        return 0
    else:
        return 1
def Number3(ss):
    num3=0
    for i in range(length):
        if ss[i]==".":
            num3+=1
    return num3


while len(imsi)<10000:
    for i in range(length):
        result += random.choice(APT_pool)
    (ss, mfe) = RNA.fold(result)
    if Number1(ss)==0 and Number2(mfe)==0 and Number3(ss)>=11:
        imsi.append((result, mfe))
    result = ""

imsi = sorted(imsi, key=lambda imsi : imsi[1])
for i in range(1000):
    results.append(imsi[i][0])

for i in range(10):
    f = open(PAIRS_PATH["rand"][i], 'w')
    for j in range(1000):
        f.write(str(j) + ',' + results[j] + '\n')
    f.close()

