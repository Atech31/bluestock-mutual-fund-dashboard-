CREATE TABLE fintech_transactions (
    Transaction_ID VARCHAR(50) PRIMARY KEY,
    Customer_ID VARCHAR(50),
    Order_Date DATE,
    Product_Category VARCHAR(50),
    Transaction_Amount NUMERIC(10, 2),
    Status VARCHAR(20),
    Region VARCHAR(50)
);

COPY fintech_transactions(Transaction_ID, Customer_ID, Order_Date, Product_Category, Transaction_Amount, Status, Region)
FROM 'E:/kunal projects/FinTech_Analytics_Project/fintech_transactions_cleaned.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM fintech_transactions LIMIT 10;