class diak:
    def __init__(self, nev, class_nev):
        self.nev = nev
        self.class_nev = class_nev

    def greet(self):
        print(f"Szia, a nevem {self.nev}, és a(z) {self.class_nev} osztályba járok.")

class tanar:
    def __init__(self, nev, subject):
        self.nev = nev
        self.subject = subject

    def greet(self):
        if len(self.subject) == 1:
            subject_str = f"a(z) {self.subject[0]} szakos tanár"
        else:
            subject_str = f"a(z) {', '.join(self.subject[:-1])} és {self.subject[-1]} szakos tanár"
        print(f"Szia, a nevem {self.nev}, {subject_str} vagyok.")



diak = [
    diak("Kiss Péter", "10.A"),
    diak("Nagy Anna", "9.B"),
]

tanar = [
    tanar("Horváth Zita", ["biológia", "kémia"]),
    tanar("Schmidt Emil", "matematika"),
]

for person in diak + tanar:
    person.greet()