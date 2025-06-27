# src/clustering.py
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

def apply_dbscan(df):
    features = df[['amount', 'hour']]
    X = StandardScaler().fit_transform(features)
    db = DBSCAN(eps=0.5, min_samples=10).fit(X)
    df['cluster'] = db.labels_
    return df
