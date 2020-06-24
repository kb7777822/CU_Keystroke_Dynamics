#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:40:44 2020

@author: kb7777822
"""
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KernelDensity
from scipy.signal import find_peaks

dict_path = '/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/'
BINS = np.arange(0,800,step=12.5) #histogram bins

debug = 2000
debug2 = 100

def get_peaks(dat, bandwidth, title):
    kde = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(dat.reshape(-1,1))
    dat2=np.exp(kde.score_samples(np.arange(np.min(dat),np.max(dat),(np.max(dat)-np.min(dat))/len(dat)).reshape(-1,1)))
    
    peaks=find_peaks(dat2,height=0.0007)[0]
    
    global debug
    debug-=1
    if debug==0:
        plt.figure()
        plt.hist(dat,density=True,alpha=0.4,bins=BINS)
        plt.plot(np.arange(np.min(dat),np.max(dat),(np.max(dat)-np.min(dat))/len(dat)),dat2)
        plt.title(title)
        print(peaks)
        plt.scatter(np.arange(np.min(dat),np.max(dat),(np.max(dat)-np.min(dat))/len(dat))[peaks],dat2[peaks],color='red')
        plt.show()
        debug=2000
    
    return len(peaks)

def single_file_eval(graph_type,bandwidth):
    for file in os.listdir(dict_path+graph_type):
        if file != '.DS_Store':
            user = file.split('_')[2][:-4]
            with open(dict_path+graph_type+'/'+file) as dict_file:
                graph_dict = eval(dict_file.readline())
            all_interesting = []
            for graph in graph_dict:
                #global debug2
                #debug2-=1
                #if debug2==0:
                #    sys.exit()
                histogram_input = []
                for word in graph_dict[graph]:
                    histogram_input += graph_dict[graph][word]
                if len(histogram_input) > 50:
                    histogram_input = [int(np.round(x / 10000)) for x in histogram_input]
                    if get_peaks(np.array(histogram_input), bandwidth, graph_type + ' ' + graph + ' ' + user) > 1:
                        all_interesting += [graph]            
            
            interesting_file = open(graph_type + '_' + user + '_interesting.txt','w')
            interesting_file.write(str(all_interesting))
            interesting_file.close()
            print(user)

single_file_eval('du',35)     
#single_file_eval('uu',30)       
#single_file_eval('ud',35)
#single_file_eval('m',20)
#single_file_eval('dd',20)

#dd
#all
#with open(dict_path + 'dd_dict_all.txt') as dd_dict_all_file:
#    dd_dict_all = eval(dd_dict_all_file.readline())
#    dd_all_interesting_file = open('dd_all_interesting.txt', 'w')
#    dd_all_interesting = []
#    for graph in dd_dict_all:
#       histogram_input = []
#       for word in dd_dict_all[graph]:
#            histogram_input += dd_dict_all[graph][word]
#        if len(histogram_input) > 50:
#            histogram_input = [int(np.round(x / 10000)) for x in histogram_input]
#            if get_peaks(np.array(histogram_input), graph + ' all') > 1:
#                dd_all_interesting += [graph]
            
#dd_all_interesting_file.write(str(dd_all_interesting))
#dd_all_interesting_file.close()          
            


