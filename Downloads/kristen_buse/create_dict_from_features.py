#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:38:27 2020

@author: Kristen Buse

This takes the output of create_features_words_timestamps.py and puts it in
a format compatible with create_histograms_words.py and get_interesting_graphs.py.

This program takes as input the five directories to the output of 
create_features_words_timestamps.py
It generates, for each user, a file titled [graph type]_dict_[user].txt, which
is a text file that evals to a nested dictionary whose keys are graphs and whose
values are dictionaries whose keys are words and whose values are lists of
the lengths of the graph as it occurs in that word.


"""
import os


m_graphs_path = '/Users/kb7777822/Downloads/kristen_buse/Graphs_with_word_labels_(and_timestamps!)/m_graphs_words'
dd_graphs_path = '/Users/kb7777822/Downloads/kristen_buse/Graphs_with_word_labels_(and_timestamps!)/dd_graphs_words'
uu_graphs_path = '/Users/kb7777822/Downloads/kristen_buse/Graphs_with_word_labels_(and_timestamps!)/uu_graphs_words'
ud_graphs_path = '/Users/kb7777822/Downloads/kristen_buse/Graphs_with_word_labels_(and_timestamps!)/ud_graphs_words'
du_graphs_path = '/Users/kb7777822/Downloads/kristen_buse/Graphs_with_word_labels_(and_timestamps!)/du_graphs_words'

#If true, this generates a separate file for each user. If false, all users' data gets clumped together.
generate_individual_dicts = False

#TODO: remove all the repetition in this code whoops
if generate_individual_dicts: 
    
    #m monographs
    for file in os.listdir(m_graphs_path):
        with open(m_graphs_path + '/' + file, 'r') as m_graphs: 
            user = file.split('_')[3]
            with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/m/m_dict_' + user,'w') as m_dict_file:
                m_graphs_words_dict = {}
                for line in m_graphs:
                    split_line = line.split()
                    if split_line[3] != '%': #if it's not in a word
                        if len(split_line[3]) < 20: #if the word isn't long nonsense
                            if m_graphs_words_dict.get(split_line[0]) == None: #if the dictionary doesn't have that graph         
                               m_graphs_words_dict[split_line[0]] = {}
                               m_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                            else: 
                               if m_graphs_words_dict[split_line[0]].get(split_line[3]) == None:#if the dictionary has the graph but not the word
                                   m_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                               else: #if the dict has both the graph and the word
                                   m_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
                m_dict_file.write(str(m_graphs_words_dict))

    for file in os.listdir(dd_graphs_path):
        with open(dd_graphs_path + '/' + file, 'r') as dd_graphs: 
            user = file.split('_')[3]
            with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/dd/dd_dict_' + user,'w') as dd_dict_file:
                dd_graphs_words_dict = {}
                for line in dd_graphs:
                    split_line = line.split()
                    if split_line[3] != '%': #if it's not in a word
                        if len(split_line[3]) < 20: #if the word isn't long nonsense
                            if dd_graphs_words_dict.get(split_line[0]) == None: #if the dictionary doesn't have that graph                 
                               dd_graphs_words_dict[split_line[0]] = {}
                               dd_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                            else:
                               if dd_graphs_words_dict[split_line[0]].get(split_line[3]) == None:#if the dictionary has the graph but not the word
                                   dd_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                               else:#if the dict has both the graph and the word
                                   dd_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
                dd_dict_file.write(str(dd_graphs_words_dict))
                
    for file in os.listdir(uu_graphs_path):
        with open(uu_graphs_path + '/' + file, 'r') as uu_graphs: 
            user = file.split('_')[3]
            with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/uu/uu_dict_' + user,'w') as uu_dict_file:
                uu_graphs_words_dict = {}
                for line in uu_graphs:
                    split_line = line.split()
                    if split_line[3] != '%':#if it's not in a word
                        if len(split_line[3]) < 20:#if the word isn't long nonsense
                            if uu_graphs_words_dict.get(split_line[0]) == None:#if the dictionary doesn't have that graph               
                               uu_graphs_words_dict[split_line[0]] = {}
                               uu_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                            else:
                               if uu_graphs_words_dict[split_line[0]].get(split_line[3]) == None:#if the dictionary has the graph but not the word
                                   uu_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                               else:#if the dict has both the graph and the word
                                   uu_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
                uu_dict_file.write(str(uu_graphs_words_dict))
                
    for file in os.listdir(ud_graphs_path):
        if file != ".DS_Store":
            with open(ud_graphs_path + '/' + file, 'r') as ud_graphs: 
                user = file.split('_')[3]
                with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/ud/ud_dict_' + user,'w') as ud_dict_file:
                    ud_graphs_words_dict = {}
                    for line in ud_graphs:
                        split_line = line.split()
                        if split_line[3] != '%':
                            if len(split_line[3]) < 20:
                                if ud_graphs_words_dict.get(split_line[0]) == None:              
                                   ud_graphs_words_dict[split_line[0]] = {}
                                   ud_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                                else:
                                   if ud_graphs_words_dict[split_line[0]].get(split_line[3]) == None:
                                       ud_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                                   else:
                                       ud_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
                    ud_dict_file.write(str(ud_graphs_words_dict))
                
    for file in os.listdir(du_graphs_path):
        with open(du_graphs_path + '/' + file, 'r') as du_graphs: 
            user = file.split('_')[3]
            with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/du/du_dict_' + user,'w') as du_dict_file:
                du_graphs_words_dict = {}
                for line in du_graphs:
                    split_line = line.split()
                    if split_line[3] != '%':
                        if len(split_line[3]) < 20:
                            if du_graphs_words_dict.get(split_line[0]) == None:              
                               du_graphs_words_dict[split_line[0]] = {}
                               du_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                            else:
                               if du_graphs_words_dict[split_line[0]].get(split_line[3]) == None:
                                   du_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                               else:
                                   du_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
                du_dict_file.write(str(du_graphs_words_dict))    
else:
    
#graphs_words_dict - {letter: {word: [list of graphs]}}

    with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/m_dict_all.txt','w') as m_dict_file:
        m_graphs_words_dict = {}
        
        for file in os.listdir(m_graphs_path):
            with open(m_graphs_path + '/' + file, 'r') as m_graphs:           
                for line in m_graphs:
                    split_line = line.split()
                    if split_line[3] != '%':
                        if len(split_line[3]) < 20:
                            if m_graphs_words_dict.get(split_line[0]) == None:              
                               m_graphs_words_dict[split_line[0]] = {}
                               m_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                            else:
                               if m_graphs_words_dict[split_line[0]].get(split_line[3]) == None:
                                   m_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                               else:
                                   m_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
        m_dict_file.write(str(m_graphs_words_dict))
    

        
    with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/dd_dict_all.txt','w') as dd_dict_file:
        dd_graphs_words_dict = {}
        for file in os.listdir(dd_graphs_path):
            with open(dd_graphs_path + '/' + file, 'r') as dd_graphs:
                for line in dd_graphs:
                    split_line = line.split()
                    if split_line[3] != '%':
                        if len(split_line[3]) < 20:
                            if dd_graphs_words_dict.get(split_line[0]) == None:              
                               dd_graphs_words_dict[split_line[0]] = {}
                               dd_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                            else:
                               if dd_graphs_words_dict[split_line[0]].get(split_line[3]) == None:
                                   dd_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                               else:
                                   dd_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
        dd_dict_file.write(str(dd_graphs_words_dict))

    with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/uu_dict_all.txt','w') as uu_dict_file:
        uu_graphs_words_dict = {}
        for file in os.listdir(uu_graphs_path):
            with open(uu_graphs_path + '/' + file, 'r') as uu_graphs:
                for line in uu_graphs:
                    split_line = line.split()
                    if split_line[3] != '%':
                        if len(split_line[3]) < 20:
                            if uu_graphs_words_dict.get(split_line[0]) == None:              
                               uu_graphs_words_dict[split_line[0]] = {}
                               uu_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                            else:
                               if uu_graphs_words_dict[split_line[0]].get(split_line[3]) == None:
                                   uu_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                               else:
                                   uu_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
        uu_dict_file.write(str(uu_graphs_words_dict))
    
    with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/ud_dict_all.txt','w') as ud_dict_file:
        ud_graphs_words_dict = {}
        for file in os.listdir(ud_graphs_path):
            if file != '.DS_Store': #macs sure are weird.
                with open(ud_graphs_path + '/' + file, 'r') as ud_graphs:
                    for line in ud_graphs:
                        split_line = line.split()
                        if split_line[3] != '%':
                            if len(split_line[3]) < 20:
                                if ud_graphs_words_dict.get(split_line[0]) == None:              
                                   ud_graphs_words_dict[split_line[0]] = {}
                                   ud_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                                else:
                                   if ud_graphs_words_dict[split_line[0]].get(split_line[3]) == None:
                                       ud_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                                   else:
                                       ud_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
        ud_dict_file.write(str(ud_graphs_words_dict))
    
    with open('/Users/kb7777822/Downloads/kristen_buse/Graph_dicts_(for_histogram_purposes)/du_dict_all.txt','w') as du_dict_file:
        du_graphs_words_dict = {}
        for file in os.listdir(du_graphs_path):
            with open(du_graphs_path + '/' + file, 'r') as du_graphs:
                for line in du_graphs:
                    split_line = line.split()
                    if split_line[3] != '%':
                        if len(split_line[3]) < 20:
                            if du_graphs_words_dict.get(split_line[0]) == None:              
                               du_graphs_words_dict[split_line[0]] = {}
                               du_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                            else:
                               if du_graphs_words_dict[split_line[0]].get(split_line[3]) == None:
                                   du_graphs_words_dict[split_line[0]][split_line[3]] = [int(split_line[1])]
                               else:
                                   du_graphs_words_dict[split_line[0]][split_line[3]] += [int(split_line[1])]
        du_dict_file.write(str(du_graphs_words_dict))    

    m_graphs.close()
    dd_graphs.close()
    uu_graphs.close()
    ud_graphs.close()
    du_graphs.close()

