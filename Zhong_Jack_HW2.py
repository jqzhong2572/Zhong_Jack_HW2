# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:23:57 2016

@author: Jack
"""

#-----------------------Question 1---------------------------
def reverse(string):
    '''
    function reverse() takes a string and return a string with reversed order
    of the characters
    
    Parameter:
    a string
    
    Return:
    the string in reversed order
    '''
    
    end_of_str = len(string)-1 # length of string minus 1
                               # because we start from [0]
    string_reverse = '' # initialize the reverse of the string
    for Char in string:
        string_reverse += string[end_of_str] # building the output from the end
        end_of_str -= 1
    return string_reverse
        
        
def is_palindrome(string):
    '''    
    function is_palindrome() recognizes palindromes
    (i.e. words that look the same written backwards). 
    For example, is_palindrome("radar")should return True.
    
    Parameter:
    a string
    
    Return:
    True if the string is a palindrome, false otherwise
    '''
    ## take care of mixed case, take out numbers, punctuations and spaces

    string = string.upper() # get everything uppercased
    string = string.replace(' ', '') # delete spaces
    if not string.isalpha():
        return False     # return false if there is non-character in it
    if reverse(string) == string:
        return True
    else:
        return False
    

def palindrome_file(file):
    '''
    function palindrome_file() reads a file and apply palindrome function
    to all lines then return lines that are palindrome
    
    Parameter:
    a file
    
    Return:
    lines that are palindrome
    
    
    '''
    file1 = open(file) # open a file
    for line in file1.read().split('\n'): # read file by lines separated by \n
        if is_palindrome(line):
            print(line) # print the line if it is palindrome
    return None
    
    
palindrome_file('C:/Users/a.txt')




#-----------------------Question 2---------------------------
def Semordnilap_file(file):
    '''
    accept a file and prints all pairs of words that are semordnilaps
    
    Parameter:
    file
    
    Return:
    pairs of words that are semordnilaps
    '''
    
    file1 = open(file) # open a file
    wordlist = file.read().split() # initialize the wordlist 
    output = []
    for word1 in wordlist:
        for word2 in wordlist:
            if word1 == words2[::-1]:
                output.append(word1)
                output.append(word2)
    return output
   
   
   
   
   
   i = 0
    while i<= length:
        j = 0
        while j <= length:
            if wordlist[i] == reverse(wordlist[j]):
                print(wordlist[i] + ' ' + wordlist [j])
                del wordlist [i]
                del wordlist [j]
                length -= 2
            else:
                j += 1None
    return 


def is_semordnilap(filepath):
    file = open(filepath)
    words = file.read().split()
    results = []
    for word1 in words:
        for word2 in words:
            if word1 == word2[::-1]:
                results.append(word1)
    return results



Semordnilap_file('C:/Users/b.txt')
        
        
       
       
       











