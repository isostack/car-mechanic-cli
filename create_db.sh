#!/bin/bash

# create_db.sh
# This file converts the CSV file into a SQL database.

# Variables
DB="car_repair.db"
TABLE="Car_Models"
CSV="Car_Models.csv" # Can also be the absolute path to the CSV file if we want.

# creating the database and table
sqlite3 $DB <<EOF
CREATE TABLE IF NOT EXISTS $TABLE(
    Company VARCHAR(15),
    Model VARCHAR(20),
    Horsepower VARCHAR(8),
    Torque VARCHAR(12),
    Transmission_Type VARCHAR(35),
    Drivetrain VARCHAR(8),
    Fuel_Economy VARCHAR(40),
    Model_Year_Range VARCHAR(20),
    Engine_Type VARCHAR(20),
    Oil_Type VARCHAR(5),
    Oil_Capacity VARCHAR(50),
    Open_Recalls CHAR(149)
    );

.mode csv
.import $CSV $TABLE
EOF

echo "Table created and data imported"
