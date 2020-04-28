#!/usr/local/bin/python3

import sys
sys.path.append('/Users/vk/MachineLearning/PythonModules/')
from YahooFinance_EOD import extractEODValue as yfin
import pandas as pd
import multiprocessing
from datetime import datetime 

def storeInFile(df):
    destDir = '/Users/vk/MachineLearning/Stocks/data/INTRADAY_EOD_RETURN/'    
    today = datetime.today().strftime('%Y-%m-%d')
    destFile = str(destDir) + str(today) + '.csv'
    
    df.to_csv(destFile, index=False)


if __name__ == '__main__':
    
    symbolsDF = pd.read_csv('/Users/vk/Desktop/SchoolAndResearch/StockResearch/COMMON_CONFIG/stocks.csv')
    etfDF = pd.read_csv('/Users/vk/Desktop/SchoolAndResearch/StockResearch/COMMON_CONFIG/ETF.csv')
    symDF = pd.DataFrame()
    
    symDF = symbolsDF[~symbolsDF['symbol'].isin(etfDF['symbol'])].dropna()
    symbols = list(symDF['symbol'])
    
    p = multiprocessing.Pool(processes = multiprocessing.cpu_count()-1)
    async_result = p.map_async(yfin.OneDayReturn, symbols)
    p.close()
    p.join() 
    
    res = [] 
    for val in async_result.get(): 
        if val != None : 
            res.append(val)

    df = pd.DataFrame(res, columns=['Stock', 'TradeDate', 'HighLowReturnUSD', 'HighLowReturnPercentage', 'CloseOpenReturnUSD', 'CloseOpenReturnPercentage'])
    storeInFile(df)
