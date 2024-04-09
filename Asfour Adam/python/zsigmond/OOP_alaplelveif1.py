class Diak:
    def __init__(self, nev, class_nev):
        self.nev = nev
        self.class_nev = class_nev

    def greet(self):
        print(f"Szia, a nevem {self.nev}, és a(z) {self.class_nev} osztályba járok.")

class Tanar:
    def __init__(self, nev, subject):
        self.nev = nev
        self.subject = subject

    def greet(self):
        if len(self.subject) > 1:
            subjects = "ok" if len(self.subject) == 2 else "ak"
            print(f"Szia, a nevem {self.nev}, {len(self.subject)} szakos tanár vagyok: {', '.join(self.subject)[:-1]} és {self.subject[-1]}.")
        else:
            print(f"Szia, a nevem {self.nev}, {self.subject[0]} szakos tanár vagyok.")

diakok = [Diak("Kiss Péter", "10.A"), Diak("Nagy Anna", "9.B")]
tanarok = [Tanar("Horváth Zita", ["biológia", "kémia"]), Tanar("Schmidt Emil", ["matematika"])]

for person in diakok + tanarok:
    person.greet()