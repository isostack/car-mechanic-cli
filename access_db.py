#!/usr/bin/python3

# access_db.py
# This is the script for accessing the cars database.
# As of now, will need to be in the same directory as the database.

import sqlite3
import subprocess

# Connect to the SQLite database
connection = sqlite3.connect('car_repair.db')
c = connection.cursor()

# VARIABLES ====================
errorMsg = "ERROR: No information found for the specified make and model."

# FUNCTIONS ====================
def validate_car(make, model):
    validation_query = """SELECT 1 FROM Car_Models WHERE LOWER(Company) = LOWER(?) AND LOWER(Model) = LOWER(?)"""
    c.execute(validation_query, (make, model))
    return c.fetchone() is not None

def display_oilcap(make, model):
    oilcap_search = """SELECT Oil_Capacity FROM Car_Models WHERE LOWER(Company) = LOWER(?) AND LOWER(Model) = LOWER(?)"""
    c.execute(oilcap_search, (make, model))
    rows = c.fetchall()
    if rows:
        for row in rows:
            print("Here is the requested information on the oil capacity:\n", row[0])
    else:
        print(errorMsg)

def display_oil_type(make, model):
    oil_type_search = """SELECT Oil_Type FROM Car_Models WHERE LOWER(Company) = LOWER(?) AND LOWER(Model) = LOWER(?)"""
    c.execute(oil_type_search, (make, model))
    rows = c.fetchall()
    if rows:
        for row in rows:
            print("Here is the requested information on the oil viscosity:\n", row[0])
    else:
        print(errorMsg)

def recalls(make, model):
    recall_search = """SELECT Open_Recalls FROM Car_Models WHERE LOWER(Company) = LOWER(?) AND LOWER(Model) = LOWER(?)"""
    c.execute(recall_search, (make, model))
    rows = c.fetchall()
    if rows:
        for row in rows:
            print("Here are the open recalls on that vehicle:\n", row[0])
    else:
        print(errorMsg)

def car_info(make, model):
    car_info_search = """SELECT Horsepower, Torque, Transmission_Type, Drivetrain, Fuel_Economy, Model_Year_Range, Engine_Type FROM Car_Models WHERE LOWER(Company) = LOWER(?) AND LOWER(Model) = LOWER(?)"""
    c.execute(car_info_search, (make, model))
    rows = c.fetchall()
    if rows:
        for row in rows:
            print("Here is the information on the car you selected:")
            print(f"Horsepower: {row[0]}")
            print(f"Torque: {row[1]}")
            print(f"Transmission Type: {row[2]}")
            print(f"Drivetrain: {row[3]}")
            print(f"Fuel Economy: {row[4]}")
            print(f"Model Year Range: {row[5]}")
            print(f"Engine Type: {row[6]}")
    else:
        print(errorMsg)

def display_all_cars():
    all_cars_search = """SELECT Company, Model FROM Car_Models"""
    c.execute(all_cars_search)
    rows = c.fetchall()
    if rows:
        print("\nAll cars in the database:")
        for row in rows:
            print(f"{row[0]} {row[1]}")
    else:
        print("ERROR: No cars found in the database.")

def awk_search(substring):
    try:
        result = subprocess.run(['./search_with_awk.sh', substring], check=True, text=True, capture_output=True)
        print(f"\nAll cars matching {substring}:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {e.stderr}")

def perl_generate_html(make, model):
    sql_search = """SELECT * FROM Car_Models WHERE LOWER(Company) = LOWER(?) AND LOWER(Model) = LOWER(?)"""
    c.execute(sql_search, (make, model))
    rows = c.fetchall()
    if rows:
        row = rows[0]
        data = {
            "Make": row[0],
            "Model": row[1],
            "Horsepower": row[2],
            "Torque": row[3],
            "Transmission_Type": row[4],
            "Drivetrain": row[5],
            "Fuel_Economy": row[6],
            "Model_Year_Range": row[7],
            "Engine_Type": row[8],
            "Oil_Type": row[9],
            "Oil_Capacity": row[10],
            "Open_Recalls": row[11]
        }
        perl_command = ['./generate_html.pl']
        for key, value in data.items():
            perl_command.append(f"{key}={value}")
        try:
            result = subprocess.run(perl_command, check=True, text=True, capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"ERROR: {e.stderr}")
    else:
        print(errorMsg)

# Basic menu for user
def main_menu():
    while True:
        print("\n" + "`"*35)
        print("MAIN MENU - AUTOMOTIVE SOLUTIONS ")
        print("`"*35)
        print("1. Enter Your Car")
        print("2. View Database")
        print("3. Search Database with AWK")
        print("4. Exit")
        print("`"*35)
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            make = input("What is the make of your car? ").strip()
            model = input("What is the model of your car? ").strip()
            if validate_car(make, model):
                car_menu(make, model)
            else:
                print(errorMsg)
        elif choice == '2':
            display_all_cars()
        elif choice == '3':
            substring = input("Enter the car to search for: ").strip()
            awk_search(substring)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("ERROR: Please select a valid option.")

# Submenu
def car_menu(make, model):
    while True:
        print(f"\n{make.upper()} {model.upper()} RECORDS:")
        print("+" + "-"*28 + "+")
        print("| 1. Oil capacity            |")
        print("| 2. Oil type                |")
        print("| 3. Open recalls            |")
        print("| 4. Car information         |")
        print("| 5. Generate HTML with Perl |")
        print("==============================")
        print("| 6. Back to Main Menu       |")
        print("| 7. Exit Program            |")
        print("+" + "-"*28 + "+")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            display_oilcap(make, model)
        elif choice == '2':
            display_oil_type(make, model)
        elif choice == '3':
            recalls(make, model)
        elif choice == '4':
            car_info(make, model)
        elif choice == '5':
            perl_generate_html(make, model)
        elif choice == '6':
            return  # Back to main menu
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("ERROR: Please select a valid option.")

# EXECUTE MAIN
main_menu()

# Close the database connection
connection.close()