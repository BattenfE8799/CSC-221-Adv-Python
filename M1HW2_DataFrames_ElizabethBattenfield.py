# Creating and manipulate dataframes
# 9/7/2021
# CSC221 M1HW2 – DataFrame
# Elizabeth Battenfield

import pandas as pd 

def main():
    """ program creating and manipulating dataframes"""
    
    #a)create dictionary of three temperatures reading for each of three people
    tempsDict = {'Maxine': [99,98,100],'James':[97,98,99],'Amanda':[98,98,97]}

    #turn dictionary into a dataframe
    temperatures = pd.DataFrame(tempsDict)
    
    #display dataframe
    print("Temperature Dataframe")
    print(temperatures)
    print()
    
    #b)recreate dataframe with custome indices
    temperatures = pd.DataFrame(tempsDict, index=['Morning','Afternoon','Evening'])
    print("Temperature Dataframe with custome indices")
    print(temperatures)
    print()
    
    #c) select form temperatures colomn of temperature reading for Maxine
    print("Colomn of Temperature Reading for Maxine")
    print(temperatures['Maxine'])
    print()
    
    #d) select from temperatures the row of morning temperature readings
    print("Row of Temperature Readings for Morning")
    print(temperatures.loc['Morning'])
    print()
    
    #e) select from temperatures the rows for morning and evening temp readings
    print("Rows of Temperature Reading for Morning and Evebing")
    print(temperatures.iloc[[0,2]])
    print()
    
    #f) select from temperatures the columns of temp reading for amanada and maxine
    print("Temperature Readings for Amanda and Maxine")
    print(temperatures.loc[['Morning','Afternoon','Evening'], ['Maxine','Amanda']])
    print()
    
    #g) select from temperatures the elements for amanda and maxine in the morning and afternoon
    print("Temperature Readings for Amanda and Maxine in the Morning and Evening")
    print("Amanda: Morning",temperatures.iat[0,2]," Evening:",temperatures.iat[1,2])
    print("Maxine: Morning",temperatures.iat[0,0],"Evening:",temperatures.iat[1,0])
    print()    
    
    #h) use the describe method to produce temperatures' descriptive statistics
    print("Temeratures Dataframe Descriptive Statistics")
    print(temperatures.describe())
    print()     
    
    #i) transpose temperatures
    print("Temperatures Dataframe transposed")
    print(temperatures.T)
    print()    
    
    #j) sort temperatures so that its colomn names are alphabetical
    print("Temperatures Dataframe with alphabetical colomns")
    print(temperatures.sort_index(axis=1))
    print()
    

if __name__=='__main__':
    main()