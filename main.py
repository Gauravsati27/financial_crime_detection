from src.generate_data import generate_transaction_data
from src.risk_analysis import analyze_risk
from src.clustering import apply_dbscan
import pandas as pd

DATA_PATH = "Data/transactions.csv"
OUTPUT_PATH = "outputs/risk_scores.csv"

def main():
    print("Generating data...")
    generate_transaction_data(DATA_PATH)

    print("Analyzing risk...")
    df = analyze_risk(DATA_PATH, OUTPUT_PATH)

    print("Applying clustering...")
    df = apply_dbscan(df)

    # Filter high risk
    high_risk = df[(df['risk_score'] >= 2) | (df['cluster'] == -1)]
    high_risk.to_csv("outputs/high_risk_transactions.csv", index=False)
    print(f"High-risk transactions: {len(high_risk)}")

if __name__ == "__main__":
    main()
