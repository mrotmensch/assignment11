import seaborn as sns
import simulation
import plotting
import userInput
from sys import exit
import os

'''
Words go here
'''

def main():
    
    try:
        sns.set_palette("deep", desat=.6)
        sns.set_context(rc={"figure.figsize": (8, 5)})
    except:
        pass
    
    pWin = 0.51
    
    ###########################################################################
    # Get User Input
    ###########################################################################
    
    # Get Positions
    positionOK = False
    
    while positionOK != True:
        
        try:
            positions = userInput.getUserPositions()
            positionOK = userInput.checkPositions(positions)
            
        except KeyboardInterrupt:
    
            exit('Exiting')
            
        except userInput.invalidInputError:
            
            print 'Invalid Input, try again'
    
    # Get NumTrials
    numTrailsOK = False
    
    while numTrailsOK != True:

        try:
            
            numTrials = userInput.getNumTrials()
            numTrailsOK = userInput.checkNumTrials(numTrials)
        
        except KeyboardInterrupt:
    
            exit('Exiting')
            
        except userInput.invalidInputError:
            
            print 'Invalid Input, try again'
        
    ###########################################################################
    # Run Simulation
    ###########################################################################
        
    fileName = 'results.txt'
    
    try:
        resultsFile = open(fileName, 'w')
    except IOError:
        print('error')
        exit()

    for numShares in positions:
        
        denom = 1000 / numShares
        
        # Simulate Payout
        payout, initialCapital = simulation.simulateInvestmentPayout(denom, numShares,numTrials, pWin)
        
        # Calculate Return
        simDailyRet = simulation.calculateDailyRet(payout, initialCapital)
        
        # Generate Labels for Histogram (title, x/y axis)
        histLabel = plotting.generateLabels(denom, numShares, numTrials)
        
        # Generate Histogram
        plotting.makeHistogram(simDailyRet, histLabel)
        
        # Save Histogram
        plotting.saveHistogramAsPDF(histLabel['fileName'])
        
        # Write to text file with summary statistics
        resultsFile.write(histLabel['titleTxt'] + '\n' + 'mean :' + str(round(simDailyRet.mean(),4)) +
                            '\n' + 'stdev: ' + str(round(simDailyRet.std(),4)) + '\n\n')

if __name__ == '__main__':   
        main()
    
