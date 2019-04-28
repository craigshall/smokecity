import pandas as pd


if __name__ == '__main__':

    # df = pd.read_csv('/Users/craighall/dev/smokecity/daily_aqi_by_cbsa_2017.csv', parse_dates=[2])
    hourly_full_df = pd.read_csv('/Users/craighall/dev/smokecity/SantaRosaHSep-Nov17PM2.5.csv', parse_dates=['Date Local'])
    # print(hourly_full_df.columns)
    hourly_df = hourly_full_df.loc[:,['Datum','AQS Parameter Desc', 'Date Local', '24 Hour Local', 'Sample Measurement']]
    hourly_df.dropna(inplace=True)
    hourly_df['Hour'] = hourly_df['24 Hour Local'].str[0:2].astype(int)
    hourly_df.drop('24 Hour Local', axis=1, inplace=True)

    df1009 = hourly_df.loc[(hourly_df['Date Local'] == pd.to_datetime("2017-10-9"))]
    print(df1009)

    print(hourly_df.head())
    # print(hourly_df.columns)
    # print(hourly_df.describe())
    print(hourly_df.info())
    print(hourly_df['Sample Measurement'].describe())
    print(hourly_df.shape)
    print(hourly_df.tail())
    # print(df.CBSA.value_counts(dropna=False))
    # print(df['CBSA Code'].value_counts(dropna=False))
    # print(df.Date.value_counts(dropna=False))
    # print(df.AQI.value_counts(dropna=False))
    # print(df.Category.value_counts(dropna=False))
    # print(df['Defining Parameter'].value_counts(dropna=False))
    # print(df['Defining Site'].value_counts(dropna=False))
    # print(df['Number of Sites Reporting'].value_counts(dropna=False))
    # print(df.loc[(df['CBSA Code']==38060)])
                  # and df['Date'] in pd.date_range('2018-04','2018-05'))])
    # print(df.loc[(df['AQI'] > 500) & (df['Defining Parameter'] == 'PM2.5')])
    # print(df.loc[(df['AQI'] > 500)])
    # print(df.loc[(df['CBSA'].str.contains("Santa Rosa")) & (df['AQI'] > 80)])
                 # (df['Defining Parameter'] == 'PM2.5')])
    # santa_rosa = hourly_df.loc[(hourly_df['CBSA'].str.contains("Santa Rosa") & (hourly_df['AQI'] > 80))]
    # print(santa_rosa)
    # print(santa_rosa.describe())