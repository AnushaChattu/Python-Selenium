import sys

from day9.packA.emp import Employee

sys.path.append("C:/Users/anush/PycharmProjects/PythonCodeForSelenium/day9/packA")
sys.path.append("C:/Users/anush/PycharmProjects/PythonCodeForSelenium/day9/packB")

#Approach-1
# import emp
# empobj=emp.Employee(101,"John",50000)
# empobj.displayemp()
#
# import stu
# stuobj=stu.Student(102,"David",60000)
# stuobj.displaystu()

#Approach-2
from emp import Employee
empobj=Employee(101,"John",30000)
empobj.displayemp()

from stu import Student
stuobj=Student(102,"David",40000)
stuobj.displaystu()