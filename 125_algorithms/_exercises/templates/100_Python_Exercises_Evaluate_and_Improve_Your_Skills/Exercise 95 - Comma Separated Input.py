#Create a program that asks the user to input values separated by commas and those values will be stored in a separate line each in a text file

line _ input("Enter values: ")

line_list _ line.split(",")

with open("user_data_commas.txt", "a+") as file:
    ___ i __ line_list:
        file.write(i + "\n")

#Video question -Intermediate
