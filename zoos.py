# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:53:45 2020

@author: khambarde
"""
#######################################################
'''You are required to enter a word that consists of  and  that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if .

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

First line: A word that starts with several Zs and continues by several Os.
Note: The maximum length of this word must be .
Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.
SAMPLE INPUT 
zzzoooooo
SAMPLE OUTPUT 
Yes
'''
#########################################################
# Write your code here
#Solution:

name = raw_input()
if 'zooo' in name:
    print('Yes')