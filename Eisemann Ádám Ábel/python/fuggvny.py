
# Függvény definíciója
def festek_kalkulator(x, y):
    '''
    Kiszámolja az adott falfelület festéséhez
    szükséges festék mennyiségét
    '''
    t = x * y
    l = t * 0.13
    return l
    
    
# Függvény hívása
liter = festek_kalkulator(5, 2)
    
# A függvény hívása lehet egy kifejezés része is
ar = festek_kalkulator(5, 2) * 700
    
      

def szamolo(a, b, c=100):
        """
        c alapértelmezett értéke: 100
        """
        return (a+b)*c
    
    
        # alapértelmezett paraméter használata
        print(szamolo(1, 7))
    
        # alapértelmezett paraméter felülírása
        print(szamolo(1, 7, 10000))
    
        # név szerinti paraméter átadás
        print(szamolo(c=10000, a=1, b=7))
    
      



def legnagyobb_kereso(x, *args):
       
    legnagyobb = x
    for szam in args:
        if szam > legnagyobb:
            legnagyobb = szam
    return legnagyobb
    
    
print(legnagyobb_kereso(1, 19, 11, 7, 17))
    
      