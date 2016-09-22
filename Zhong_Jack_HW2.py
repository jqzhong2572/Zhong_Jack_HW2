# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:23:57 2016

@author: Jack Zhong
"""

#-----------------------Question 1---------------------------      
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
    if string[::-1] == string: # if the reverse is the same as itself
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
    
    
palindrome_file('Z:/1.txt')




#-----------------------Question 2---------------------------
def semordnilap_file(file):
    '''
    accept a file and prints all pairs of words that are semordnilaps
    
    Parameter:
    a file
    
    Return:
    pairs of words that are semordnilaps
    '''
    
    file1 = open(file) # open a file
    wordlist = file1.read().split() # separate lines by white space 
    output = [] # initialize output
    for word1 in wordlist: # variable 1 from wordlist
        for word2 in wordlist: # variable 2 from wordlist
            if word1 == word2[::-1]: # [::-1] reverse a string
                output.append(word1 + ' ' + word2)             
    return output


print(semordnilap_file('Z:/2.txt'))





#-----------------------Question 3---------------------------      
def char_freq_table(filepath):
    '''
    function car_freq_table() accepts a file name from the user, builds a
    frequency listing of the characters contained in the file, and prints a 
    sorted and nicely formatted character frequency table to the screen.    
    
    Parameter:
    a file
    
    Returns:
    frequency list of characters
    '''
   
    import string # import punctuation
    file1 = open(filepath) # open a file
    string1 = file1.read().lower().replace(" ", "").replace("\n", "")
        # read the file, lowercase everthing, get rid of spaces and line changes
    punc = list(string.punctuation)  # exclude punctuation
    string1 = ''.join(ch for ch in string1 if ch not in punc) # strip punctuation
    num = list (string.digits)
    string1 = ''.join(ch for ch in string1 if ch not in num) # strip numbers
    
    dic= {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,
          'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,
          'u':0,'v':0,'w':0,'x':0,'y':0,'z':0} # initialize a dictionary
    for char in string1:
        dic[char] += 1 # add counts
    import operator
    sorted_dic = sorted(dic.items(), key=operator.itemgetter(0))
        # we can only return a sorted list since dictionary cannot be sorted
    print (sorted_dic)


char_freq_table('Z:/3.txt')




#-----------------------Question 4---------------------------    
def speak_ICAO(string,ICAOpause=1,lengthpause=3):
    '''
    procedure speak_ICAO() is able to translate any text (i.e. any string)
    into spoken ICAO words.
    Apart from the text to be spoken, your procedure also needs to accept two 
    additional parameters: a float indicating the length of the pause between 
    each spoken ICAO word, and a float indicating the length of the pause 
    between each word spoken.
    
    Parameter:
    a string, 2 float indication pause duration
    
    Returns:
    spoken words
    
    '''

    from string import punctuation
    import os, time    
    ICAO = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
	 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
	 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
	 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
	 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
	 'z':'zulu'} # define dictionary dic
    words = string.split() # split string into words
    for word in words: # For every word in the provided string
        for char in word: # and get each character
            if char not in punctuation: # we can only pronounce characters
                os.system('say ' + ICAO[char.lower()])
                time.sleep(ICAOpause) # pause after each character
        time.sleep(lengthpause) # pause after each word
      
    
speak_ICAO('hello how are you',0.5,2) 




#-----------------------Question 5--------------------------- 
def hapax(filepath):
    '''
    A hapax legomenon (often abbreviated to hapax) is a word which
    occurs only once in either the written record of a language, the
    works of an author, or in a single text. Define a function that given
    the file name of a text will return all its hapaxes. Make sure your
    program ignores capitalization.
    
    Parameter:
    a file
    
    Returns:
    all hapaxes
    '''

    string1 = open(filepath).read().lower() #read file and lowercase everything
    import string
    punc = list(string.punctuation)  # exclude punctuation
    string1 = ''.join(ch for ch in string1 if ch not in punc) # strip punctuation
    hapaxes = [] # initialize
    for i in string1.split():
        if string1.count(i) == 1: # if the word is only counted once
            hapaxes.append(i) # then its a hapaxes and add it to the list
    return hapaxes


hapax('Z:/4.txt')




#-----------------------Question 6--------------------------- 
def add_line_num(filepath):
    '''
    Write a program that given a text file will create a new text file in
    which all the lines from the original file are numbered from 1 to n
    (where n is the number of lines in the file).
    
    Parameter:
    a file
    
    Return:
    a new file with lines numbered
    '''
    
    file1 = open(filepath).readlines() # read each line
                                       # and return a list of strings
    file2 = open(input('New file location (eg. D:/123.txt): ')
                        +'.txt', 'w')
                    # create a new file in a desired location 
    for i in range(len(file1)): # range returns a list from 0 to n-1
                                # len returns a single int so we need range()
        file2.write('line'+str(i+1)+': '+file1[i])
            # write 'line' then the number of lines, since string starts with
            # [0] so I put str(i+1), then just put the actual line
    file2.close() # close
    
    
add_line_num('Z:/1.txt')




#-----------------------Question 7--------------------------- 
def avg_word_length(filepath):
    '''
    avg_word_length() will calculate the average word length of a text
    stored in a file (i.e the sum of all the lengths of the word tokens in
    the text, divided by the number of word tokens).

    Parameter:
    a file

    Return:
    average word length
    '''
    
    import string
    string1 = open(filepath).read().replace('\n',' ') # no change line sign
    punc = list(string.punctuation)  # exclude punctuation
    string1 = ''.join(ch for ch in string1 if ch not in punc) # strip punctuation
    word_count = len(string1.split()) # split words and count
    length_count = len(string1.replace(' ','')) # remove spaces and count
    return length_count / word_count


avg_word_length('Z:/5.txt')




#-----------------------Question 8--------------------------- 
def guess():
    '''
    guess() is able to play the "Guess the number"-game, where
    the number to be guessed is randomly chosen between 1 and 20.

    Parameter:
    N/A
    
    Returns
    number of guesses until reach the correct answer
    '''
    
    name = input('What is your name?   ')
    print('Well, {}, I am thinking of a number between 1 and 20.'.format(name))
    count = 0 # initialize
    while True:
        num_guess = int(input('Take a guess  '))
        if  num_guess<1 or num_guess>20:
            print('Are you stupid? I said 1-20!')
        elif num_guess == 18:
            print('Good job, {}! You guessed my number in {} guesses!'
                    .format(name,count+1)) # count + the last guess
            break # stop the program
        elif num_guess > 18:
            print('Your guess is too high.') 
        else:                        
            num_guess = print('Your guess if too low.')
        count += 1 # add a count everytime after judging if it is 18
    return None


guess()




#-----------------------Question 10-------------------------- 
def lingo(word):
    '''
    There is a hidden word, five characters long.The object of the game is 
    to find this word by guessing, and in return receive two kinds of clues: 
    1) the characters that are fully correct, with respect to identity 
       as well as to position, put square brackets, and 
    2) the characters that are indeed present in the word, but which are
       placed in the wrong position, put ordinary parentheses
       
    Parameter:
    an answer key
    
    Returns:
    clue with modified input
    '''
    ## take care of the error if input is a word other than 5 characters     
    
    while True:
        guess = input('') # guess a word in each iteration
        output = '' # initialize output string
        if len(guess) != 5:
            print('the word has five characters') # prevent input which
                       # is not 5 characters leading my code to an error
        else:
            for i in range(len(word)): # index position of the word
                if guess[i] == word[i]:
                    output += '[{}]'.format(guess[i]) # requirement 1)
                elif guess[i] in word:
                    output += '({})'.format(guess[i]) # requirement 2)
                else:
                    output += guess[i] # if it doesn't match anything
            print('Clue: ', output)
        if guess == word: # when the program is terminated
            break
    
    
lingo('tiger')    
        



#-----------------------Question 11-------------------------- 
def sent_splitter(filepath):
    '''
    This function opens a txt file and works as a sentence splitter to
    write its sentences with each sentences on a separate line.
    Sentence boundaries occur at one of "." (periods), "?" or "!", except that
    a. Periods followed by whitespace followed by a lower case letter
    are not sentence boundaries.
    b. Periods followed by a digit with no intervening whitespace are
    not sentence boundaries.
    c. Periods followed by whitespace and then an upper case letter,
    but preceded by any of a short list of titles are not sentence
    boundaries. Sample titles include Mr., Mrs., Dr., and so on.
    d. Periods internal to a sequence of letters with no adjacent
    whitespace are not sentence boundaries (for example,
    www.aptex.com, or e.g).
    e. Periods followed by certain kinds of punctuation (notably comma
    and more periods) are probably not sentence boundaries.   
    
    Parameter:
    a file
    
    Returns:
    a modified file
    '''
    punc = '?!'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    title = ['Mr','Mrs','Dr']
    punctuation = '`~!@#$%^&*()_-=+[]{}\|;:,<.>/?'
    string = open(filepath,'r').read() # read it only with 'r'
    string = string.replace('\n', ' ') # get rid of old new lines
    for i in range(1,len(string)-2):
        # in case the code go to an error, my index is from [1] to len()-2
        if string[i] == '.': # if char is a period
            if string[i+1] == ' 'and string[i+2] in lower:
                string = string
                # Periods followed by whitespace followed by a lower case letter
            elif string[i+1] in num:
                string = string 
                # Periods followed by a digit with no intervening whitespace 
            elif ((string[i-2:i] or string[i-3:i]) in title and
                   string[i+1]==' ' and string[i+2] in cap):
                string = string 
                # Periods followed by whitespace and then an upper case letter, 
                # but preceded by any of a short list of titles
            elif string[i-1] != ' ' and string[i+1] != ' ':
                string = string 
                # Periods internal to a sequence of letters with no adjacent whitespace
            elif string[i+1] in punctuation:
                string = string 
                # Periods followed by certain kinds of punctuation
            else:
                string = string[:i+1] + '\n' + string[i+2:] 
                # Add new line mark after period, and copy the rest
        elif string[i] in punc:
            string = string[:i+1] + '\n' + string[i+2:]
            # other punctuation definitely indicates a new line
    file1 = open(filepath,'w') # open for write
    file1.write(string) # write string into it
    file1.close() # close it