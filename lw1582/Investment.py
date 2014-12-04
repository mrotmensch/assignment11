'''import libraries used for calculations'''
import numpy as np

def investment(positions, num_trials):
  
  '''this program accepts two inputs: positions and num_trials:
     positions: list of number of shares to buy in parallel
     num_trials: how many times to randomly repeat the test

     the program returns the outcomes of num_trials times'''
  final_ret = np.zeros((num_trials,1))
  
  '''for every position, using the position value:
  1. calculate cumulative return that day with 51% chance of doubling and 49% of losing everythin
  2. calculate daily return based on cumulative return
  
  if there are 10 positions, each would be a random independent trial and the cumulative return is the sum of the outcome of the 10 positions'''
  for position in positions:
    position_value = 1000 / position
    
    win = position_value * 2
    odds = np.random.rand(num_trials,position)
    np.place(odds, odds > 0.51, 0)
    np.place(odds, odds != 0, win)
    cumu_ret = np.sum(odds, axis = 1)
    daily_ret = cumu_ret / 1000 -1
    daily_ret = np.expand_dims(daily_ret, axis =1)
    final_ret = np.concatenate((final_ret, daily_ret),axis = 1)
    
  final_ret = np.delete(final_ret,0,1)
  return final_ret
  
