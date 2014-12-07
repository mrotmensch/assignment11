import sys
import pandas as pd
from utility import *

def write_file(str, file_name):
	fp = open(file_name, "w")
	fp.write(str)
	fp.close()

def output_to_file(df, file_name):
        #Write results.txt
	try:
		write_file(df.to_string(), file_name)
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		return False
	except:
		print "Unexpected error", sys.exc_info()[0]
		return False

	return True
