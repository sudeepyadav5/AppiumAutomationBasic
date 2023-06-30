class EmployeeDetails:
    def __int__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

    def empdetails(self, name, number, address):
        print("Name :", name)
        print("Number", number)
        print("Address :", address)

    def empName(self):
        print("Employee Name :", self.name)


emp = EmployeeDetails("Sudeep", 29, "Surat")

emp.empdetails("Anil", 7, "India")

emp.empName()