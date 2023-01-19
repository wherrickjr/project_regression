import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_zillow_data():
    filename = 'zillow.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('select calculatedfinishedsquarefeet as sqft, bedroomcnt as bedrooms, \
            bathroomcnt as bathrooms, taxvaluedollarcnt as tax_value \
            from properties_2017 as props\
                join predictions_2017 as preds using(parcelid)\
                    where props.parcelid = preds.parcelid and\
                        propertylandusetypeid = 261;', get_connection('zillow'))
        df.to_csv(filename)
        return df

#wrangle.py

def acquire_zillow():
    '''
    This function checks to see if zillow.csv already exists, 
    if it does not, one is created
    '''
    #check to see if telco_churn.csv already exist
    if os.path.isfile('zillow.csv'):
        df = pd.read_csv('zillow.csv', index_col=0)
    
    else:

        #creates new csv if one does not already exist
        df = get_zillow_data()
        df.to_csv('zillow.csv')

    return df

def prep_zillow(df):
    '''
    This function takes in the zillow df
    then the data is cleaned and returned
    '''
    #change column names to be more readable
    df = df.rename(columns={'bedroomcnt':'bedrooms', 
                          'bathroomcnt':'bathrooms', 
                          'calculatedfinishedsquarefeet':'area',
                          'taxvaluedollarcnt':'tax_value'})

    #drop null values- at most there were 9000 nulls (this is only 0.5% of 2.1M)
    df = df.dropna()

    #drop duplicates
    df.drop_duplicates(inplace=True)
    
    #drop outliers

    Q1 = np.percentile(df['tax_value'], 25, interpolation = 'midpoint')
    Q3 = np.percentile(df['tax_value'], 75, interpolation = 'midpoint')
    IQR = Q3 - Q1
    df = df[df['tax_value'] <= Q3 + 1.5 * IQR]
    df = df[df['tax_value'] >= Q1 - 1.5 * IQR]
    # train/validate/test split
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)
    
    return train, validate, test


def wrangle_zillow():
    '''
    This function uses the acquire and prepare functions
    and returns the split/cleaned dataframe
    '''
    train, validate, test = prep_zillow(acquire_zillow())
    
    return train, validate, test
