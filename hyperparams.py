#!/usr/bin/python3
BASE_PATH = "data/"
SEQ_PATH = BASE_PATH + "sequence/"
STR_PATH = BASE_PATH + "structure/"
CLF_PATH = "clf/"
NPZ_PATH = {
    "NPInter" : "npz/NPInter.npz",
    "RPI" : {
        1807 : "npz/RPI1807.npz",
        2241 : "npz/RPI2241.npz",
        369  : "npz/RPI369.npz",
        488  : "npz/RPI488.npz"
    },
    "API" : {
        "A_train"   : "npz/API_A_train.npz",
        "B_train"   : "npz/API_B_train.npz",
        "A_test"    : "npz/API_A_test.npz",
        "B_test"    : "npz/API_B_test.npz"
    },
    "rand"  : {
        0   : "npz/random_apt0.npz",
        1   : "npz/random_apt1.npz",
        2   : "npz/random_apt2.npz",
        3   : "npz/random_apt3.npz",
        4   : "npz/random_apt4.npz",
        5   : "npz/random_apt5.npz",
        6   : "npz/random_apt6.npz",
        7   : "npz/random_apt7.npz",
        8   : "npz/random_apt8.npz",
        9   : "npz/random_apt9.npz"
    },
    "genetic"   : {
        0   : "npz/genetic_apt0.npz",
        1   : "npz/genetic_apt1.npz",
        2   : "npz/genetic_apt2.npz",
        3   : "npz/genetic_apt3.npz",
        4   : "npz/genetic_apt4.npz",
        5   : "npz/genetic_apt5.npz",
        6   : "npz/genetic_apt6.npz",
        7   : "npz/genetic_apt7.npz",
        8   : "npz/genetic_apt8.npz",
        9   : "npz/genetic_apt9.npz",
        10   : "npz/genetic_apt10.npz",
        11   : "npz/genetic_apt11.npz",
        12   : "npz/genetic_apt12.npz",
        13   : "npz/genetic_apt13.npz",
        14   : "npz/genetic_apt14.npz",
        15   : "npz/genetic_apt15.npz",
        16   : "npz/genetic_apt16.npz",
        17   : "npz/genetic_apt17.npz",
        18   : "npz/genetic_apt18.npz",
        19   : "npz/genetic_apt19.npz",
        20   : "npz/genetic_apt20.npz",
        21   : "npz/genetic_apt21.npz",
        22   : "npz/genetic_apt22.npz",
        23   : "npz/genetic_apt23.npz",
        24   : "npz/genetic_apt24.npz",
        25   : "npz/genetic_apt25.npz",
        26   : "npz/genetic_apt26.npz",
        27   : "npz/genetic_apt27.npz",
        28   : "npz/genetic_apt28.npz",
        29   : "npz/genetic_apt29.npz"
    },
    "protein" : "npz/protein.npz",
    "mix"   : "npz/mix.npz"
}

