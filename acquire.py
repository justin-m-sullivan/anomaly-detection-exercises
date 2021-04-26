from env import host, user, password
import pandas as pd

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the CodeUp db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_curriculum_logs():
    '''
    This function reads in the logs table from curriculum_logs on Codeup's Sequel Ace Database
    and joins the cohorts table to return a single dataframe
    '''

    sql_query = '''SELECT *
                FROM logs as l
                LEFT JOIN cohorts as c on l.cohort_id = c.id; 
                '''
    df = pd.read_sql(sql_query, get_connection('curriculum_logs'))

    return df


