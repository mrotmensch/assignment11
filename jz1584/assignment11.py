from package import *

def main():
    """The program accepts the input of "positions" and "trails" from user , then saves the result of 
    the trials for each position in a histogram with X axis from -1.0 to +1.0, and Y axis as the number 
    of trials with that result  into pdf files with corresponding name. In addition,  the program 
    will also save the mean and the standard deviation of the daily return into a text file called "results.txt"
    """
    x=1
    while x:
        try:
            positions=raw_input('please enter a list of number of shares to buy in eg.[1,10,100,1000]: ')
            checkList(positions)
            
        except KeyboardInterrupt:
            print '\n KeyboardInterrupt, system exit'
            sys.exit()
        
        try:             
            num_trails=raw_input('please enter the number of times to randomly repeat the test:')
            checkTrail(num_trails)
            
        except KeyboardInterrupt:
            print '\n KeyboardInterrupt, system exit'
            sys.exit()
        
            
            
        positions=checkList(positions)
        num_trails=checkTrail(num_trails)
        print "working...."
        stat_to_file(positions,num_trails)
        print"\n Results.txt file has been generated"
        visualizeRet_to_pdf(positions,num_trails)
        print" All histograms have been generated and saved into pdf files \n"
        

if __name__=='__main__':
    main()


    
    
    
    
    