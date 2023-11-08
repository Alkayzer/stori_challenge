CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount FLOAT NOT NULL,
    type ENUM('debit', 'credit') NOT NULL,
    date DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS user_transactions (
    user_id INT,
    transaction_id INT,
    PRIMARY KEY (user_id, transaction_id),
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (transaction_id) REFERENCES transactions (id)
);
