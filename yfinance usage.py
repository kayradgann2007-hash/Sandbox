FILE="c:/Users/semah/Desktop/polito year 1/yfinance_info.txt"
FILE2="c:/Users/semah/Desktop/polito year 1/daily_return_script.txt"
FILE3="c:/Users/semah/Desktop/polito year 1/simple_moving_average.txt"
FILE4="c:/Users/semah/Desktop/polito year 1/log_returns.txt"
FILE5="c:/Users/semah/Desktop/polito year 1/volatility.txt"
FILE6="c:/Users/semah/Desktop/polito year 1/RSI.txt"

import yfinance as yf
import matplotlib.pyplot as plt 
import numpy as np

def writefile(filename,dict):
    try:
        with open(filename,"a",encoding="utf-8") as file:
            for key,value in dict.items():
                file.write(f"{key}:{value}\n")
    except OSError as problem:
        print(problem)
        exit(1)

def file_write_script(filename,script):
    try:
        with open(filename,"w",encoding="utf-8") as file:
            file.write(f"{script}\n")
    except OSError as problem:
        print(problem)
        exit(1)
            
def returndict(input):
    dict={}
    for key,value in input.items():
        dict[key]=value
    return dict

def return_doub_dict(input_1,input_2):
    dict1={}
    dict2={}
    for key,value in input_1.items():
        dict1[key]=value
    for key,value in input_2.items():
        dict2[key]=value
    return dict1,dict2

def plotting(dict):
    plt.plot(dict["Close"],color="blue")
    plt.xlabel("Dates")
    plt.xticks(rotation=45)
    plt.ylabel("Close Price",color="blue")
    plt.plot(dict["Open"],color="red")
    plt.ylabel("Open Price",color="red")
    plt.show()

def daily_returns(dict):
    dict["Returns"]=dict["Close"].pct_change()
    return dict["Returns"]

def simple_moving_average(dict):
    dict["SMA_20"]=dict["Close"].rolling(window=20).mean()
    return dict["SMA_20"]

def log_returns(dict):
    dict["Log_Returns"]=np.log(dict["Close"]/dict["Close"].shift(1))
    return dict["Log_Returns"]

def volatility(dict):
    daily_volatility=dict["Returns"].std()
    annual_volatility=daily_volatility*np.sqrt(252)
    return {"Daily Volatily ":daily_volatility,"Annual Volatility":annual_volatility}

def RSI(dict,period=14):
    delta=dict["Close"].diff()
    gain=delta.where(delta>0,0)
    loss=delta.where(delta<0,0).abs()
    avg_gain=gain.rolling(window=period).mean()
    avg_loss=loss.rolling(window=period).mean()
    rs=avg_gain/avg_loss
    rsi=100-(100/(1+rs))
    return rsi

def bollinger_bands(dict,window=20,cof=2):
    ...


def main():
    dat=yf.Ticker("MSFT")
    dict_calend=returndict(dat.calendar)
    dict_apt=returndict(dat.analyst_price_targets)
    file_write_script(FILE,"CALENDER:")
    writefile(FILE,dict_calend)
    file_write_script(FILE,"ANALYST PRICE TARGET")
    writefile(FILE,dict_apt)
    #
    dict_history=returndict(dat.history(period="1mo"))
    print(dict_history)
    #
    file_write_script(FILE2,"DAILY RETURNS:")
    d_returns=returndict(daily_returns(dict_history))
    writefile(FILE2,d_returns)
    #
    file_write_script(FILE3,"SIMPLE MOVING AVERAGE:")
    sma=returndict(simple_moving_average(dict_history))
    writefile(FILE3,sma)
    #
    file_write_script(FILE4,"LOG RETURNS:")
    log_ret=returndict(log_returns(dict_history))
    writefile(FILE4,log_ret)
    #
    vol_dat=(volatility(dict_history))
    file_write_script(FILE5,"VOLATILITY:")
    writefile(FILE5,vol_dat)
    #
    file_write_script(FILE6,"RSI:")
    rsi=returndict(RSI(dict_history))
    writefile(FILE6,rsi)



if __name__=="__main__":
     main()


