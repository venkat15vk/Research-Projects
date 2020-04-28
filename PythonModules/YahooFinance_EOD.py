import yfinance as yf

class extractEODValue():

    def __init__(self,stock):
        self.stock = stock


    def MultipleDaysReturn(stock):
        try:
            ticker = yf.Ticker(stock)
            print ("processing ticker - " + str(stock))

            hist = ticker.history(period="30d")
            hist.reset_index(level=0, inplace=True)
            dates = list(hist['Date'])
            
            
            
            
            tday = dates[29]
            tminus1 = dates[28]
            tminus2 = dates[27]
            tminus3 = dates[26]
            
            tminus5 = dates[24]
            tminus10 = dates[19]
            tminus15 = dates[14]
            tminus30 = dates[0]

            
            tminus5close = float(hist.loc[hist['Date'] == tminus5, 'Close'])
            tminus10close = float(hist.loc[hist['Date'] == tminus10, 'Close'])
            tminus15close = float(hist.loc[hist['Date'] == tminus15, 'Close'])
            tminus30close = float(hist.loc[hist['Date'] == tminus30, 'Close'])

            
            tminus3close = float(hist.loc[hist['Date'] == tminus3, 'Close'])
            tminus2close = float(hist.loc[hist['Date'] == tminus2, 'Close'])
            tminus1close = float(hist.loc[hist['Date'] == tminus1, 'Close'])
            tdayclose = float(hist.loc[hist['Date'] == tday, 'Close'])

            
            return1day = tdayclose - tminus1close
            return1day = round((return1day*tminus1close)/100, 3)

            return2day = tdayclose - tminus2close
            return2day = round((return2day*tminus2close)/100, 3)
            
            return3day = tdayclose - tminus3close
            return3day = round((return3day*tminus3close)/100, 3)
            
            return5day = tdayclose - tminus5close
            return5day = round((return5day*tminus5close)/100, 3)
            
            
            return10day = tdayclose - tminus10close
            return10day = round((return10day*tminus10close)/100, 3)
            
                                 
            return15day = tdayclose - tminus15close
            return15day = round((return15day*tminus15close)/100, 3)
            
            
            return30day = tdayclose - tminus30close
            return30day = round((return30day*tminus30close)/100, 3)

            return (stock, tday, return1day, return2day, return3day, return5day, return10day, return15day,return30day)
            
        except:
            print ("Error in MultipleDaysReturn - Not processing, no data for - " + str(stock))

    def OneDayReturn(stock):
        try:
            ticker = yf.Ticker(stock)
            print ("processing ticker - " + str(stock))

            hist = ticker.history(period="2d")
            hist.reset_index(level=0, inplace=True)
            dates = list(hist['Date'])
            tday = dates[0]
            
            closePrice = float(hist.loc[hist['Date'] == tday, 'Close'])
            openPrice = float(hist.loc[hist['Date'] == tday, 'Open'])
            highPrice = float(hist.loc[hist['Date'] == tday, 'High'])
            lowPrice = float(hist.loc[hist['Date'] == tday, 'Low'])
            
            closeOpenReturn = closePrice - openPrice
            highLowReturn = highPrice - lowPrice
            
            highLowReturn = round(highLowReturn,5)
            closeOpenReturn = round(closeOpenReturn,5)
            
            closeOpenReturnPercent = round((closeOpenReturn*openPrice)/100,5)
            highLowReturnPercent = round((highLowReturn*lowPrice)/100, 5)

            return (stock, tday, highLowReturn, highLowReturnPercent, closeOpenReturn, closeOpenReturnPercent )
 

        except:
            print ("Error in OneDayReturn - Not processing, no data for - " + str(stock))      


def find15DayReturn(sym):
        
    try:
        ticker = yf.Ticker(sym)
        print ("processing ticker - " + str(sym))

        hist = ticker.history(period="30d")
        hist.reset_index(level=0, inplace=True)
        
        dates = list(hist['Date'])
        
        startDate = dates[14]
        endDate = dates[29]
        
        startPrice = hist.loc[hist['Date'] == startDate, 'Close'].item()
        endPrice = hist.loc[hist['Date'] == endDate, 'Close'].item()
        
        priceDiffPercent = round(((startPrice-endPrice)/startPrice)*100, 3)
        
        return (sym, priceDiffPercent)

    except:
        print ("Not processing, no data for - " + str(sym))


