import pandas as pd


if __name__ == '__main__':

    df = pd.read_csv('/Users/craighall/dev/smokecity/daily_aqi_by_cbsa_2018.csv', parse_dates=[2])

    print(df.head())
    print(df.columns)
    print(df.shape)
    print(df.info())
    print(df.iloc[0,2])