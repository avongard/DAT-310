"""
    Author: Michael Portegello
    Class: DAT-310
    Assignment: Assignment 2

    Certification of Authenticity:
    I certify that this is entirely my own work, except where I have given
    fully-documented references to the work of others. I understand the definition
    and consequences of plagiarism and acknowledge that the assessor of this
    assignment may, for the purpose of assessing this assignment:
    - Reproduce this assignment and provide a copy to another member of academic
    - staff; and/or Communicate a copy of this assignment to a plagiarism checking
    - service (which may then retain a copy of this assignment on its database for
    - the purpose of future plagiarism checking)

    About the data set:
    Link to .csv file (https://www.kaggle.com/datasets/zedataweaver/global-salary-data/)
    The dataset contains a list of 222 countries along with their continent and average monthly saleries in USD

    About the code:
    The code is designed to calculate 9 different equations based on the average monthly salaries of the countries.
    Those equations are, minimum value, maximum value, median, mode, mean, standard deviation, variance, ascending, descending order.
"""

# Imports
import csv


# Menu
def menu():
    print("Salary Data by Country")
    print("[1] Minimum")
    print("[2] Maximum")
    print("[3] Median")
    print("[4] Mode")
    print("[5] Mean")
    print("[6] Standard Deviation")
    print("[7] Variance")
    print("[8] Ascending Order")
    print("[9] Descending Order")
    print("[Q] Quit")


# Main
def main():
    while True:
        menu()
        choice = input("Enter an option 1-9 or press 'q' to quit:")

        if choice == '1':
            minimum()
        elif choice == '2':
            maximum()
        elif choice == '3':
            median()
        elif choice == '4':
            mode()
        elif choice == '5':
            mean()
        elif choice == '6':
            standard_deviation()
        elif choice == '7':
            variance()
        elif choice == '8':
            ascending()
        elif choice == '9':
            descending()
        elif choice == 'q' or 'Q':
            print("Exiting the program.")
            break
        else:
            print("Not a valid option.")


def minimum():
    # Specify .csv path
    csv_path = 'salary_data.csv'
    minimum_average_salary = float(1)  # Variable to be updated
    country_with_minimum = ''  # Variable to be updated

    # Syntax for reading a CSV file: https://earthly.dev/blog/csv-python/
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country = row['country_name']
            salary = float(row['average_salary'])

            # Check if row minimum is less then variable
            if salary < minimum_average_salary:
                minimum_average_salary = salary
                country_with_minimum = country

    print(f"Minimum Average Salary: {minimum_average_salary}")
    print(f"The minimum average salary is: {country_with_minimum}")
    input("Press Enter to continue...")

def maximum():
    # Specify .csv path
    csv_path = 'salary_data.csv'
    maximum_average_salary = float(1)  # Variable to be updated
    country_with_maximum = ''  # Variable to be updated

    # Syntax for reading a CSV file: https://earthly.dev/blog/csv-python/
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country = row['country_name']
            salary = float(row['average_salary'])

            # Check if row minimum is greater then variable
            if salary > maximum_average_salary:
                maximum_average_salary = salary
                country_with_maximum = country

    print(f"Minimum Average Salary: {maximum_average_salary}")
    print(f"The minimum average salary is: {country_with_maximum}")
    input("Press Enter to continue...")

def median():
    # Specify .csv path
    csv_path = 'salary_data.csv'
    average_salary = []  # List containing the average salary of each country

    # Syntax for reading a CSV file: https://earthly.dev/blog/csv-python/
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            salary = float(row['average_salary'])
            average_salary.append(salary)

    # Sort the list of average salary
    sorted_average_salary = sorted(average_salary)
    # Calculate median from sorted list
    median_average_salary = sorted_average_salary[len(sorted_average_salary) // 2]

    print(f"The median average salary is: {median_average_salary}")
    input("Press Enter to continue...")

def mode():
    # Specify .csv path
    csv_path = 'salary_data.csv'
    minimum_average_salary = float(1)  # Variable to be updated
    maximum_average_salary = float(1)  # Variable to be updated

    # Syntax for reading a CSV file: https://earthly.dev/blog/csv-python/
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country = row['country_name']
            salary = float(row['average_salary'])

            # Check if row minimum is less then variable
            if salary < minimum_average_salary:
                minimum_average_salary = salary
                country_with_minimum = country

            # Check if row maximum is greater then variable
            if salary > maximum_average_salary:
                maximum_average_salary = salary
                country_with_maximum = country

    # Calculate mode
    mode = maximum_average_salary - minimum_average_salary

    print("Mode Average Salary: ")
    input("Press Enter to continue...")

def mean():
    # Specify .csv path
    csv_path = 'salary_data.csv'
    average_salary = []  # List of countries average salary

    # Syntax for reading a CSV file: https://earthly.dev/blog/csv-python/
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            salary = float(row['average_salary'])
            average_salary.append(salary)

    # Calculate mean from the list of average salaries divided by how many countries are on the list
    mean_average_salary = sum(average_salary) / len(average_salary)

    print(f"Mean Average Salary: {mean_average_salary}")
    input("Press Enter to continue...")

def standard_deviation():
    # Specify .csv path
    csv_path = 'salary_data.csv'
    average_salary = []  # List of countries average salary

    # Syntax for reading a CSV file: https://earthly.dev/blog/csv-python/
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            salary = float(row['average_salary'])
            average_salary.append(salary)

    # Calculate the standard deviation from the list of average salaries
    # Steps to finding standard deviation: https://www.scribbr.com/statistics/standard-deviation/
    # Calculate the mean
    mean = sum(average_salary) / len(average_salary)
    # Calculate the standard deviation
    step1 = sum((i - mean) ** 2 for i in average_salary)
    step2 = step1 / len(average_salary)
    sd = step2 ** .05

    print(f"Standard Deviation of Average Salary: {sd}")
    input("Press Enter to continue...")

def variance():
    # Specify .csv path
    csv_path = 'salary_data.csv'
    average_salary = []  # List of countries average salary

    # Syntax for reading a CSV file: https://earthly.dev/blog/csv-python/
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            salary = float(row['average_salary'])
            average_salary.append(salary)

    # Calculate the standard deviation from the list of average salaries
    # Steps to finding variance: https://www.scribbr.com/statistics/standard-deviation/
    # Calculate the mean
    mean = sum(average_salary) / len(average_salary)
    # Calculate variance
    variance = sum((i - mean) ** 2 for i in average_salary) / len(average_salary)

    print(f"Variance of Average Salary: {variance}")
    input("Press Enter to continue...")

def ascending():
    # Specify .csv path
    csv_path = 'salary_data.csv'
    average_salary = []  # List containing the average salary of each country

    # Syntax for reading a CSV file: https://earthly.dev/blog/csv-python/
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            salary = float(row['average_salary'])
            average_salary.append(salary)

    # Sort the list of average salary
    sorted_average_salary = sorted(average_salary)

    print(*sorted_average_salary, sep = "\n")
    input("Press Enter to continue...")


def descending():
    # Specify .csv path
    csv_path = 'salary_data.csv'
    average_salary = []  # List containing the average salary of each country

    # Syntax for reading a CSV file: https://earthly.dev/blog/csv-python/
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            salary = float(row['average_salary'])
            average_salary.append(salary)

    # Sort the list of average salary
    sorted_average_salary = sorted(average_salary, reverse=True)

    print(*sorted_average_salary, sep = "\n")
    input("Press Enter to continue...")


# Start Main
if __name__ == "__main__":
    main()



