import os, sys, csv

# --- Arguments ---
#we need at least 1source, 2destination and 3change we want
if len(sys.argv) < 3:
    print("Proper usage is: reader.py <src> <dst> <change1> <change2> ... Give me input!")
    sys.exit(1) #program closes with error ---(1)--- when the input is invalid

src = sys.argv[1]
dst = sys.argv[2]
changes = sys.argv[3:] #slice the input from index 3 to the end

# --- Check source file ---
if not os.path.isfile(src): #if the file is ---not--- found
    print("Error: source file not found.")

    directory = os.path.dirname(src) or "."
    print("Files in the same directory:")
    for name in os.listdir(directory): #show what files are in the directory
        print(name)

    sys.exit(1)

# --- Read CSV ---
with open(src, newline="") as f: #open the file and automatically close later
    reader = csv.reader(f) #make the csv readable by python in form of rows
    data = list(reader) #change the rows into a normal list.

# --- Apply changes ---
for change in changes:
    parts = change.split(",") #change string form into a list, divided by comma ("3,1,mug" into ["3","1","mug"])

    if len(parts) != 3:
        print(f"Skipping invalid change: {change}")
        continue

    #unpacking the indices into a singular, usable info
    #col = parts[0]
    #row = parts[1]
    #value = parts[2]
    col, row, value = parts

    #column and row info can't be a string
    try:
        col = int(col)
        row = int(row)
    except ValueError:
        print(f"Invalid numbers in change: {change}")
        continue

    #col and row have to point to an existing place
    if row >= len(data) or col >= len(data[row]):
        print(f"Out of range: {change}")
        continue

    #now we can go to the row [row], column [col] and make a change in the place we want
    data[row][col] = value

# --- Display result ---
for row in data:
    print(",".join(row)) #kind of opposite of ".split". We take a list and put it together (["piano","3","7","0"] into piano,3,7,0)

# --- Save CSV ---
#writes all rows to the file, overwriting if the file exists
with open(dst, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)