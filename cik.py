#Get the CIK of a ticker from the downloaded cik.csv file
#cik.csv is a tab delimited file with all tickers and CIKs

#imports
import pandas as pd

#location of cik.csv
cikDir = 'cik.csv'

#read cik.csv as a pandas DataFrame
ciksDF = pd.read_csv(cikDir, delimiter='\t', header=None)

#set the column with all the tickers as the index
ciksDF = ciksDF.set_index(0)


#function to return CIK of a ticker
def getCIK(ticker):
    #return CIK if it exists
    try:
        return int(ciksDF.loc[ticker.lower(), 1])

    #return None there's no CIK for the ticker
    except:
        return None