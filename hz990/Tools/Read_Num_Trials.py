import sys
import Exceptions
def Read_Num_Trials():
    '''This function reads the input number of trials and checks whether it is in correct form

    Returns the legal input if no exceptions raised'''
    while True:
        try:
            num_trials_raw = raw_input('Enter number of trials you want or type \'quit\' to exit : \n')
            if num_trials_raw == 'quit':
                sys.exit()
            elif (isinstance(int(num_trials_raw), int) and int(num_trials_raw)>0):
                return num_trials_raw
                break
            else:
                raise Exceptions.Invalid_Num_Trials
        except Exceptions.Invalid_Num_Trials as e:
            print e
        except (KeyboardInterrupt, EOFError):
            sys.exit()