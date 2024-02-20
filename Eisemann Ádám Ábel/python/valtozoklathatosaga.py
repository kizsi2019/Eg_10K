
    # Local (function) scope
'''''
def negyzet(a):
    print(a)
    return a ** 2


print(negyzet(3))




# Global (module) scope

def negyzet(a):
    print(f'A negyzet függvényen belül: {a}')
    return a ** 2


def kob(a):
    print(f'A kob függvényen belül: {a}')
    return a ** 2


a = 0
print(f'A függvényen kívül: {a}')
print(negyzet(2))
print(kob(3))

 

    # Enclosing (nonlocal) scope

def kulso_fgv():
    szam = 17
        
    def belso_fgv():
        print(f'A belső függvényből {szam}')
        
    belso_fgv()


kulso_fgv()    

# Built-in scope

print(len(dir(__builtins__)))    
''''' 
  

def negyzet(a):
    return a ** 2


def main():
    szam = 17
    print(negyzet(2))


main()
  