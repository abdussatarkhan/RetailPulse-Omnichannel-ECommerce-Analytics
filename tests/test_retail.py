import os
import pandas as pd

def test_retail_data():
    assert os.path.exists('data/fact_orders.csv')
    df = pd.read_csv('data/fact_orders.csv')
    assert len(df) > 0
    assert df['gross_sales'].sum() > 0
