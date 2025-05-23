import sqlite3

# Connect to the database
con = sqlite3.connect('/home/kali/CourseFiles/IntroCybersecurity/chinook.db')
cur = con.cursor()

def underline(text):
  return "\033[4m" + text + "\033[0m"

def highlight(text):
  return "\033[93;103m" + text + "\033[0m"

def make_query(employeeID, password):
  return "SELECT firstname, lastname FROM employees WHERE employeeID = '" + employeeID + "' AND password = '" + password + "'"

# Prompt the user for login info
print(underline("Chinook Corp - Login"))
employeeID = input("EmployeeID: ")
password = input("Password:   ")
print()

# Construct the SQL query
query = make_query(employeeID, password)

# Show the SQL query we are about to run
print(underline("SQLite will run this query:"))
print(make_query(highlight(employeeID), highlight(password)))
print()

# Fetch the result
employee_info = (cur.fetchall())

# Print the result
print(underline("SQLite query result:"))
if employee_info:
  for x in employee_info:
    print(x)
else:
  print("Employee not found.")
