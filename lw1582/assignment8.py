
'''import module for assignment8'''
from result import result
from userinput import *
import sys

def main():
  
  '''check for empty input'''
  while True:
    try:
      positions_input, num_trials_input = get_input()
      break
    except:
      print 'empty input'
  
  '''exit program on prompt'''
  if (positions_input == 'exit') or (num_trials_input == 'exit'):
    sys.exit()
  
  '''check for valid input'''
  while True:
    try:
      positions,num_trials = parse_input(positions_input,num_trials_input)
      break
    except:
      print 'invalid input'

  '''runs investment simulation on user input'''
  result(positions, num_trials)

if __name__=="__main__":
  try:
    main()
  except KeyboardInterrupt:
    sys.exit()

