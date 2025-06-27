import pandas as pd
import numpy as np
from faker import Faker  # Changed import
import random
import os

def generate_transaction_data(save_path):
    fake = Faker()  # Changed instantiation
    Faker.seed_instance(42)  # Changed seeding method
    np.random.seed(42)
    random.seed(42)

    accounts = [fake.uuid4() for _ in range(1000)]

    data = []
    for _ in range(50000):
        acc = random.choice(accounts)
        amount = round(np.random.exponential(1000), 2)
        type_ = np.random.choice(['Deposit', 'Withdrawal', 'Transfer'], p=[0.4, 0.3, 0.3])
        country = np.random.choice(['US', 'IN', 'DE', 'SG', 'BR', 'RU'])
        is_foreign = country != 'US'
        channel = np.random.choice(['Online', 'ATM', 'Branch'])
        date = fake.date_time_this_year()
        data.append([
            fake.uuid4(), acc, amount, type_, date, country, is_foreign, channel, fake.sentence()
        ])

    df = pd.DataFrame(data, columns=[
        'transaction_id', 'account_id', 'amount', 'transaction_type',
        'timestamp', 'country', 'is_foreign', 'channel', 'description'
    ])
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
