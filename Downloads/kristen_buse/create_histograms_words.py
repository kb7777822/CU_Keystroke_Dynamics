#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:30:35 2020

@author: kb7777822
"""
import matplotlib.pyplot as plt
#import numpy as np
import os

dict_path = '/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/'
BINS = [0,25,50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525,550,575,600,625,650,675,700,725,750,775,800]
#np.arange(0,800,step=25) #histogram bins





while True:
    graph_type = input("Enter the type of graph (m, dd, uu, ud, or du): ")
    if not (graph_type == 'm' or graph_type == 'dd' or graph_type == 'uu' or graph_type == 'ud' or graph_type == 'du'):
        print('Enter a graph type correctly')
        continue
    user = input("Enter the participant # you'd look at the graphs of, or 'all' to look at all participants: ")
    if user == 'all':
        with open(dict_path + graph_type + '_dict_all.txt', 'r') as dict_file: 
            dict = eval(dict_file.readline())
            
            #get the 20 graphs with the largest representation
            max_graphs = ('',0)
            min_max_graphs = ('',100000000)
            biggest_graphs = []
            for letters in dict:
                
                if len(letters) == 3:

                    number_of_graphs = 0
                    for word in dict[letters]:
                        number_of_graphs += len(dict[letters][word])
                        
                    if len(biggest_graphs) < 20:
                        biggest_graphs += [(letters,number_of_graphs)]
                        if number_of_graphs > max_graphs[1]:
                            max_graphs = (letters,number_of_graphs)
                        if number_of_graphs < min_max_graphs[1]:
                            min_max_graphs = (letters,number_of_graphs)
                    else:
                        if number_of_graphs > max_graphs[1]:                                                
                            biggest_graphs.remove(min_max_graphs)
                            biggest_graphs+=[(letters,number_of_graphs)]
                            max_graphs = (letters,number_of_graphs)
                        elif number_of_graphs > min_max_graphs[1]:
                            biggest_graphs.remove(min_max_graphs)
                            biggest_graphs+=[(letters,number_of_graphs)]
                        min_max_graphs_inner = max_graphs
                            
                        for im_tired in biggest_graphs:
                            if im_tired[1] < min_max_graphs_inner[1]:
                                min_max_graphs_inner = im_tired
                        min_max_graphs = min_max_graphs_inner
                
            second = lambda x : x[1]
            biggest_graphs.sort(key=second,reverse=True)
            
                
                
            while True:
                
                print("The 20 largest graphs are: ")
                
                for letters in biggest_graphs:
                    print(letters[0]+ ' ' + str(letters[1]))
                
                
                letters = input("Enter the specific graph you want to look at (capital letters, \
                                digraph letters separated by a /), \n or 'exit' to stop looking at " + \
                        graph_type + " for all users: ")
                if letters == 'exit':
                    break

                if dict.get(letters) == None:
                    print('Enter a real graph next time :(')
                    continue
                 
                #get the 20 words with the largest representation for the graph
                max_word = ('',0)
                min_max_word = ('',100000000)
                biggest_words = []
                for word in dict[letters]:
                    
                    number_of_words = 0
                    
                    number_of_words += len(dict[letters][word])
                    
                    if len(biggest_words) < 20:
                        biggest_words += [(word,number_of_words)]
                        if number_of_words > max_word[1]:
                            max_word = (letters,number_of_words)
                        if number_of_words < min_max_word[1]:
                            min_max_word = (word,number_of_words)
                    else:
                        if number_of_words > max_word[1]:
                            biggest_words.remove(min_max_word)
                            biggest_words+=[(word,number_of_words)]
                            max_graphs = (word,number_of_graphs)
                        elif number_of_words > min_max_word[1]:
                            biggest_words.remove(min_max_word)
                            biggest_words+=[(word,number_of_words)]
                        min_max_word_inner = max_word
                        
                        for im_tired_words in biggest_words:
                            if im_tired_words[1] < min_max_word_inner[1]:
                                min_max_word_inner = im_tired_words
                        min_max_word = min_max_word_inner
                
                            
                biggest_words.sort(key=second,reverse=True)
                for word in biggest_words:
                    print(word[0]+ ' ' + str(word[1]))
                
                words = input("Enter the words you'd like to look at, separated by a space (all caps please), or enter '+' to look at all words: ")
                histogram_input = []
                if words == '+':
                    for word in dict[letters]:
                        histogram_input += dict[letters][word]
                        
                else:
                    for word in words.split():
                        if dict[letters].get(word) == None:
                            print("Sorry, the word " + word + " doesn't exist for the " + letters + " " + graph_type  + " graph")
                            continue
                        histogram_input += dict[letters][word]
    
                histogram_input = [x / 10000 for x in histogram_input] #tbh data should probably be changed so we don't have to do this.
                #anyway, that line converted the times to ms
                
                #make histogram
                plt.figure()
                plt.hist(histogram_input,bins=BINS,color='blue')
                plt.title(graph_type + ' ' + letters + ' ' + ' in the words: ' + words + ' for all users')
                plt.xlabel('miliseconds', size='14')
                plt.ylabel('Occurences', size='14')
                plt.show()
    else:
        file_name = dict_path + graph_type + '/' + graph_type + '_dict_' + user + '.txt'
        if not os.path.isfile(file_name):
            print("That wasn't a realy participant #, sorry!")
            continue
        with open(file_name) as dict_file:
            dict = eval(dict_file.readline())
            
            #get the 20 graphs with the largest representation
            max_graphs = ('',0)
            min_max_graphs = ('',100000000)
            biggest_graphs = []
            for letters in dict:
                
                if len(letters) == 3:
                
                    number_of_graphs = 0
                    for word in dict[letters]:
                        number_of_graphs += len(dict[letters][word])
                    
                    if len(biggest_graphs) < 20:
                        biggest_graphs += [(letters,number_of_graphs)]
                        if number_of_graphs > max_graphs[1]:
                            max_graphs = (letters,number_of_graphs)
                        if number_of_graphs < min_max_graphs[1]:
                            min_max_graphs = (letters,number_of_graphs)
                    else:
                        if number_of_graphs > max_graphs[1]:                                                
                            biggest_graphs.remove(min_max_graphs)
                            biggest_graphs+=[(letters,number_of_graphs)]
                            max_graphs = (letters,number_of_graphs)
                        elif number_of_graphs > min_max_graphs[1]:
                            biggest_graphs.remove(min_max_graphs)
                            biggest_graphs+=[(letters,number_of_graphs)]
                        min_max_graphs_inner = max_graphs
                        
                        for im_tired in biggest_graphs:
                            if im_tired[1] < min_max_graphs_inner[1]:
                                min_max_graphs_inner = im_tired
                        min_max_graphs = min_max_graphs_inner
            
            second = lambda x : x[1]
            biggest_graphs.sort(key=second,reverse=True)
            
            
            while True:
                print("The 20 largest graphs are: ")
                
                for letters in biggest_graphs:
                    print(letters[0]+ ' ' + str(letters[1]))
                
                
                letters = input("Enter the specific graph you want to look at (capital letters, \
                                digraph letters separated by a /), \n or 'exit' to stop looking at " + \
                                graph_type + " for user " + user + ": ")
                if letters == 'exit':
                    break
                
                
                
                if dict.get(letters) == None:
                    print('Enter a real graph next time :(')
                    continue
                
                #get the 20 words with the largest representation
                max_word = ('',0)
                min_max_word = ('',100000000)
                biggest_words = []
                for word in dict[letters]:
                    
                    number_of_words = 0
                    
                    number_of_words += len(dict[letters][word])
                    
                    
                    if len(biggest_words) < 40:
                        biggest_words += [(word,number_of_words)]
                        if number_of_words > max_word[1]:
                            max_word = (letters,number_of_words)
                        if number_of_words < min_max_word[1]:
                            min_max_word = (word,number_of_words)
                    else:
                        if number_of_words > max_word[1]:                                                
                            biggest_words.remove(min_max_word)
                            biggest_words+=[(word,number_of_words)]
                            max_graphs = (word,number_of_graphs)
                        elif number_of_words > min_max_word[1]:
                            biggest_words.remove(min_max_word)
                            biggest_words+=[(word,number_of_words)]
                        min_max_word_inner = max_word
                        
                        for im_tired_words in biggest_words:
                            if im_tired_words[1] < min_max_word_inner[1]:
                                min_max_word_inner = im_tired_words
                        min_max_word = min_max_word_inner
                
                            
                biggest_words.sort(key=second,reverse=True)
                for word in biggest_words:
                    print(word[0]+ ' ' + str(word[1]))
                
                words = input("Enter the words you'd like to look at, separated by a space (all caps please), or enter '+' to look at all words: ")
                histogram_input = []
                if words == '+':
                    for word in dict[letters]:
                        histogram_input += dict[letters][word]
                else:
                    for word in words.split():
                        if dict[letters].get(word) == None:
                            print("Sorry, the word " + word + " doesn't exist for the " + letters + " " + graph_type  + " graph")
                            continue
                        histogram_input += dict[letters][word]

                histogram_input = [x / 10000 for x in histogram_input] 
        
                #make histogram
                plt.figure()
                plt.hist(histogram_input,color='blue',bins=BINS)
                plt.title(graph_type + ' ' + letters + ' ' + ' in the words: ' + words + ' for user ' + user)
                plt.xlabel('miliseconds', size='14')
                plt.ylabel('Occurences', size='14')
                plt.show()