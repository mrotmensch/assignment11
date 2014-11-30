import sys, re
from userexceptions import InputError, ConversionError

def med_input(prompt, exit_flags=['quit', 'exit']):
    """ Handle basic KeyboardInterrupt, EOF, and user termination. """
    try:
        raw = raw_input(prompt)
    except (KeyboardInterrupt, EOFError):
        sys.exit('Interrupted')

    if raw in exit_flags:
        sys.exit('Terminated by user')
    else:
        med = raw
        
    return med

def well_input(prompt, required_type, exit_flags=['quit', 'exit']):
    """ Convert input to required type, exit if not able to convert. """
    med = med_input(prompt, exit_flags)
    if type(required_type) != type:
        raise InputError('{} is not a type'.format(required_type))
    try:
        well = required_type(med)
    except ValueError:
        raise ConversionError('Cannot convert {0} to {1}'.format(med, required_type))

    return well

def list_input(prompt, required_type, exit_flags=['quit', 'exit']):
    """ Convert user input to a list. Input needs to be separated by comma. exit if coversion fails. """
    well = re.split('\s*,\s*', med_input(prompt, exit_flags))
    if type(required_type) != type:
        raise InputError('{} is not a type'.format(required_type))
    try:
        well = map(required_type, well)
    except ValueError:
        raise ConversionError('Please check your input list')

    return well
            
