class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLangauge(self):
        print(f"Out of all the languages here is your langauge: {self.language}")        

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language}langauge")

a = Employee()
b = Programmer()

b.show()
b.printLangauge()
b.showLanguage()