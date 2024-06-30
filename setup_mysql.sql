-- Create a MySQL server database for BrainFlip

CREATE DATABASE if NOT EXISTS brainflip_db;
CREATE USER if NOT EXISTS 'brainflipuser'@'localhost' IDENTIFIED BY 'brainflip2024';
GRANT USAGE ON *.* TO 'brainflipuser'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'brainflipuser'@'localhost';
GRANT ALL PRIVILEGES ON `brainflip_db`.* TO 'brainflipuser'@'localhost';

FLUSH PRIVILEGES;
