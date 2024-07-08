# python

[link](https://blog.stackademic.com/ultimate-python-cheat-sheet-practical-python-for-everyday-tasks-c267c1394ee8)

[link](https://levelup.gitconnected.com/6-python-string-things-i-regret-not-knowing-earlier-6c777942e8c2?source=email-303c28d3da55-1720046260172-digest.reader-5517fd7b58a6-6c777942e8c2----0-109------------------2bebd417_cfb8_4d3b_adbf_176f2c88cbf3-1)




* common values of [1,4,65,7,890][4,3,7,65,987] using forloop

```python.py
list1 = [1, 4, 65, 7, 890]
list2 = [4, 3, 7, 65, 987]

set1 = set(list1)
set2 = set(list2)

common_values = list(set1 & set2)
print(common_values)


```

* print the Second position  values in each Number [56789,456,89004]

```python.py
numbers = [56789, 456, 89004]

second_positions = []
for number in numbers:
    str_num = str(number)
    if len(str_num) > 1:
        second_positions.append(str_num[1])
    else:
        second_positions.append(None)  # or handle it as you prefer
print(second_positions)

```


* print even strings in "helloworld"

```pop.py
string_list = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

# Use a for loop to iterate through the list indices
for index in range(len(string_list)):
    # Check if the index is even
    if index % 2 == 0:
        # Print the element at the even index
        print(string_list[index])

```

* we have employee details in joson file of eid, name, phone num, city, salary ,,, when I type the eid then I get all info about that eid.
```employee.json
{
    "employees": [
        {
            "eid": "E001",
            "name": "John Doe",
            "phone": "123-456-7890",
            "city": "New York",
            "salary": 70000
        },
        {
            "eid": "E002",
            "name": "Jane Smith",
            "phone": "234-567-8901",
            "city": "Los Angeles",
            "salary": 80000
        },
        {
            "eid": "E003",
            "name": "Emily Davis",
            "phone": "345-678-9012",
            "city": "Chicago",
            "salary": 75000
        }
    ]
}

```
```eid.py
import json

# Load employee data from the JSON file
def load_employee_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['employees']

# Get employee details by eid
def get_employee_details(eid, employees):
    for employee in employees:
        if employee['eid'] == eid:
            return employee
    return None

# Main program
if __name__ == "__main__":
    employees = load_employee_data('employees.json')

    # Input the eid to search for
    search_eid = input("Enter the Employee ID (eid): ")

    # Get and print employee details
    employee_details = get_employee_details(search_eid, employees)
    if employee_details:
        print("Employee Details:")
        print(f"EID: {employee_details['eid']}")
        print(f"Name: {employee_details['name']}")
        print(f"Phone: {employee_details['phone']}")
        print(f"City: {employee_details['city']}")
        print(f"Salary: ${employee_details['salary']}")
    else:
        print(f"No employee found with EID: {search_eid}")

```


* http://k8s api reference docs/google.com

above Url i want to replace "/" with ":" symbol

```url.py
url = "http://k8s/api/reference/docs/google.com"
modified_url = url.replace("/", ":")
print(modified_url)
```
or
```url.py
import re

url = "http://k8s/api/reference/docs/google.com"
modified_url = re.sub(r"/", ":", url)
print(modified_url)
```



* http://k8s api reference docs/google.com I want google.com is out put

```last.py
url = "http://k8s/api/reference/docs/google.com"

# Split the URL by '/'
parts = url.split('/')

# Get the last part (word) after the last '/'
last_word = parts[-1]

# Print the last word
print(last_word)
'''


* strings ["apple","ameerpetaammai","aravaiaarlu","amberpeata"] count the number of "a" s in the each string

```number.py
strings = ["apple", "ameerpetaammai", "aravaiaarlu", "amberpeata"]

for s in strings:
    count_a = s.count('a')
    print(f"Number of 'a's in '{s}': {count_a}")
```


* create one file and insert data inside the file using script
  ```file.py
  # Open a file named output.txt in write mode ('w')
with open('output.txt', 'w') as f:
    # Write some data to the file
    f.write("Hello, world!\n")
    f.write("This is a test file.\n")
    f.write("Writing data to a file.\n")

print("Data has been written to output.txt")
```
