class Human:
  def __init__(self, first_name, gender,
    location, ethnicity, hobbies):
    self.first_name = first_name
    self.gender = gender
    self.location = location
    self.ethnicity = ethnicity
    self.hobbies: List[str] = hobbies

    self.energy: float = 1.0 # 0=tired; 1=awake
    self.alive = True

>  def eat(self): ...
>  def sleep(self): ...
>  def code(self): ...

plasmike = Human(
  first_name = "Mike",
  gender = "male",
  location = "Germany",
  ethnicity = "Croatian",
  hobbies = ["Programming", "Electronics", "High Voltage",
    "Volleyball", "Swimming"])

while plasmike.alive:
  plasmike.eat()
  plasmike.sleep()
  plasmike.code()
