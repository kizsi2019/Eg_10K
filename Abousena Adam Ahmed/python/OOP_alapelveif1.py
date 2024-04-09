class Diák:
    def __init__(self, name, class_name):
        self.name = name
        self.class_name = class_name

    def bemutatkozás(self):
        return f"Szia, a nevem {self.name}, és a(z) {self.class_name} osztályba járok."

class Tanár:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def bemutatkozás(self):
        return f"Szia, a nevem {self.name}, {self.subject} szakos tanár vagyok."

student1 = Diák("Kiss Péter", "10.A")
teacher1 = Tanár("Horváth Zita", "biológia-kémia")
teacher2 = Tanár("Schmidt Emil", "matematika")

print(student1.bemutatkozás())
print(teacher1.bemutatkozás())
print(teacher2.bemutatkozás())