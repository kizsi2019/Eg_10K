
#2. rész
def tavolsagok(menetido, sebesseg)-> float:
    return menetido/ 60 * sebesseg

print(tavolsagok(int(input("eltelt idő (perc)")),int(input("sebesség (km/h)"))))

def szerviz(gyartasi_ev:int):
    if gyartasi_ev < 2015:
        print("évente kell szervizbe vinni")
    elif gyartasi_ev < 2021:
        print("2 évente kell szervizelni")
    else:
        print("elég 3 évente vinni")

szerviz(int(input("mikor gyártották le a hajót (év)")))
