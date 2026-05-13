def create_features(df):

    # Time-based features
    df['Hour'] = df.index.hour
    df['Day'] = df.index.day
    df['Month'] = df.index.month
    df['Weekday'] = df.index.weekday

    # Rolling statistics
    df['Rolling_Mean_24'] = (
        df['Global_active_power']
        .rolling(window=24)
        .mean()
    )

    df['Rolling_STD_24'] = (
        df['Global_active_power']
        .rolling(window=24)
        .std()
    )

    # Deviation feature
    df['Deviation'] = (
        df['Global_active_power']
        - df['Rolling_Mean_24']
    )

    # Remove rolling NaN rows
    df = df.dropna()

    return df