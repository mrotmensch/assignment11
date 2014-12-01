import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def makeHistogram(data, histLabel):
                
    # Make Histogram from data using labels from histLabel
    
    plt.figure()
    plt.hist(data, bins = 100, range = [-1,1])
    plt.xlim(-1,1)
    
    plt.ylabel(histLabel['yTxt']), 
    plt.xlabel(histLabel['xTxt']), 
    plt.title(histLabel['titleTxt'])
    
def generateLabels(denomination, numShares, numTrials):
    
    # Generates a dict of lables for plotting (title, x/y axis labels)
    
    numShares_str = str(numShares)
    numTrials_str = str(numTrials) 
    denom_str = str(int(denomination))
    
    if numShares == 1:
        titleTxt = numShares_str + ' Share of $' + denom_str + ', numTrials = ' + numTrials_str 
    else:
        titleTxt = numShares_str + ' Shares of $' + denom_str + ', numTrials = ' + numTrials_str      
    
    fileName = 'histogram_' + numShares_str.zfill(4)+'_pos.pdf'
     
    histLabel = {'titleTxt': titleTxt, 'yTxt': 'Count', 'xTxt': 'Return', 'fileName': fileName }
        
    return histLabel
    
def saveHistogramAsPDF(name):
    
    # Save Histogram
    
    pp = PdfPages(name)
    pp.savefig()
    pp.close()
    

    