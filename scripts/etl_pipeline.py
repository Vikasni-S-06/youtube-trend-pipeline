import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding='latin-1')
    return df

def clean_data(df):
    df.dropna(inplace=True)
    df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m')
    df['publish_time'] = pd.to_datetime(df['publish_time'])
    return df

def transform_data(df):
    top_channels = df['channel_title'].value_counts().head(10)
    top_videos = df.groupby('title')['views'].max().sort_values(ascending=False).head(10)
    return top_channels, top_videos
