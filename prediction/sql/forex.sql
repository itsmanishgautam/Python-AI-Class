CREATE TABLE IF NOT EXISTS forex_rates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rate_date DATE NOT NULL,
    currency VARCHAR(50) NOT NULL,
    unit INT NOT NULL,
    buy DECIMAL(10, 4) NOT NULL,
    sell DECIMAL(10, 4) NOT NULL,
    source VARCHAR(50) NOT NULL
);

INSERT INTO forex_rates (rate_date, currency, unit, buy, sell, source)
VALUES ('2024-06-24', 'INR (Indian Rupee)', 100, 160.00, 160.15, 'Fixed by Nepal Rastra Bank');

INSERT INTO forex_rates (rate_date, currency, unit, buy, sell, source)
VALUES 
('2024-06-24', 'USD (U.S. Dollar)', 1, 133.36, 133.96, 'Open Market'),
('2024-06-24', 'EUR (European Euro)', 1, 142.60, 143.24, 'Open Market'),
('2024-06-24', 'GBP (UK Pound Sterling)', 1, 168.65, 169.41, 'Open Market'),
('2024-06-24', 'CHF (Swiss Franc)', 1, 149.19, 149.86, 'Open Market'),
('2024-06-24', 'AUD (Australian Dollar)', 1, 88.56, 88.96, 'Open Market'),
('2024-06-24', 'CAD (Canadian Dollar)', 1, 97.37, 97.81, 'Open Market'),
('2024-06-24', 'SGD (Singapore Dollar)', 1, 98.42, 98.86, 'Open Market'),
('2024-06-24', 'JPY (Japanese Yen)', 10, 8.35, 8.38, 'Open Market'),
('2024-06-24', 'CNY (Chinese Yuan)', 1, 18.37, 18.45, 'Open Market'),
('2024-06-24', 'SAR (Saudi Arabian Riyal)', 1, 35.55, 35.71, 'Open Market'),
('2024-06-24', 'QAR (Qatari Riyal)', 1, 36.58, 36.74, 'Open Market'),
('2024-06-24', 'THB (Thai Baht)', 1, 3.63, 3.65, 'Open Market'),
('2024-06-24', 'AED (UAE Dirham)', 1, 36.31, 36.47, 'Open Market'),
('2024-06-24', 'MYR (Malaysian Ringgit)', 1, 28.30, 28.42, 'Open Market'),
('2024-06-24', 'KRW (South Korean Won)', 100, 9.60, 9.65, 'Open Market'),
('2024-06-24', 'SEK (Swedish Kroner)', 1, 12.69, 12.75, 'Open Market'),
('2024-06-24', 'DKK (Danish Kroner)', 1, 19.12, 19.20, 'Open Market'),
('2024-06-24', 'HKD (Hong Kong Dollar)', 1, 17.08, 17.16, 'Open Market'),
('2024-06-24', 'KWD (Kuwaiti Dinar)', 1, 434.54, 436.49, 'Open Market'),
('2024-06-24', 'BHD (Bahrain Dinar)', 1, 353.74, 355.33, 'Open Market');