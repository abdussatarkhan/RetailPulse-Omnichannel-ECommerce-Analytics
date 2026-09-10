import pandas as pd
import numpy as np
import os

os.makedirs('data', exist_ok=True)
np.random.seed(42)

n_cust = 500
customers = {
    'customer_id': [f'CUST_{i:05d}' for i in range(1, n_cust + 1)],
    'customer_segment': np.random.choice(['Champions', 'Loyal Customers', 'Potential Loyalists', 'At-Risk', 'Hibernating'], n_cust, p=[0.15, 0.25, 0.30, 0.20, 0.10]),
    'rfm_score': np.random.randint(111, 555, n_cust)
}
pd.DataFrame(customers).to_csv('data/dim_customer.csv', index=False)

n_orders = 6000
orders = {
    'order_id': [f'ORD_{i:06d}' for i in range(1, n_orders + 1)],
    'customer_id': np.random.choice(customers['customer_id'], n_orders),
    'channel': np.random.choice(['Online DTC', 'Amazon Store', 'Retail Flagship', 'Mobile App'], n_orders),
    'gross_sales': np.round(np.random.exponential(scale=120, size=n_orders) + 15, 2),
    'discount_amount': np.round(np.random.uniform(0, 20, size=n_orders), 2)
}
df_ord = pd.DataFrame(orders)
df_ord['net_margin'] = np.round((df_ord['gross_sales'] - df_ord['discount_amount']) * 0.42, 2)
df_ord.to_csv('data/fact_orders.csv', index=False)
print("RetailPulse synthetic order records generated in data/")
