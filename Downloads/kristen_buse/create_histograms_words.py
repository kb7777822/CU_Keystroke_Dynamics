#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:30:35 2020

@author: Kristen Buse

Takes in data in the form of a .txt file for a specific user that evals to a 
dictionary with graphs as keys and has as values - dictionaries with words as 
keys and a list of the length of its digraphs as values.
For instance, the text 
{'A/P': {'PAPER': [900123, 1165149, 895495, 1349998, 1550093, 1079863, 2281163, 
1839967, 1390870, 850107, 1215858, 1250310, 1150068, 800270, 1879992], 
'PARAGRAPH': [6411657]}
(That is, takes as input the output of create_dict_from_features.py)

This code does a few things: first, you choose the type of digraph (DD, DU, 
UD, UU) or monograph (M) you want to look at. Then you choose the user you
want to look at, or all users. It will print out the GRAPH_NUM most popular
graphs for that user. After choosing a graph, it will print out the WORD_NUM
most popular words for the selected user that contain the selected graph.
At this point, you have a few options: 
Typing '+' will plot the distribution of the graph for all words it occurs it. 
Typing a word or list of words (all caps,separated by a space) will plot the 
graph as it occurs in those words. 
Typing "except" followed by a list of words (all caps, separated by a 
space) will print out all words that this user typed with this graph except 
the ones in the list, and will plot the occurrences of the graph in those 
words. 
Typing "one" followed by a number will print out two lists of words: first, 
the words that only occurred once whose graph was faster than the given 
number; and second, the words that only occurred once whose graph was slower
than the given number. It will also plot the graph in the words that occur
once.


"""
import matplotlib.pyplot as plt
import numpy as np
import os


dict_path = '/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/'
BINS = np.arange(0,800,step=12.5) #histogram bins
GRAPH_NUM = 10
WORD_NUM = 20


while True:
    graph_type = input("Enter the type of graph (m, dd, uu, ud, or du): ")
    
    if not (graph_type == 'm' or graph_type == 'dd' or graph_type == 'uu' or graph_type == 'ud' or graph_type == 'du'):
        print('Enter a graph type correctly')
        continue
    user = input("Enter the participant # you'd like to look at the graphs of, or 'all' to look at all participants: ")
    user_dict = []
    user_title = ''
    if user == 'all':
        with open(dict_path + graph_type + '_dict_all.txt', 'r') as dict_file: 
            user_dict = eval(dict_file.readline())
        user_title = ' all users'
    else:
        file_name = dict_path + graph_type + '/' + graph_type + '_dict_' + user + '.txt'
        if not os.path.isfile(file_name):
            print("That wasn't a realy participant #, sorry!")
            continue
        with open(file_name) as dict_file:
            user_dict = eval(dict_file.readline())
        user_title = ' user ' + user
            
            
    #get the NUM_GRAPHS graphs with the largest representation
    max_graphs = ('',0)
    min_max_graphs = ('',100000000)
    biggest_graphs = []
    for letters in user_dict:
        if len(letters) == 3:

            number_of_graphs = 0
            for word in user_dict[letters]:
                number_of_graphs += len(user_dict[letters][word])
                
            if len(biggest_graphs) < GRAPH_NUM:
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
        
        print("The " + str(GRAPH_NUM)+ " most commonly occurring graphs are: ")
        
        for letters in biggest_graphs:
            print(letters[0]+ ' ' + str(letters[1]))
        
        
        letters = input("Enter the specific graph you want to look at (capital letters, \
                        digraph letters separated by a /), \n or 'exit' to stop looking at " + \
                graph_type + " for all users: ")

        if letters == 'exit':
            break

        if user_dict.get(letters) == None:
            print('Enter a real graph next time :(')
            continue
         
        #get the WORD_NUM words with the largest representation for the graph
        max_word = ('',0)
        min_max_word = ('',100000000)
        biggest_words = []
        for word in user_dict[letters]:                  
            number_of_words = 0                    
            number_of_words += len(user_dict[letters][word])                    
            if len(biggest_words) < WORD_NUM:
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
        
        print("The " + str(WORD_NUM) + " most commonly occurring words are: ")
        for word in biggest_words:
            print(word[0]+ ' ' + str(word[1]))
        
        words = input("Enter the words you'd like to look at, separated by a space (all caps please), or enter '+' to look at all words, " + 
                      "or enter \"except\" [words], or enter \"one\" [miliseconds] to print the words that only occur once before [miliseconds] " +
                      "and after [miliseconds]: ")
        histogram_input = []
        if words == '+':
            for word in user_dict[letters]:
                histogram_input += user_dict[letters][word]
        else:
            if len(words) == 0:
                print("give a word k thx")
                continue
            elif words.split()[0] == 'except': 
                for user_dict_word in user_dict[letters]:
                    if not user_dict_word in words.split()[1:]:
                        histogram_input += user_dict[letters][user_dict_word]
                        print(user_dict_word, end=" ")
                print('\n')
            elif words.split()[0] == 'one':
                time = int(words.split()[1]) * 10000
                quicker_words = []
                slower_words = []
                for user_dict_word in user_dict[letters]:
                    
                    if len(user_dict[letters][user_dict_word]) == 1:
                        histogram_input += user_dict[letters][user_dict_word]
                        if user_dict[letters][user_dict_word][0] > time:
                            slower_words += [user_dict_word]
                        else:
                           quicker_words += [user_dict_word]
                for quick_word in quicker_words:
                    print(quick_word, end=' ')
                print()
                for slow_word in slower_words:
                    print(slow_word, end=' ')
                print('\n')
                
                
            else:          
                for word in words.split():
                    if user_dict[letters].get(word) == None:
                        print("Sorry, the word " + word + " doesn't exist for the " + letters + " " + graph_type  + " graph")
                        continue
                    histogram_input += user_dict[letters][word]

        histogram_input = [x / 10000 for x in histogram_input] #tbh data should probably be changed so we don't have to do this.
        #anyway, that line converted the times to ms
        
        #make histogram
        plt.figure()
        plt.hist(histogram_input,bins=BINS,color='blue')
        plt.title(graph_type + ' ' + letters + ' ' + ' in the words: ' + words + ' for' + user_title)
        plt.xlabel('miliseconds', size='14')
        plt.ylabel('Occurences', size='14')
        plt.show()
        
                















