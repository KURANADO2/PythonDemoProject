import os


class EmployeeInfo(object):
    def __init__(self):
        self.path = 'employee.txt'

    def add_employee(self, emp):
        if os.path.exists(self.path):
            with open(self.path, 'a') as file:
                file.write(emp[0] + '\n' + emp[1] + '\n')
                file.write('-'*10 + '\n')
        else:
            print('File does not exist')

    def count_employee(self):
        count = 0
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                for line in file:
                    if line == '-'*10 + '\n':
                        count += 1
        else:
            print('File does not exist')
        print('Count: ', count)

    def find_employee(self, emp_code):
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                for line in file:
                    if line == emp_code + '\n':
                        print(line)
                        print(file.readline())
                        print(file.readline())
        else:
            print('File does not exist')


if __name__ == '__main__':
    code = input('Code:')
    name = input('Name:')
    emp = [code, name]
    employeeInfo = EmployeeInfo()
    employeeInfo.add_employee(emp)
    employeeInfo.count_employee()
    search_code = input('code: ')
    employeeInfo.find_employee(search_code)
