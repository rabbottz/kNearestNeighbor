'''
CPSC427
Team Member 1: Andrew Abbott
Submitted By: Andrew Abbott
GU Username: aabbott
File Name: kNN.py
Program asks user to enter how much time they have spent playing video games, number of frequent flyer miles, 
and how much ice cream they eat per year. Then the program classifies that person and determines if they will 
be liked based upon a training set of data baised on the kNN algorithm. 
To Execute: python prog3.py
Python Version 2.7.10
'''

from kNN import *

'''
pre: norm_data_matrix contains the normed data to be referenced, range_vals contains the range of acceptable values,
min_values contains the minnimum vlaues, labels_vecotrs contains the labes to be checked against.
Post: the reponse of whether or not the person will be liked.

'''
def classify_person(norm_data_matrix, range_vals, min_vals, labels_vector):
    labels = ['in large doses', 'in small doses', 'not at all']
    raw_labels = ['3', '2', '1']
    k = 3
    percent_video = float(raw_input("percentage of time spent playing video games " +
                                    "over the past year?\n"))
    freq_flier_miles = float(raw_input("Number of frequent flyer miles earned in " +
                                       "the past year?\n"))
    liters_ice_cream = float(raw_input("Number of liters of ice cream eaten in " +
                                "the past year?\n"))
    in_pt = array([freq_flier_miles, percent_video, liters_ice_cream])
    in_pt_norm = normalize_point(in_pt, min_vals, range_vals)
    
    result = classify(in_pt_norm, norm_data_matrix, labels_vector, k)
    for i in range(3):
        if result == raw_labels[i]:
            potential = labels[i]
            break            
    print ("You will probably like this person: " + potential)


def main():
    data_matrix, labels_vector = file2matrix("datingTestSet2.txt")
    norm_data_matrix, range_vals, min_vals = normalize(data_matrix)
    classify_person(norm_data_matrix, range_vals, min_vals, labels_vector)
    
main()
