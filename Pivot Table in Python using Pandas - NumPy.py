import pandas as pd
import numpy as np

# piovtFunc will take input an excel file and will give other as output
# Functionality of Piovt Table in python

def pivotFunc(input):
    df = pd.read_excel(input)
    pivot_df = pd.pivot_table(df,index=["PO"], values=["Dzn"],aggfunc=np.sum)
    newFile = pivot_df.to_excel("New_Pivot.xlsx")
    return newFile
userInput = input("Enter Excel File name with Extension:")
pivotFunc(userInput)
