class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __str__(self):
        return f'Employee(Name: {self.name}, Salary: {self.salary})'


# Example usage
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Adding salaries
total_salary = emp1 + emp2
print(f'Total Salary: {total_salary}')  # Output: Total Salary: 110000

# Subtracting salaries
salary_difference = emp1 - emp2
print(f'Salary Difference: {salary_difference}')  # Output: Salary Difference: -10000

# Comparing salaries
print(f"Is Alice's salary greater than Bob's? {emp1 > emp2}")  # Output: Is Alice's salary greater than Bob's? False
print(f"Is Alice's salary less than Bob's? {emp1 < emp2}")  # Output: Is Alice's salary less than Bob's? True
print(f"Do Alice and Bob have the same salary? {emp1 == emp2}")  # Output: Do Alice and Bob have the same salary? False
