import random
 
kitalalando = random.randint(1, 10)

tipp = 0

def eltalalta(tipp, kitalalando):
   return tipp == kitalalando

def tipp_bekero():
   tipp = int(input("Kérlek add meg a tiped: "))
   return tipp

def main():
   global tipp
   tipp_szamlalo = 0

   print("Tippelj, amíg el nem találod a számomat!")

   while True:
       tipp = tipp_bekero()
       tipp_szamlalo += 1

       if eltalalta(tipp, kitalalando):
           print(f"Gratulálok! Eltaláltad a számomat ({kitalalando})")
           print(f"A tipped száma: {tipp_szamlalo} alkalommal sikerült.")
           break
       elif tipp < kitalalando:
           print("Próbáld újra!")
       else:
           print("Próbáld újra!")

if __name__ == "__main__":
   main()