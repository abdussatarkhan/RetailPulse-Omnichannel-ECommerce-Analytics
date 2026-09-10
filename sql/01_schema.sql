-- Star Schema for RetailPulse E-Commerce
CREATE TABLE dim_customer (
    customer_id VARCHAR(32) PRIMARY KEY,
    customer_segment VARCHAR(30), -- Champions, Loyal, At-Risk, Lost
    first_order_date DATE,
    rfm_score INT
);

CREATE TABLE dim_product (
    product_id VARCHAR(32) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    cost_price NUMERIC(10, 2),
    retail_price NUMERIC(10, 2)
);

CREATE TABLE fact_orders (
    order_id VARCHAR(64) PRIMARY KEY,
    customer_id VARCHAR(32) REFERENCES dim_customer(customer_id),
    order_date DATE,
    channel VARCHAR(30),
    gross_sales NUMERIC(10, 2),
    discount_amount NUMERIC(10, 2),
    shipping_cost NUMERIC(10, 2),
    net_margin NUMERIC(10, 2)
);
