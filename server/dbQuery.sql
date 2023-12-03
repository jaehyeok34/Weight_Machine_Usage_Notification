DROP Table sensor_data

CREATE TABLE sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor VARCHAR(255) NOT NULL,
    sensor_signal BOOLEAN NOT NULL,
    sensor_value FLOAT,
    save_date VARCHAR(255) NOT NULL
);

SELECT * FROM sensor_data