PAIRS_PATH = {
    "recommend" : BASE_PATH + "recommend.csv",
    "NPInter" : BASE_PATH + "NPInter_pairs.txt",
    "RPI" : {
        1807 : BASE_PATH + "RPI1807_pairs.txt",
        2241 : BASE_PATH + "RPI2241_pairs.txt",
        369  : BASE_PATH + "RPI369_pairs.txt",
        488  : BASE_PATH + "RPI488_pairs.txt"
    },
    "API" : {
        "A_train"   : BASE_PATH + "benchmark_A_train_sequences.csv",
        "B_train"   : BASE_PATH + "benchmark_B_train_sequences.csv",
        "A_test"    : BASE_PATH + "benchmark_A_test_sequences.csv",
        "B_test"    : BASE_PATH + "benchmark_B_test_sequences.csv"
    },
    "rand"  : {
        0   : BASE_PATH + "random_apt0.csv",
        1   : BASE_PATH + "random_apt1.csv",
        2   : BASE_PATH + "random_apt2.csv",
        3   : BASE_PATH + "random_apt3.csv",
        4   : BASE_PATH + "random_apt4.csv",
        5   : BASE_PATH + "random_apt5.csv",
        6   : BASE_PATH + "random_apt6.csv",
        7   : BASE_PATH + "random_apt7.csv",
        8   : BASE_PATH + "random_apt8.csv",
        9   : BASE_PATH + "random_apt9.csv"
    },
    "genetic"   : {
        0   : BASE_PATH + "genetic_apt0.csv",
        1   : BASE_PATH + "genetic_apt1.csv",
        2   : BASE_PATH + "genetic_apt2.csv",
        3   : BASE_PATH + "genetic_apt3.csv",
        4   : BASE_PATH + "genetic_apt4.csv",
        5   : BASE_PATH + "genetic_apt5.csv",
        6   : BASE_PATH + "genetic_apt6.csv",
        7   : BASE_PATH + "genetic_apt7.csv",
        8   : BASE_PATH + "genetic_apt8.csv",
        9   : BASE_PATH + "genetic_apt9.csv",
        10   : BASE_PATH + "genetic_apt10.csv",
        11   : BASE_PATH + "genetic_apt11.csv",
        12   : BASE_PATH + "genetic_apt12.csv",
        13   : BASE_PATH + "genetic_apt13.csv",
        14   : BASE_PATH + "genetic_apt14.csv",
        15   : BASE_PATH + "genetic_apt15.csv",
        16   : BASE_PATH + "genetic_apt16.csv",
        17   : BASE_PATH + "genetic_apt17.csv",
        18   : BASE_PATH + "genetic_apt18.csv",
        19   : BASE_PATH + "genetic_apt19.csv",
        20   : BASE_PATH + "genetic_apt20.csv",
        21   : BASE_PATH + "genetic_apt21.csv",
        22   : BASE_PATH + "genetic_apt22.csv",
        23   : BASE_PATH + "genetic_apt23.csv",
        24   : BASE_PATH + "genetic_apt24.csv",
        25   : BASE_PATH + "genetic_apt25.csv",
        26   : BASE_PATH + "genetic_apt26.csv",
        27   : BASE_PATH + "genetic_apt27.csv",
        28   : BASE_PATH + "genetic_apt28.csv",
        29   : BASE_PATH + "genetic_apt29.csv"
    }
}

SEQ_PATH = {
    "NPInter" : {
        "RNA"     : SEQ_PATH + "NPinter_rna_seq.fa",
        "Protein" : SEQ_PATH + "NPinter_protein_seq.fa"
    },
    "RPI" : {
        1807 : {
            "RNA"     : SEQ_PATH + "RPI1807_rna_seq.fa",
            "Protein" : SEQ_PATH + "RPI1807_protein_seq.fa"
        },
        2241 : {
            "RNA"     : SEQ_PATH + "RPI2241_rna_seq.fa",
            "Protein" : SEQ_PATH + "RPI2241_protein_seq.fa"
        },
        369  : {
            "RNA"     : SEQ_PATH + "RPI369_rna_seq.fa",
            "Protein" : SEQ_PATH + "RPI369_protein_seq.fa"
        },
        488  : {
            "RNA"     : SEQ_PATH + "RPI488_rna_seq.fa",
            "Protein" : SEQ_PATH + "RPI488_protein_seq.fa"
        }
    }
}

PIC_PATH = {
    "randomForests": {
        "A": CLF_PATH + "randomForests_A.pickle",
        "B": CLF_PATH + "randomForests_B.pickle"
    },
    "mix_randomForests": CLF_PATH + "mix_randomForests.pickle"
    ,
    "svm": {
        "A": CLF_PATH + "svm_A.pickle",
        "B": CLF_PATH + "svm_B.pickle"
    },
    "NaiveBayesClassifier": {
        "A": CLF_PATH + "NaiveBayesClassifier_A.pickle",
        "B": CLF_PATH + "NaiveBayesClassifier_B.pickle"
    },
    "BaggingLinearsvmClassifier": {
        "A": CLF_PATH + "BaggingLinearsvmClassifier_A.pickle",
        "B": CLF_PATH + "BaggingLinearsvmClassifier_B.pickle"
    },
    "BaggingKNeighborsClassifier": {
        "A": CLF_PATH + "BaggingKNeighborsClassifier_A.pickle",
        "B": CLF_PATH + "BaggingKNeighborsClassifier_B.pickle"
    },
    "GradientBoost": {
        "A": CLF_PATH + "GradientBoost_A.pickle",
        "B": CLF_PATH + "GradientBoost_B.pickle"
    },
    "BaggingRandomForestClassifier": {
        "A": CLF_PATH + "BaggingRandomForestClassifier_A.pickle",
        "B": CLF_PATH + "BaggingRandomForestClassifier_B.pickle"
    },
    "Voting": {
        "A": CLF_PATH + "Voting_A.pickle",
        "B": CLF_PATH + "Voting_B.pickle"
    }
}