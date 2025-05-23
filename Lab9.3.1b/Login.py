import sqlite3

# Construct the SQL query by inserting the user-entered employeeID and password
def make_query(employeeID, password):
  return "SELECT firstname, lastname FROM employees WHERE employeeID = '" + employeeID + "' AND password = '" + password + "'"

# Underline some text
def underline(text):
  return "\033[4m" + text + "\033[0m"

# Highlight some text
def highlight(text):
  return "\033[30;106m" + text + "\033[0m"

# Connect to the database
con = sqlite3.connect('/home/kali/CourseFiles/IntroCybersecurity/chinook.db')
cur = con.cursor()

# Prompt the user for login info
print(underline("Chinook Corp - Login"))
employeeID = input("EmployeeID: ")
password = input("Password:   ")
print()

# Construct the SQL query
query = make_query(employeeID, password)

# Show the SQL query we are about to run, with employeeID and password values highlighted
print(underline("SQLite will run this query:"))
print(make_query(highlight(employeeID), highlight(password)))
print()

# Run the query and Fetch the result
cur.execute(query)
employee_info = (cur.fetchall())

# Print the result
print(underline("SQLite query result:"))
if employee_info:
  for x in employee_info:
    print(x)
else:
  print("Employee not found.")
print()
