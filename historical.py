import pandas_datareader.data as web
import os
import datetime
import time

def download_data(tickers,start,end,all_data=False):
    count = 1
    if all_data==True:
        end = datetime.datetime.now()
        end = '%s-%s-%s' % (end.month,end.day,end.year)
        start = '03-25-2019'

    directory = 'stock_data'
    if not os.path.exists(directory):
        os.makedirs(directory)

    d = {}
    for ticker in tickers:
        filename = directory+'/'+ticker+'.csv'
        d[ticker] = web.DataReader(ticker,"yahoo",start,end)
        d[ticker].to_csv(filename)
        count  = count + 1
        if count % 50 == 0:
            time.sleep(10)
    return

if __name__ == '__main__':
    tickers = ['ATVI','GLUU','GME','NTDOY','ZNGA']
    start = '2016-01-01'
    end = '2016-12-21'
    download_data(tickers,start,end,all_data=True)
