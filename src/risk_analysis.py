# src/risk_analysis.py
import pandas as pd

def analyze_risk(input_path, output_path):
    df = pd.read_csv(input_path, parse_dates=['timestamp'])

    df['flag_large_amount'] = df['amount'] > 10000
    df['flag_foreign'] = df['is_foreign'] & (df['amount'] > 5000)

    df['hour'] = df['timestamp'].dt.hour
    df['date'] = df['timestamp'].dt.date
    agg = df.groupby(['account_id', 'date', 'transaction_type']).size().reset_index(name='daily_count')
    df = df.merge(agg, on=['account_id', 'date', 'transaction_type'])

    df['flag_structuring'] = (df['transaction_type'] == 'Withdrawal') & (df['daily_count'] > 5)
    df['risk_score'] = df[['flag_large_amount', 'flag_foreign', 'flag_structuring']].sum(axis=1)

    df.to_csv(output_path, index=False)
    return df
