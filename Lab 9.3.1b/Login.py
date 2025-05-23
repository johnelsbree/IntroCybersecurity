import sqlite3

# Connect to the database
con = sqlite3.connect('/home/kali/CourseFiles/IntroCybersecurity/chinook.db')
cur = con.cursor()

def bold(text):
  return "\033[1m" + text + "\033[0m"
  
# Prompt the user for login info
print(bold("Chinook Corp - Login"))
employeeID = input("EmployeeID: ")
password = input("Password:   ")
print()

# Construct the SQL query
query = "SELECT firstname, lastname FROM employees WHERE employeeID = '" + employeeID + "' AND password = '" + password + "'"

# Show the SQL query we are about to run
print(bold("SQLite will run this query:"))
print(query)
print()

# Fetch the result
employee_info = (cur.fetchall())

# Print the result
print(bold("SQLite query result:"))
if employee_info:
  for x in employee_info:
    print(x)
else:
  print("Employee not found.")
