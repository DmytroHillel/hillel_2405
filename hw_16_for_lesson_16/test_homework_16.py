from pytest import mark


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

    def developer_team_lead_presentation(self):
        pass


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

    def developer_team_lead_presentation(self):
        return f"name: {self.name}, \nsalary: {self.salary}, \nprogramming_language: {self.programming_language}"


team_lead = TeamLead('John', 1500, 'QA', 'Python', 15)
print(team_lead.developer_team_lead_presentation())


@mark.parametrize("attribute", ['name', 'salary', 'department', 'programming_language', 'team_size', 'another'],
                  ids=['test1', 'test2', 'test3', 'test4', 'test5', 'test6'])
def tc_name_attribute(attribute):
    assert hasattr(team_lead, attribute), f"Атрибут {attribute} не існує"



