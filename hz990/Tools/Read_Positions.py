import sys
import Exceptions
from True_Positions import *

def Read_Positions():
    '''This function reads the input positions and checks whether it is in correct form

    Returns the legal input if no exceptions raised'''
    while True:
        try:
            positions_raw = raw_input('Enter a list of positions or type \'quit\' to exit : \n')
            if positions_raw == 'quit':
                sys.exit()
            elif True_Positions(positions_raw):
                return positions_raw
                break
            else:
                raise Exceptions.Invalid_Position_List
        except Exceptions.Invalid_Position_List as e:
            print e
        except (KeyboardInterrupt, EOFError):
            sys.exit()


