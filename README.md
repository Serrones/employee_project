employee_project

Python --version --> 3.6.1


This project is an usefull example of how to use a web application to create an
employee database, which you can add, list, update and delete any object.

Managing Employees List:

http://127.0.0.1:8000/employee_manager/


Accessing Employees List:

http://127.0.0.1:8000/employee_manager/


Accessing a single employee:

http://127.0.0.1:8000/employee_manager/id_number


-----------############-----------############-----------############-----------


Yet, the project has an Django Rest API to allow other applications access the
Employees DataBase, and manipulate its objects whitout problems.

How to use of Curl in this project:

get all

curl -u "username" -H "Content-Type: application/javascript" "http://127.0.0.1:8000/api/employee/"

get a specific employee

curl -u "username" -H "Content-Type: application/javascript" "http://127.0.0.1:8000/api/employee/id_number/"

post a new employee

curl -u "username" -d "{"name":"NAME", "email":"email@email.com","department":"DEPARTAMENTO"}"
    -H "Content-Type:application/javascript" -X POST "http://127.0.0.1:8000/api/employee/"

update an employee

curl -u "username" -d '{"name":"NAME", "email":"email@email.com", "department":"Department"}'
    -H "Content-Type:application/javascript" -X PUT "http://127.0.0.1:8000/api/employee/id_number/"

delete an object

curl -u "username" -X DELETE "http://127.0.0.1:8000/api/employee/id_number/"
