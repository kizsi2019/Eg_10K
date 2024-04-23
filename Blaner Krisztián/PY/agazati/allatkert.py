class Allatkert:
    def __init__(self,novenyek,allatok):
        self.novenyek = novenyek
        self.allatok = allatok
    def count(self):
        return f"Novenyek: {self.novenyek}\nAllatok: {self.allatok}"
    def createtxt(self):
        with open("allatkert.txt","w",encoding="utf-8") as file:
            file.write(self.count())

sanyikert = Allatkert(73,42)
print(sanyikert.count())
sanyikert.createtxt()