from webhandler import get,post
from model.database import Database
from model.employee import Employee


@get('/')
def index():
    return {
        '__template__': 'employee_list.html'
    }


@get('/services/employees')
def get_employees():
    emps = Database.query_employee()
    return dict(employees=emps)


@get('/ui/employees/add')
def ui_add_employee():
    return {
        '__template__': 'add_edit_employee.html',
        'id': '',
        'action': '/services/employees'
    }


@post('/services/employees')
def save_employee(*, code, name):
    emp = Employee(code, name)
    Database.save_employee(emp)


@get('/ui/employees/edit')
def ui_edit_employee(*, id):
    return {
        '__template__': 'add_edit_employee.html',
        'id': id,
        'action': '/services/employees/%s' % id
    }


@get('/services/employees/{id}')
def get_employee(*, id):
    emp = Database.query_employee_by_id(id)
    print(emp)
    return dict(id=emp[0], code=emp[1], name=emp[2])


@post('/services/employees/{id}')
def update_employee(*, id, code, name):
    emp = Employee(code, name)
    emp.id = id
    Database.update_employee(emp)


@post('/services/employees/{id}/delete')
def delete_employee(*, id):
    Database.delete_employee(id)
