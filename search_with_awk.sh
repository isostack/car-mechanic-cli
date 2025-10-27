#!/bin/bash

# search_with_awk.sh
# This script searches cars in the Car_Models.csv file using AWK.

if [ $# -ne 1 ]; then
    echo "Usage: $0 <substring>"
    exit 1
fi

substring="$1"

# BEGIN AWK
awk -F, -v substring="$substring" '
BEGIN { 
    found = 0 
}
{
    company = tolower($1)
    model = tolower($2)
    combined = company " " model
    if (company ~ tolower(substring) || model ~ tolower(substring) || combined ~ tolower(substring)) {
        found = 1
        print $1 " " $2
    }
}
END {
    if (!found) {
        print "No information found for the specified make or model."
    }
}
' Car_Models.csv
