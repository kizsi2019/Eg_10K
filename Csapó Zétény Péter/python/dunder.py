class Book:
    def __init__(self, title, author, edition):
        self.title = title
        self.author = author
        self.edition = edition

    def __repr__(self):
        return f"Book(author='{self.author}', title='{self.title}', edition={self.edition})"

    def __str__(self):
        return f'{self.author}: {self.title}'

# str - immutábilis (megváltoztathatatlan)
szo_1 = 'alma'
szo_2 = 'alma'

print('szo_1 id:', id(szo_1))  # szo_1 id: 2809970279600
print('szo_2 id:', id(szo_2))  # szo_2 id: 2809970279600

print('szo_1 == szo_2', szo_1 == szo_2)  # szo_1 == szo_2 True
print('szo_1 is szo_2', szo_1 is szo_2)  # szo_1 is szo_2 True
print()


# list - mutábilis (megváltoztatatható)
lista_1 = ['alma', 'körte']
lista_2 = ['alma', 'körte']

print('lista_1 id:', id(lista_1))  # lista_1 id: 2809970241408
print('lista_2 id:', id(lista_2))  # lista_2 id: 2809970681088

print('lista_1 == lista_2', lista_1 == lista_2)  # lista_1 == lista_2 True
print('lista_1 is lista_2', lista_1 is lista_2)  # lista_1 is lista_2 False
  
class Book:
    def __init__(self, title, author, edition):
        self.title = title
        self.author = author
        self.edition = edition

    # egyenlő, ha a cím és szerző egyezik
    # a kiadásnak nem kell egyeznie
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

class School:
    def __init__(self, name):
        self.name = name
        self.level = self.get_level()

    def get_level(self):
        if 'általános iskola' in self.name.lower():
            return 1
        elif 'gimnázium' in self.name.lower():
            return 2
        elif 'egyetem' in self.name.lower():
            return 3
        else:
            return 0

    def __lt__(self, other):
        return self.level < other.level

    def __le__(self, other):
        return self.level <= other.level

    def __gt__(self, other):
        return self.level > other.level

    def __ge__(self, other):
        return self.level >= other.level

    def __repr__(self):
        return self.name

names = ['Berzsenyi Gimnázium', 'Kossuth Általános Iskola', 'Szegedi Tudományegyetem']
schools = []
for name in names:
    schools.append(School(name))

print(f'{schools}')
# [Berzsenyi Gimnázium, Kossuth Általános Iskola, Szegedi Tudomány Egyetem]

schools.sort()
print(f'{schools}')
# [Kossuth Általános Iskola, Berzsenyi Gimnázium, Szegedi Tudomány Egyetem]