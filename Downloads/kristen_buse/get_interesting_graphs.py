#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program takes as input a folder of .txt files titled [graph type]_dict_[user].txt
where graph type is dd, du, ud, or uu. (This does not currently work for m 
monographs.) The input files eval to a 
dictionary with graphs as keys and has as values - dictionaries with words as 
keys and a list of the length of its digraphs as values.
For instance, the text 
{'A/P': {'PAPER': [900123, 1165149, 895495, 1349998, 1550093, 1079863, 2281163, 
1839967, 1390870, 850107, 1215858, 1250310, 1150068, 800270, 1879992], 
'PARAGRAPH': [6411657]}

The program outputs, for each file in the directory given, a .txt file titled
[graph type]_[user]_interesting.txt containing a list of all the digraphs
deemed "interesting", that is, multimodal.


Created on Mon Jun 22 18:40:44 2020

@author: Kristen Buse and Blaine Ayotte
"""
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KernelDensity
from scipy.signal import find_peaks

dict_path = '/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/'
BINS = np.arange(0,800,step=33) #histogram bins

#debug = 4
#debug controls the amount of (visual) graphs produced. uncomment lines 32 and 
#50 to graph every debug-th graph

def get_peaks(dat, bandwidth, title):
#returns the number of peaks in dat, doing kde with bandwidth

    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(dat.reshape(-1,1))
    #^gives us an estimation of the pdf of the histogram. bandwidth controls how sensitve it is
    dat2=np.exp(kde.score_samples(np.arange(np.min(dat),np.max(dat),(np.max(dat)-np.min(dat))/len(dat)).reshape(-1,1)))
    #^I honestly am not sure what this does, but I trust Blaine
    
    peaks=find_peaks(dat2,height=0.001,width=10)[0]
    #^gives us a list of the peaks in the data. 
    #^height is the minimun frequency to be considered a peak
    #^width is the minimum width to be considered of a peak

    global debug
    #debug-=1
    if debug==0:
        plt.figure()
        plt.hist(dat,density=True,alpha=0.4,bins=BINS)
        plt.plot(np.arange(np.min(dat),np.max(dat),(np.max(dat)-np.min(dat))/len(dat)),dat2)
        plt.title(title)
        print(peaks)
        plt.scatter(np.arange(np.min(dat),np.max(dat),(np.max(dat)-np.min(dat))/len(dat))[peaks],dat2[peaks],color='red')
        plt.show()
        debug=40
    #this part just plots every debug graphs. feel free to get rid of it
    
    return len(peaks)

def directory_eval(graph_type,bandwidth):
    for file in os.listdir(dict_path+graph_type):
        if file != '.DS_Store': #this is a mac thing
            user = file.split('_')[2][:-4]
            
            with open(dict_path+graph_type+'/'+file) as dict_file:
                graph_dict = eval(dict_file.readline())

            all_interesting = [] 
            #this is our list where we store all the multimodal graphs for this user
            
            for graph in graph_dict:
                if len(graph) == 3: #we're only looking at letter-letter graphs                                        
                    histogram_input = [] 
                    #this is where we store all of the values this person has for this graph
                    for word in graph_dict[graph]:
                        histogram_input += graph_dict[graph][word]
                    if len(histogram_input) > 50: #if we have enough data on this graph
                        histogram_input = [int(np.round(x / 10000)) for x in histogram_input] 
                        #converts the data ints, in miliseconds
                        if get_peaks(np.array(histogram_input), bandwidth, graph_type + ' ' + graph + ' ' + user) > 1:
                            all_interesting += [graph]

                    
            interesting_file = open(graph_type + '_' + user + '_interesting.txt','w')
            interesting_file.write(str(all_interesting))
            interesting_file.close()
            #^write to a file
            print(user)

#directory_eval('du',35)     
#directory_eval('uu',30)       
#directory_eval('ud',35)
directory_eval('dd',35)     
#these bandwidth values were all found through trial and error; there might be better ones   
            


