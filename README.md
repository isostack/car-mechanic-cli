# 🧰 Car Mechanic CLI Tool

A multi-language command-line application built for a **Linux Systems Programming class**, combining **Bash, Python, Perl, and AWK** to create an interactive automotive database utility.

This tool allows users to:
- Initialize and populate an SQLite database from a CSV file  
- Query car information (oil type, recalls, drivetrain, horsepower, etc.)  
- Search using AWK  
- Generate HTML summaries using Perl  
- Log all system operations (disk usage, memory stats, etc.)

---

## 🏗️ Project Structure

```
car-mechanic-cli/
├── app.sh                # Main entry point (setup + launch)
├── access_db.py          # CLI interface & database access logic
├── create_db.sh          # Creates SQLite database from CSV
├── generate_html.pl      # Generates HTML reports per vehicle
├── search_with_awk.sh    # Performs pattern search using AWK
├── Car_Models.csv        # Source data for import
└── results/              # Logs and HTML outputs are stored here
```

---

## ⚙️ Setup & Execution

### **1. Requirements**
Make sure the following are installed:
- **bash**
- **sqlite3**
- **python3**
- **perl**
- **awk**

You can verify these with:
```bash
bash --version
sqlite3 --version
python3 --version
perl --version
awk --version
```

---

### **2. Make the Scripts Executable**
If you cloned or downloaded the project, ensure executable permissions:
```bash
chmod +x app.sh create_db.sh access_db.py generate_html.pl search_with_awk.sh
```

---

### **3. Run the Program**
Simply execute the main script:
```bash
./app.sh
```

This will:
- Initialize the `results/` directory and `log.txt`
- Display system diagnostics (date, uptime, disk/memory usage)
- Prepare and clean up CSV files
- Create the SQLite database
- Launch the interactive CLI (`access_db.py`)

---

## 🧩 Interactive Menu Features

When `access_db.py` runs, it opens a CLI-driven menu system:

### **Main Menu**
```
MAIN MENU - AUTOMOTIVE SOLUTIONS
1. Enter Your Car
2. View Database
3. Search Database with AWK
4. Exit
```

- **1. Enter Your Car** → Input make & model, then view:
  - Oil capacity  
  - Oil type  
  - Open recalls  
  - Detailed car specs  
  - Generate HTML summary (Perl output saved in `results/`)

- **2. View Database** → Lists all car entries  
- **3. Search Database with AWK** → Case-insensitive text search in the CSV  
- **4. Exit** → Clean exit  

---

## 📊 Data Import Logic

`create_db.sh` converts `Car_Models.csv` into an SQLite table:
```bash
sqlite3 car_repair.db
```

**Schema Example:**
| Field | Type | Description |
|-------|------|-------------|
| Company | VARCHAR(15) | Manufacturer name |
| Model | VARCHAR(20) | Vehicle model |
| Horsepower | VARCHAR(8) | Engine HP |
| Torque | VARCHAR(12) | Engine torque |
| Transmission_Type | VARCHAR(35) | Manual/Automatic |
| Drivetrain | VARCHAR(8) | FWD/RWD/AWD |
| Fuel_Economy | VARCHAR(40) | MPG range |
| Model_Year_Range | VARCHAR(20) | Years available |
| Engine_Type | VARCHAR(20) | Engine family |
| Oil_Type | VARCHAR(5) | SAE grade |
| Oil_Capacity | VARCHAR(50) | Oil fill volume |
| Open_Recalls | CHAR(149) | Recall summary |

---

## 🌐 HTML Generation (Perl)

When selecting **“Generate HTML with Perl”**, the script:
1. Reads all key car fields.
2. Constructs an HTML page.
3. Saves it to:
   ```
   results/output.html
   ```
   (Automatically increments filename if one already exists.)

Example Output:
```html
<html>
  <head><title>Toyota Corolla Information</title></head>
  <body>
    <h1>Toyota Corolla</h1>
    <table border="1">
      <tr><th>Horsepower</th><td>139</td></tr>
      <tr><th>Torque</th><td>126</td></tr>
      <tr><th>Transmission Type</th><td>CVT</td></tr>
      <tr><th>Oil Capacity</th><td>4.4 qt</td></tr>
    </table>
  </body>
</html>
```

---

## 🔍 AWK Search Utility

The `search_with_awk.sh` script performs a flexible, case-insensitive substring search on the CSV:

```bash
./search_with_awk.sh "Ford"
```

**Output:**
```
Ford Mustang
Ford F-150
```

If no matches are found:
```
No information found for the specified make or model.
```

---

## 🧾 Logging

Every system and database setup action is logged to:
```
results/log.txt
```

The log includes:
- Directory creation  
- File permissions  
- Disk & memory usage  
- CSV cleanup  
- Uptime and system stats  

Example snippet:
```
RUN BASH COMMANDS...
Current date and time: Sun Oct 27 01:32:54 PDT 2025
Current directory: /home/user/car-mechanic-cli
Displaying disk usage:
Filesystem      Size  Used Avail Use% Mounted on
...
```

---

## 🧩 Technologies Used

| Language | Purpose |
|-----------|----------|
| **Bash** | Environment setup, logging, permissions |
| **Python (SQLite3)** | CLI interface, database operations |
| **Perl** | HTML file generation |
| **AWK** | Efficient substring searching |
| **SQLite3** | Local data storage |
