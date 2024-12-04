import pandas as pd

def cleanData(file_name):
    # open the file
    df1 = pd.read_csv(file_name)
    # create new file
    
    # read headers / write to new file
    # read each line:
        # read country
        
    # convert to csv
    df2 = df1
    df2.to_csv("cleaned_" + file_name)