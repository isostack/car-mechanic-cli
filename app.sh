#!/bin/bash
# app.sh
# This script is what the user will run to start the program.

clear

# Create results directory and initialize log file
if [ -d ./results ]; then
    echo "Directory exists already! Skipping creation" > ./results/log.txt
else 
    mkdir results
    echo "Created results directory" > ./results/log.txt
fi

# Create log file
echo "Creating log file..." >> ./results/log.txt
echo "Log file created and old log wiped" > ./results/log.txt

echo "RUN BASH COMMANDS..." >> ./results/log.txt
echo "" >> ./results/log.txt

# Show date and time
echo "Current date and time: $(date)\n" >> ./results/log.txt
echo "" >> ./results/log.txt

# Show curr directory
echo "Current directory: $(pwd)" >> ./results/log.txt

# List files
echo "Listing files in directory:" >> ./results/log.txt
ls -l >> ./results/log.txt
echo "" >> ./results/log.txt

# Display disk & memory usage
echo "Displaying disk usage:" >> ./results/log.txt
df -h >> ./results/log.txt
echo "Displaying memory usage:" >> ./results/log.txt
free -h >> ./results/log.txt

# Add Permissions
echo "Adding permissions to files..." >> ./results/log.txt
chmod +x access_db.py
chmod +x create_db.sh
chmod +x generate_html.pl
chmod +x search_with_awk.sh

# Remove the old database file
rm -f "car_repair.db"
echo "Removed the old database file" >> ./results/log.txt

# Remove the header line from Car_Models.csv
sed -i '/Company,Model,Horsepower,Torque,Transmission_Type/d' Car_Models.csv
echo "Removed header line from CSV" >> ./results/log.txt

# Display the first 5 lines of Car_Models.csv
echo "Displaying the first 5 lines of Car_Models.csv:" >> ./results/log.txt
head -n 5 Car_Models.csv >> ./results/log.txt

# Check the number of lines in Car_Models.csv
echo "# LINES in Car_Models.csv: $(wc -l < Car_Models.csv)" >> ./results/log.txt
echo "" >> ./results/log.txt

# Word count of Car_Models.csv
echo "Word count of Car_Models.csv:" >> ./results/log.txt
wc -w Car_Models.csv >> ./results/log.txt
echo "" >> ./results/log.txt

# Search for string
echo "Search 'Ford' in Car_Models.csv:" >> ./results/log.txt
grep 'Ford' Car_Models.csv >> ./results/log.txt
echo "" >> ./results/log.txt

# Show uptime
echo "Uptime:" >> ./results/log.txt
uptime >> ./results/log.txt
echo "" >> ./results/log.txt


# =====================================================================

# Run create_db.sh to set up the database
echo "RUN create_db.sh to set up the database..." >> ./results/log.txt
./create_db.sh

# Run access_db.py to start the application
echo "Running access_db.py to start the application..." >> ./results/log.txt
./access_db.py