class Human:
  def __init__(self, first_name, gender,
    location, hobbies, skills):

    self.first_name = first_name
    self.gender = gender
    self.location = location
    self.hobbies: List[str] = hobbies
    self.skills: List[str] = skills

    self.energy: float = 1.0 # 0=tired; 1=awake
    self.alive = True

>  def eat(self): ...
>  def sleep(self): ...
>  def code(self): ...

plasmike = Human(
  first_name = "Mike",
  gender = "male",
  location = "Germany",
  hobbies = ["Programming", "Electronics","Weightlifting", "Gaming", "3D Art"]
  skills = ["Python", "C++", "C", "Blender", "CAD", "3D Printing"])

while plasmike.alive:
  plasmike.eat()
  plasmike.sleep()
  plasmike.code()
