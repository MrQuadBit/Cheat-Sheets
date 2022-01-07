# Given the next data from a company staff :
employees = [
  {
    'id': 345,
    'name': 'Manuel',
    'lastName': 'Torres',
    'age': 25,
    'city': 'Guadalajara'
  },
  {
    'id': 456,
    'name': 'Alicia',
    'lastName': 'Correa',
    'age': 22,
    'city': 'Monterrey'
  },
  {
    'id': 785,
    'name': 'Gael',
    'lastName': 'Rosales',
    'age': 35,
    'city': 'Mexico City'
  },
  {
    'id': 987,
    'name': 'Roberto',
    'lastName': 'Aguilar',
    'age': 22,
    'city': 'Monterrey'
  },
  {
    'id': 103,
    'name': 'Rossana',
    'lastName': 'Cortes',
    'age': 37,
    'city': 'Guadalajara'
  },
  {
    'id': 143,
    'name': 'Mariana',
    'lastName': 'Ortiz',
    'age': 27,
    'city': 'Guadalajara'
  },
]
''' Show on the console the answer to the next questions:
    - Who are the oldest and the youngest members of the crew?
    - How many employees are located by city?
    - A new employee has been hired since the employee with the id '103' has been promoted. Could you please update the staff data to include the new employee and remove the employee who got the promotion?
 New employee ->   id: 1023, name: Karla, lastname: Ramirez, age: 20, city: Mexico City.'''

def main():
  '''
  - Who are the oldest and the youngest members of the crew?
  There are different approaches for this feature
  The first one that I can figure out is to do a loop to iterate over employees to get the oldest, asking 1 by 1 who has a bigger age,
  at the end you end up with the biggest value, this has O(n) complexity
  You can repeat the same process for the youngest member in this way complexity scales to O(2n) doing 2 different functions for each needed output 
  (oldest and youngest),but it breaks the principle DRY repeating code unnecessary
  You can reduce it to only 1 iteration O(n) by asking for both bigger and smaller at the same time but it makes bad code, by keeping it simple (KISS) 
  is not a good practice to have a function that does multiple tasks, also YAGNI says that maybe this single or even both functions are going
  to be used 1 time only so I decided to sort employees based on their age
  The documentation says that the "sorted" function is based on O(N log N) algorithm, this means a slower solution 
  but at least in this case where N is equal to 6, we have O(2 N) = 12 and O(N log N) = 4.6 where our second approach is a better option
  **only for this case is a better option but if the list size grows to more than 100 members is even better to have 2 functions doing similar tasks
  '''
  sorted_employees = sorted(employees, key=lambda x: x['age'], reverse=True)
  oldest_member, youngest_member = sorted_employees[::len(sorted_employees)-1]
  print(f'Oldest member: {oldest_member["name"]} {oldest_member["lastName"]} is {oldest_member["age"]} years old')
  print(f'Youngest member: {youngest_member["name"]} {youngest_member["lastName"]} is {youngest_member["age"]} years old\n')

  '''
  - How many employees are located by city?
  For this feature is needed visiting every member to know where he or she lives, this approach is O(n), to not increase more the complexity
  I decided to use a dictionary to check if already exists the key (the city) and if it is, add 1 employee, otherwise add the new city to the dictionary
  with 1 employee
  '''
  cities = employeesPerCity(employees)
  print(''.join(f'{city} has {num_employees} employees\n' for city, num_employees in cities.items()))

  '''
  - A new employee has been hired since the employee with the id '103' has been promoted. 
  Could you please update the staff data to include the new employee and remove the employee who got the promotion?
  New employee ->   id: 1023, name: Karla, lastname: Ramirez, age: 20, city: Mexico City.

  In this feature we need to mutate the state of employees list, I am not a big fan of this so I decided to create 2 functions 
  (add a new employee and remove an existing employee) each list receives a list and returns a different list with the modifications required

  About complexity, we can do something similar to the first feature, sort employees but now based on the key "id" which give us a complexity of O(N log N) 
  and then by doing a binary search who has a complexity of O(log n) find the required element to remove giving a total of O(n log n + log n) complex,
  but like in the first feature this approach is better only with the actual size of the employees list e.g.
    where n = 6, O(n log n + log n) = 5.44 < O(n) = 6
  but when the list starts to growth the complexity scales up so fast e.g.
    where n = 100, O(n log n + log n) = 202 > O(n) = 100
  **maybe this approach is viable for bigger inputs if the employees list was already sort by id
  
  I compared the past approach with O(n) because there is a more pythonist option using the 'in' operator,
  we can iterate over the employees and then ask if 'id' is 'in' the actual employee 
  the documentation says that only for dictionaries the time complexity is constant O(1)
  and for lists, the complexity is O(n) giving a total of O(n*1)

  so for practicality, I decided to use the second approach
  '''

  new_employee = {'id':1023, 'name':'Karla', 'lastname':'Ramirez', 'age':20, 'city':'Mexico City'}
  promoted_employee_id = 103
  updated_staff = addNewEmployee(new_employee, employees)
  updated_staff = promoteEmployee(promoted_employee_id, updated_staff)

def promoteEmployee(id, employees):
  empl = employees[:]
  for employee in empl:
    if id == employee['id']:
      empl.remove(employee)
      print(f'The member {id} has been promoted and it not longer belongs to the staff')
  return empl

def addNewEmployee(new_employee, employees):
  empl = employees[:]
  empl.append(new_employee)
  print(f'{new_employee["name"]} has been integrated to the staff')
  return empl


def employeesPerCity(employees):
  cities = {}
  for employee in employees:
    if employee['city'] in cities:
      cities[employee['city']] += 1
    else:
      cities[employee['city']] = 1
  return cities


if __name__ == '__main__':
  main()