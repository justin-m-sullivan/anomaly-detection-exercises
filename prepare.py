import os
import pandas as pd

def prep_access_logs(df):
    '''
    This function takes in the dataframe containing access logs
    for the Codeup Curriculum and prepares it for analysis by:
    
    - Concatenting the date and time columns to a dt column and setting is as a datetime index
    - Filling the nulls in co_hort with 0
    
    It returns a prepared dataframe.
    '''
    
    #Create a datetime column by concatenating date and time
    df['dt'] = df['date'] + ' ' + df['time']
    
    #Drop date and time columns
    df.drop(columns={'date', 'time'}, inplace=True)
    
    #Convert dt to datetime object
    df.dt = pd.to_datetime(df.dt)
    
    #set dt as index
    df = df.set_index('dt')
    
    #Set columns with date values as datetime dtypes
    df.created_at = pd.to_datetime(df.created_at, unit='ns')
    df.updated_at = pd.to_datetime(df.updated_at, unit='ns')
    df.start_date = pd.to_datetime(df.start_date, unit='ns')
    df.end_date = pd.to_datetime(df.end_date, unit='ns')
    
    #Fill nulls in co_hort id 
    df.cohort_id = df.cohort_id.fillna('0')
    
    #Drop remaining uncessary/duplicated columns
    df.drop(columns={'id', 'deleted_at', 'program_id', 'slack'}, inplace=True)
    
    return df