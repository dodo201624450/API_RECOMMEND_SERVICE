import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from hyperparams import *

def testset_set():
    A_test = np.load('npz/API_A_test.npz')
    A_T_XP = A_test['XP']
    A_T_XA = A_test['XR']
    A_T_Y = A_test['Y']
    B_test = np.load('npz/API_B_test.npz')
    B_T_XP = B_test['XP']
    B_T_XA = B_test['XR']
    B_T_Y = B_test['Y']
    A_T_XP = np.array(A_T_XP)
    A_T_XA = np.array(A_T_XA)
    B_T_XP = np.array(B_T_XP)
    B_T_XA = np.array(B_T_XA)
    A_X_test = np.concatenate((A_T_XP, A_T_XA), axis=-1)
    A_Y_test = np.array(A_T_Y)
    B_X_test = np.concatenate((B_T_XP, B_T_XA), axis=-1)
    B_Y_test = np.array(B_T_Y)
    return A_X_test, A_Y_test, B_X_test, B_Y_test

def testset_mix():
    A_test = np.load('npz/API_A_test.npz')
    A_T_XP = A_test['XP']
    A_T_XA = A_test['XR']
    A_T_Y = A_test['Y']
    B_test = np.load('npz/API_B_test.npz')
    B_T_XP = B_test['XP']
    B_T_XA = B_test['XR']
    B_T_Y = B_test['Y']
    A_T_XP = np.array(A_T_XP)
    A_T_XA = np.array(A_T_XA)
    B_T_XP = np.array(B_T_XP)
    B_T_XA = np.array(B_T_XA)
    XP = np.append(A_T_XP,B_T_XP,axis=0)
    XA = np.append(A_T_XA,B_T_XA,axis=0)
    MIX_Y = np.append(A_T_Y, B_T_Y, axis=0)
    MIX_X = np.concatenate((XP,XA), axis=-1)

    return MIX_X,MIX_Y

def trainset_set():
    A_train = np.load('npz/API_A_train.npz')
    B_train = np.load('npz/API_B_train.npz')
    A_XP = A_train['XP']
    A_XA = A_train['XR']
    A_Y = A_train['Y']
    B_XP = B_train['XP']
    B_XA = B_train['XR']
    B_Y = B_train['Y']
    A_XP = np.array(A_XP)
    A_XA = np.array(A_XA)
    B_XP = np.array(B_XP)
    B_XA = np.array(B_XA)
    A_X_train = np.concatenate((A_XP, A_XA), axis=-1)
    A_Y_train = np.array(A_Y)
    B_X_train = np.concatenate((B_XP, B_XA), axis=-1)
    B_Y_train = np.array(B_Y)
    return A_X_train, A_Y_train, B_X_train, B_Y_train

def trainset_mix():
    A_train = np.load('npz/API_A_train.npz')
    B_train = np.load('npz/API_B_train.npz')
    A_XP = A_train['XP']
    A_XA = A_train['XR']
    A_Y = A_train['Y']
    B_XP = B_train['XP']
    B_XA = B_train['XR']
    B_Y = B_train['Y']
    A_XP = np.array(A_XP)
    A_XA = np.array(A_XA)
    B_XP = np.array(B_XP)
    B_XA = np.array(B_XA)
    A_Y = np.array(A_Y)
    B_Y = np.array(B_Y)
    XP = np.append(A_XP, B_XP, axis=0)
    XA = np.append(A_XA, B_XA, axis=0)
    MIX_Y = np.append(A_Y, B_Y, axis=0)
    MIX_X = np.concatenate((XP, XA), axis=-1)
    return MIX_X,MIX_Y

def learning(func):
    A_X_train, A_Y_train, B_X_train, B_Y_train = trainset_set()

    A_clf, B_clf = func(A_X_train, A_Y_train, B_X_train, B_Y_train)

    A_X_test, A_Y_test, B_X_test, B_Y_test = testset_set()

    AA_scores = cross_val_score(A_clf, A_X_test, A_Y_test, cv=10)
    AB_scores = cross_val_score(A_clf, B_X_test, B_Y_test, cv=10)
    BB_scores = cross_val_score(B_clf, B_X_test, B_Y_test, cv=10)
    BA_scores = cross_val_score(B_clf, A_X_test, A_Y_test, cv=10)

    print("AA: {}".format(AA_scores))
    print("AB: {}".format(AB_scores))
    print("BB: {}".format(BB_scores))
    print("BA: {}".format(BA_scores))
    print("mean AA: {}, AB: {}, BB: {}, BA: {}".format(np.mean(AA_scores), np.mean(AB_scores),np.mean(BB_scores),np.mean(BA_scores)))

    saveClf(func,A_clf,B_clf)

