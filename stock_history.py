# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:29:58 2020

@author: brand
"""
import robin_stocks as r
import pandas as pd
import csv
import matplotlib.pyplot as plt
import os
import shutil

def login(path):
  with open(path, newline='') as f:
      reader = csv.reader(f)
      row1 = next(reader)  # gets the first line
      r.login(row1[0],row1[1], store_session=True)

def currentOpenStatus(bought, sold):
    objects = ('Bought', 'Sold')
    performance = [round(bought, 2), round(sold, 2)]

    plt.barh(objects, performance)
    
    for index, value in enumerate(performance):
        plt.text(value, index, str(value))
        
    plt.ylabel('Amount')
    plt.title('Current Open Penny Stock Status')
    
def currentReturnStatus(bought, sold):
    objects = ('Bought', 'Sold')
    performance = [round(bought, 2), round(sold, 2)]

    plt.barh(objects, performance)
    
    for index, value in enumerate(performance):
        plt.text(value, index, str(value))
        
    plt.ylabel('Amount')
    plt.title('Current Closed Penny Stock Status')
    

def main():
    
    login("C://login_files//robinHood_Login.csv")
    r.export.export_completed_stock_orders("C://stockHistoryFile//")
    fileName = [filename for filename in os.listdir("C://stockHistoryFile//") if filename.startswith("stock_orders")]
    fileName = "C://stockHistoryFile//" + fileName[0]
    print(fileName)
    data = pd.read_csv(fileName)
    answer = input("Do you want your current stock earnings, including open investments? Yes or no.")
    
    #return stock earnings/spendings including open investments
    if answer.lower() == "yes": 
        #return only sold stocks that were considered a penny stock (under 10 bucks)
        dataBuy = data[(data.side == "buy") & (data.average_price <= 10.00)]
        
        stocksBought = [stock for stock in dataBuy["symbol"]]
        dataSold = data[(data.symbol.isin(stocksBought)) &  (data.side == "sell")]
        
        #return the sum off all bought/sold stock
        valuesBought = dataBuy.quantity * dataBuy.average_price
        valuesSold = dataSold.quantity * dataSold.average_price
        dataBuy['Values'] = valuesBought
        dataSold['Values'] = valuesSold
        totalBought = dataBuy['Values'].sum()
        totalSold = dataSold['Values'].sum()
        
        dataBuy.to_csv(r'C://login_files//bought.csv')
        dataSold.to_csv(r'C://login_files//sold.csv')
    
        currentOpenStatus(totalBought, totalSold)

    #return stock earnings/spendings including ONLY closedye investments  
    else:                
        dataSold = data[(data.side == "sell")]
        stocksSold = [stock for stock in dataSold["symbol"]]
       
        #return only sold stocks that were considered a penny stock (under 10 bucks)
        dataBuy = data[(data.side == "buy") & (data.average_price <= 10.00) & (data.symbol.isin(stocksSold))]
        
        #return the sum off all bought/sold stock
        valuesBought = dataBuy.quantity * dataBuy.average_price
        valuesSold = dataSold.quantity * dataSold.average_price
        dataBuy['Values'] = valuesBought
        dataSold['Values'] = valuesSold
        totalBought = dataBuy['Values'].sum()
        totalSold = dataSold['Values'].sum()
            
        dataBuy.to_csv(r'C://login_files//bought.csv')
        dataSold.to_csv(r'C://login_files//sold.csv')    
        
        currentReturnStatus(totalBought, totalSold)
        
        
    shutil.move(fileName, "C://stockHistoryFile//Archive//")
       

if __name__== "__main__":
   main() 