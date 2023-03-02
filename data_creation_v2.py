from datetime import datetime
from random import randint

# Creates new file with header row and random name based on time.
def create_file():
    file_name = str("generated_sales_data_" + str(datetime.now().strftime("%H%M%S")) + ".csv")
    open(file_name, "x")
    f = open(file_name, "a")
    f.write("OrderId,FirstName,LastName,Date,Product,Count")
    f.close()

    return file_name

# Creates the random data
def create_data(filename):
    data_dic = []
    fruits = ["apple", "orange", "banana"]
    names = ["John", "Bob", "Kyle", "Smith"]
    i = 1
    while i <= 25:
        order_id = i
        first_name = names[randint(0,3)]
        last_name = names[randint(0,3)]
        date = str(randint(1, 28)) + "-" + str(randint(1, 12)) + "-" + str(randint(2000, 2022))
        fruits = {"apple": randint(0,3), 
                 "orange": randint(0,3), 
                 "banana": randint(0,3)}

        for fruit in fruits:
            count = randint(0,5)
            if count != 0:
                data_dic.append({
                    "order_id": order_id,
                    "first_name": first_name,
                    "last_name": last_name,
                    "date": date,
                    fruit: count
                    })
        i+=1

    write_to_csv(filename, data_dic)

# Writes the random data to a file
def write_to_csv(filename, data_dic):
    with open(filename, "a") as f:
        for data in data_dic:
            fruit = check_fruit(str(data.keys()))
            row_data = "\n" + str(data["order_id"]) + "," + data["first_name"] + "," + data["last_name"] + "," + str(data["date"]) + "," + fruit + "," + str(data[fruit])
            f.write(row_data)

# Checks to see which fruit belongs in the row of data
def check_fruit(fruit_string):
    fruits = ["apple", "orange", "banana"]
    for name in fruits:
        if name in fruit_string:
            return name

# Create a file and fill with random data
def start():
    f_name = create_file()
    create_data(f_name)
    return f_name
