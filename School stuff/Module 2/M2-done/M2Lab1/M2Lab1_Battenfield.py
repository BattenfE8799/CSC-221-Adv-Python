# CCS-221
# M2Lab1
# Elizabeth Battenfield

import pandas as pd
%matplotlib


def main():
    """ 
    9.12.3 Titanic Dataset
    """
    print('\n9.12.3')
    titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
    pd.set_option('precision', 2)
    print('\nFirst 30 Rows')
    print('\n',titanic.head())
    print('\nLast 30 Rows')
    print('\n',titanic.tail())
    titanic.columns = ['name', 'survived','sex','age','class']
    print('\nCustome Column Names')
    print('\n',titanic.head())

    
    """ 
    9.12.4 Titanic Dataset
    """
    print('\n9.12.4')
    print('\nDescribe()')
    print('\n',titanic.describe())
    print('\nDeterming by comparing and getting True/False\n')
    print((titanic.survived == 'yes').describe())

    """ 
    9.12.5 Titanic Dataset
    """
    print('\n9.12.5')
    print('\nVisulization with Matplotlib')
    histogram = titanic.hist()
    print(histogram)


if __name__ == "__main__":
    main()