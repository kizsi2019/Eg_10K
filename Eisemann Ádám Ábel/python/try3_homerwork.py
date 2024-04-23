#Hozz létre egy szöveges állományt, amely tartalmaz két számot egymástól tabulátorral elválasztva! Írj egy programot, amely beolvassa a fájl tartalmát, és a képernyőn megjeleníti a két szám hányadosát! A programot készítsd fel az esetleges hibalehetőségekre, a felhasználó pedig kapjon a hibának megfelelő figyelmeztető üzenetet ilyen esetben!
def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readline().strip().split('\t')
            num1, num2 = map(float, data)
            return num1, num2
    except Exception as e:
        print(f"Hiba történt a fájl olvasása közben: {e}")
        return None, None

def calculate_and_display_ratio(num1, num2):
    try:
        ratio = num1 / num2
        print(f"A két szám hányadosa: {ratio}")
    except Exception as e:
        print(f"Hiba történt a hányados számítása közben: {e}")

filename = "szamok.txt"
num1, num2 = read_numbers_from_file(filename)
if num1 is not None and num2 is not None:
    calculate_and_display_ratio(num1, num2)
