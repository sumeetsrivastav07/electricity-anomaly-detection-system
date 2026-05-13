import pandas as pd


def load_and_clean_data(file_path):

    # Load dataset
    df = pd.read_csv(
        file_path,
        sep=';',
        na_values=['?'],
        low_memory=False
    )

    # Numeric columns
    numeric_columns = [
        'Global_active_power',
        'Global_reactive_power',
        'Voltage',
        'Global_intensity',
        'Sub_metering_1',
        'Sub_metering_2',
        'Sub_metering_3'
    ]

    # Convert to numeric
    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col],
            errors='coerce'
        )

    # Remove missing values
    df = df.dropna()

    # Create datetime column
    df['Datetime'] = pd.to_datetime(
        df['Date'] + ' ' + df['Time'],
        format='%d/%m/%Y %H:%M:%S'
    )

    # Set datetime index
    df.set_index('Datetime', inplace=True)

    return df