# def print_number(start,end):
#     """Print Number
#     args:
#       start: starting number
#       end: ending value
#       return: None
#     """
    
#     for i in range(start,end+1):
#         print(i,end=" ")
        
# print_number(1,190)
# print_number(end = 15, start = 11)

# https://github.com/pythonbykhaja/April24

# set up the folder structure as mentioned above


# import random

# def write_result(principal , rate , result):
#     """this function appends the results to the end of the file 
    
#     """
#     with open("results.csv", "a") as writer:
        
# def read_results():
#     with open("results.txt", "r") as reader: 
# if__name__ = __main__.__name__

# import random
# def write_record():
#       pass  
# def write_random_data():
#       csv_path = "results.csv"
#       for index in range(3):
#             p = random.randint(1000,10000)
#             i = random.randint(6,24)
            




# ### import csv files to read and write the results 

# import csv

# with open('my_file.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
# with open('output.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Name', 'Age', 'Email'])
#     writer.writerow(['Alice', 30, 'alice@example.com'])
#     writer.writerow(['Bob', 25, 'bob@example.com'])
### https://github.com/pythonbykhaja/April24/commit/8c470202de1aebfe041e0300c4d8da4750352b46
import random
import csv
import os

def write_record(path,p,i,t,r):
    # find if file exists
    file_exists = False
    if os.path.exists(path):
        file_exists = True
    with open(path, 'a') as file:
        results_writer = csv.writer(file)
        results_writer.writerow([p,i,t,r])
        
def write_random_data():
    csv_path = "results.csv"
    for index in range(3):
        p = random.randint(1000,10000)
        i = random.randint(6,24)
        t = random.randint(1,10)
        r = random.randint(1000,10000)
        write_record(csv_path,p,i,t,r)

def read_results(file_path):
    with open(file_path, 'r') as reader:
        result_reader = csv.reader(reader,delimiter=',')
        for record in result_reader:
            print(record)

if __name__ == "__main__":
    write_random_data()
    #read_results("results.csv")

