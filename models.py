import RNA
import random
import numpy as np
from hyperparams import *

chromosomes = []
new_chroms = []
scores = np.zeros(100000)
generation = 0

def makeCh(str_len):
    global  chromosomes
    APT_pool = "ACGU"
    seq = ""
    chromosomes = []
    # length - 10 , 10000 seq
    for i in range(100000):
        for j in range(str_len):
            seq += random.choice(APT_pool)
        chromosomes.append(seq)
        seq = ""

def evaluation():
    global chromosomes, scores
    scores = np.zeros(100000)

    for i in range(100000):
        seq = str(chromosomes[i])
        str_len = len(seq)
        (ss, mfe) = RNA.fold(seq)
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
        if base>=11 :
            #scores[i] += (base-11)
            #scores[i] += (base-11)/2.0
            scores[i] += 1

def selection():
    global chromosomes, scores, new_chroms
    new_chroms = []
    selected = 0
    max = np.max(scores)
    while(selected != 10000):
        for i in range(100000):
            if scores[i] == max and selected<10000:
                new_chroms.append(chromosomes[i])
                selected += 1
        max -= 1

def crossover():
    global new_chroms
    parent1 = new_chroms[:5000]
    parent2 = new_chroms[5000:]

    str_len = len(parent1[0])

    for i in range(5000):
        child1 = parent1[i][:int(str_len/2)] + parent2[i][int(str_len/2):]
        child2 = parent2[i][:int(str_len/2)] + parent1[i][int(str_len/2):]
        new_chroms.append(child1)
        new_chroms.append(child2)

def mutation():
    global new_chroms

    APT_pool = "ACGU"

    for i in range(4):
        chroms = new_chroms[:20000]
        str_len = len(chroms[0])
        for j in range(20000):
            for k in range(str_len):
                b = random.randint(0,3) # 25% mutaion
                if b==3 :
                    mutated = str(chroms[j][:k]) + str(random.choice(APT_pool)) + str(chroms[j][k+1:])
                    chroms[j] = mutated
        for j in range(20000):
            new_chroms.append(chroms[j])

def update():
    global chromosomes, new_chroms, generation

    chromosomes = new_chroms[:]
    generation += 1

def genetic(apt_len):
    global chromosomes
    makeCh(apt_len)
    print("Phase: " + str(apt_len))
    for i in range(30):
        evaluation()
        selection()
        crossover()
        mutation()
        update()

    print(len(chromosomes))

def main():
    global chromosomes
    """
    for i in range(10,15):
        apt_len = i
        genetic(apt_len)

        f = open(PAIRS_PATH["genetic"][apt_len], 'w')
        for j in range(len(chromosomes)):
            f.write(str(j) + ',' + chromosomes[j] + '\n')
        f.close()

    """
    for i in range(21,30):
        apt_len = i
        genetic(apt_len)
    
        f = open(PAIRS_PATH["genetic"][apt_len], 'w')
        for j in range(len(chromosomes)):
            f.write(str(j) + ',' + chromosomes[j] + '\n')
        f.close()

if __name__ == '__main__':
    main()