from dataclasses import dataclass

@dataclass
class Employee():
    name : str
    ID : int
    role : str
e1=Employee(name="lava",ID=52150893,role="Network engineer")
print(e1)
