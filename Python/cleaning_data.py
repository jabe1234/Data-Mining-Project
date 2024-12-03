import pandas as pd

def cleanData(file_name):
    # open the file
    df1 = pd.read_csv('data/country_vaccinations.csv')
    # create new file
    # read headers / write to new file
    # read each line:
        # read country