def learning_mix(func):
    X_train, Y_train = trainset_mix()
    X_test, Y_test = testset_mix()
    A_clf = func(X_train, Y_train)

    AA_scores = cross_val_score(A_clf, X_test, Y_test, cv=10)

    print("AA: {}".format(AA_scores))
    print("mean AA: {}".format(np.mean(AA_scores)))

    mix_saveClf(func,A_clf)

def saveClf(func, A_clf, B_clf):
    label = func.__name__
    filename_A = PIC_PATH[label]["A"]
    filename_B = PIC_PATH[label]["B"]
    pickle.dump(A_clf, open(filename_A, 'wb'))
    pickle.dump(B_clf, open(filename_B, 'wb'))

def mix_saveClf(func, A_clf):
    label = func.__name__
    filename_A = PIC_PATH[label]
    pickle.dump(A_clf, open(filename_A, 'wb'))

def svm(A_X_train, A_Y_train, B_X_train, B_Y_train):
    A_clf = SVC()
    A_clf.fit(A_X_train, A_Y_train)

    B_clf = SVC()
    B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def randomForests(A_X_train, A_Y_train, B_X_train, B_Y_train):
    A_clf = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=None, min_samples_split=2, random_state=0)
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=None, min_samples_split=2, random_state=0)
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def mix_randomForests(MIX_X, MIX_Y):
    A_clf = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=None, min_samples_split=2, random_state=0)
    A_clf = A_clf.fit(MIX_X, MIX_Y)

    return A_clf

def NaiveBayesClassifier(A_X_train, A_Y_train, B_X_train, B_Y_train):
    A_clf = GaussianNB()
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = GaussianNB()
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def GradientBoost(A_X_train, A_Y_train, B_X_train, B_Y_train):
    A_clf = GradientBoostingClassifier(random_state=0)
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = GradientBoostingClassifier(random_state=0)
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def BaggingLinearsvmClassifier(A_X_train, A_Y_train, B_X_train, B_Y_train):
    estimator = LinearSVC()
    A_clf = BaggingClassifier(base_estimator=estimator, n_estimators=100, max_samples=1./10, n_jobs=1)
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = BaggingClassifier(base_estimator=estimator, n_estimators=100, max_samples=1./10, n_jobs=1)
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def BaggingKNeighborsClassifier(A_X_train, A_Y_train, B_X_train, B_Y_train):
    estimator = KNeighborsClassifier(n_neighbors=5)
    A_clf = BaggingClassifier(base_estimator=estimator, n_estimators=100, max_samples=1./10, n_jobs=1)
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = BaggingClassifier(base_estimator=estimator, n_estimators=100, max_samples=1./10, n_jobs=1)
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def BaggingRandomForestClassifier(A_X_train, A_Y_train, B_X_train, B_Y_train):
    estimator = RandomForestClassifier(n_estimators=100, criterion="entropy")
    A_clf = BaggingClassifier(base_estimator=estimator, n_estimators=100, max_samples=1./10, n_jobs=1)
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = BaggingClassifier(base_estimator=estimator, n_estimators=100, max_samples=1./10, n_jobs=1)
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def Voting(A_X_train, A_Y_train, B_X_train, B_Y_train):
    estimator_1 = LinearSVC()
    estimator_2 = KNeighborsClassifier()

    SVM = SVC()
    RFC = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=None, min_samples_split=2, random_state=0)
    NBC = GaussianNB()
    GBC = GradientBoostingClassifier(random_state=0)
    BLS = BaggingClassifier(base_estimator=estimator_1, n_estimators=100, max_samples=1./10, n_jobs=1)
    BKN = BaggingClassifier(base_estimator=estimator_2, n_estimators=100, max_samples=1./10, n_jobs=1)

    A_clf = VotingClassifier(estimators=[('svm', SVM), ('rfc', RFC), ('nbc', NBC), ('gbc', GBC), ('bls', BLS), ('bkn', BKN)], voting='hard', weights=[0.75, 0.74, 0.42, 0.68, 0.75, 0.75])
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = VotingClassifier(estimators=[('svm', SVM), ('rfc', RFC), ('nbc', NBC), ('gbc', GBC), ('bls', BLS), ('bkn', BKN)], voting='hard', weights=[0.78, 0.91, 0.69, 0.83, 0.70, 0.53])
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

if __name__ == "__main__":
    """"""
    print("Random Forest Classification")
    learning(randomForests)
    print("SVM")
    learning(svm)
    print("Naive Bayes Classification")
    learning(NaiveBayesClassifier)
    print("Bagging Linear svm Classification")
    learning(BaggingLinearsvmClassifier)
    print("Bagging KNeighbors Classifier")
    learning(BaggingKNeighborsClassifier)
    print("Gradient Boosting Classification")
    learning(GradientBoost)
    print("BaggingRandomForestClassifier")
    learning(BaggingRandomForestClassifier)
    print("Voting")
    learning(Voting)
    """"""
    print("mix_randomForests")
    learning_mix(mix_randomForests)