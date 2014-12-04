# -*- coding: utf-8 -*-
"""Programming for Data Science
   Assignment 8
   Mengfei Li
"""

from ass8 import *
import sys


"""This project simulate the investment instrument to determine how to 
   make a better bet under the certain rules.
   Warning:
   if a small number accepted for repeated times, the simulation may have
   a large variance
"""

def main():
    
     #Make sure receiving the correct form of positions
     while True:
         is_valid_pos_input=False             
         try:
           positions_input=raw_input('Enter a list of positions: ')
           if positions_input!='quit':
               try:
                   positions_list=input_validation(positions_input)
                   is_valid_pos_input=True
                   break
               except AssertionError as e:
                   print e
               except AssertionError as e:
                   print e
           elif positions_input=='quit':
               sys.exit()
         except KeyboardInterrupt:
            sys.exit()
     
     #make sure receiving the correct form of number of trials     
     
     while is_valid_pos_input:
         try:
           num_trials=raw_input('Enter an int for repeated times: ')
           if num_trials=='quit':
               sys.exit()
           else:
               num_trials=int(num_trials)
               break
         except ValueError:
             print "invalid input type. Please enter an integer"
         except KeyboardInterrupt:
            sys.exit()
            
           
    #simulate the gambling and store the results in the variable 'final'
     final=strats(positions_list,num_trials)    
    #generate results.txt
     statistics=stats(final,positions_list)
     with open('result.txt','w') as file:    
        file.write(str(statistics))
    #generate histograms        
     for p in positions_list:
        hist_generator(final,p)            
      
        



if __name__=='__main__':
    main()