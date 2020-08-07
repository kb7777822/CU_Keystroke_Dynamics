#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:25:50 2020

@author: Kristen Buse

This takes as input a directory, with files titled [user].txt. These files have
on each line, 3 things, separated by spaces: a timestamp, a 0 or 1 indicating
if a key was pressed or released, and the key being pressed/released.

This generates, for each user, 5 files titled 
[graph type]_graphs_words_[user].txt, with the 5 graph types being m, dd, uu, 
ud, and du. Each file has, on each line, separated by a space, the symbols 
that make up the graph, the length of the graph, the timestamp, and the word
the graph is in.

A few notes: 
Files are saved in the same directory with the name 
[type of graph]_graphs_words_[user].txt
This discards graphs with a length of 0 and those that are over MAX_TIME 
(which is currently the same for all graphs). 
If the user types a symbol, the word associated is "%". Also, the "word" 
doesn't account for things like backspace.
"""

import os

MAX_TIME = 8000000 
raw_path = '/Users/kb7777822/Downloads/kristen_buse/clarkson_free_text_keystroke_db/'

for file in os.listdir(raw_path):
    raw_data = open(raw_path + file,'r')
    user = os.fsdecode(file)
    processed_data_m = open('m_graphs_words_' + user + '.txt','w')
    processed_data_dd = open('dd_graphs_words_' + user + '.txt','w')
    processed_data_uu = open('uu_graphs_words_' + user + '.txt','w')
    processed_data_ud = open('ud_graphs_words_' + user + '.txt','w')
    processed_data_du = open('du_graphs_words_' + user + '.txt','w')

    line = raw_data.readline()
    m_dict = {}
    dd_next = ('',0)
    ud_next = ('',0)
    uu_next = ('',0)
    du_queue = []
    word = '%'
    inWord = False
    
    print(user)
    
    while not line == '':
        current_line = line.split()
        timestamp = int(current_line[0])
        
        
        #This block of code determines the word we're in.
        if not inWord:
            last_timestamp = 0
            if len(current_line[2]) == 1:
                inWord = True
                current_file_position = raw_data.tell()
                word = current_line[2]

                current_word_line = raw_data.readline().split()
                #We consider a word to end if the user types a non-letter that isn't Shift
                while len(current_word_line) > 0  and (len(current_word_line[2]) == 1 or current_word_line[2] == 'LShiftKey'):
                    if len(current_word_line[2]) == 1 and current_word_line[1] == '0':
                        word += current_word_line[2]
                    current_word_line = raw_data.readline().split()
                raw_data.seek(current_file_position)
        
        #We consider a word to end if the user types a non-letter that isn't Shift
        if not(len(current_line[2]) == 1 or current_line[2] == 'LShiftKey'):
            inWord = False
            word = '%'
                
        
        #m monograph
        if (current_line[1] == '0'):
            m_dict[current_line[2]] = timestamp
        else:
            if m_dict.get(current_line[2]) != None:
                m = timestamp - m_dict[current_line[2]]
                if m < MAX_TIME and m > 0:
                    processed_data_m.write(current_line[2] + ' ' + str(m) + ' ' + current_line[0] + ' ' + word + '\n')
    
        #dd digraph
        if dd_next != ('',0):
            if current_line[1] == '0':
                dd = timestamp - dd_next[1]
                if dd < MAX_TIME and dd > 0:
                    processed_data_dd.write(dd_next[0] + '/' + current_line[2] + ' ' + str(dd) + ' ' + current_line[0] + ' ' + word + '\n')
                dd_next = (current_line[2],timestamp)
        else:
            dd_next = (current_line[2],timestamp)
        
        #ud digraph
        if ud_next != ('',0):
            if current_line[1] == '1':
                ud_next = (current_line[2],timestamp)
            else:
                ud = timestamp - ud_next[1]
                if ud < MAX_TIME and dd > 0:
                    processed_data_ud.write(ud_next[0] + '/' + current_line[2] + ' ' + str(ud) + ' ' + current_line[0] + ' ' + word + '\n')
        else:
            if current_line[1] == '1':
                ud_next = (current_line[2],timestamp)
                
        #uu digraph
        if uu_next != ('',0):
            if current_line[1] == '1':
                uu = timestamp - uu_next[1]
                if uu < MAX_TIME and uu > 0:
                    processed_data_uu.write(uu_next[0] + '/' + current_line[2] + ' ' + str(uu) + ' ' + current_line[0] + ' ' + word + '\n')
                uu_next = (current_line[2],timestamp)
        else:
            if current_line[1] == '1':
                uu_next = (current_line[2],timestamp)
        
        #du digraph
        #this is a weird one: basically, we add down keypresses to a queue, and when we get an up keypress, we delete from the
        #queue everything except the key that just went up and the most recent keydown that wasn't the letter that was 
        #released. Sorry if that wasn't a great explanation, I can give a better one w/an example.
        if current_line[1] == '0':
            du_queue += [(current_line[2],timestamp)]
        else:
            to_delete = []
            last_noncurrent_letter_index = -1
            
            for i in range(0,len(du_queue)):
                key = du_queue[i]
                if key[0] != current_line[2]:
                    du = timestamp - key[1]
                    if i != len(du_queue) - 1:
                        to_delete += [i]
                    if du < MAX_TIME and du > 0:
                        processed_data_du.write(key[0] + '/' + current_line[2] + ' ' + str(du) + ' ' + current_line[0] + ' ' + word + '\n')
                    
            for j in reversed(range(0,len(to_delete))):    
                if len(du_queue) > 1:
                    del du_queue[to_delete[j]]

        
        line = raw_data.readline()
        
        
    raw_data.close()

