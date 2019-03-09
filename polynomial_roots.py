# WORK IN PROGRESS..
# THIS IS NOT READY FOR USE YET
# IT IS NOT COMPLETED, SO IT DOESN'T HAVE FULL FUNCTIONALITY, AND IT'S NOT TRANSLATED TO ENGLISH
# PLEASE BE PATIENT
# -----------------------------------------

najwyzsza_potega = input("Najwyzsza potega twojego wielomianu: ")
wspolczynniki = []

# Sprawdzam czy ilosc elementow napewno jest liczba a nie np tekstem
try:
    najwyzsza_potega = int(najwyzsza_potega)
except ValueError:
    print("[!] Potega musi byc liczba calkowita")
    exit()

if najwyzsza_potega <= 1:
    print("[!] Potega musi byc wieksza niz 1")
    exit()

# Tworze liste przechowywujaca potegi i wpisuje do niej potegi

potegi = []

for i in reversed(range(najwyzsza_potega)):
    potegi.append(i)

# Zapisuje elementy podawane przez uzytkownika, do poprzednio utworzonej tablicy wspolczynniki,
# jednoczesnie sprawdzam czy podawane wspolczynniki, czy tez wyraz wolny sa liczbami


for j in range(1, najwyzsza_potega):
    try:
        if (j < najwyzsza_potega):
            wspolczynniki.append(int(input("Podaj wspolczynnik, wystepujacy przed x, z potega " + str(potegi[j - 1]) + ": ")))
        if (j == (najwyzsza_potega - 1)):
            wspolczynniki.append(int(input("Podaj wyraz wolny: ")))
    except ValueError:
        print("\n[!] Wprowadzone dane nie sa liczba calkowita")

# Tworze nowa tablice dzielniki_wyrazu_wolnego, ktora po nazwie wiadomo co bedzie przechowywac...
# aby znalezc jego dzielniki uzywam petli ponizej

dzielniki_wyrazu_wolnego = []

for k in range (1, wspolczynniki[najwyzsza_potega - 1]):
    if (wspolczynniki[najwyzsza_potega - 1] % k == 0):
        dzielniki_wyrazu_wolnego.append(k)
        dzielniki_wyrazu_wolnego.append(-1 * k)

dzielniki_wyrazu_wolnego.append(wspolczynniki[najwyzsza_potega - 1])
dzielniki_wyrazu_wolnego.append((wspolczynniki[najwyzsza_potega - 1]) * -1)

root = 0
sum = 1
for l in dzielniki_wyrazu_wolnego:
    print("W(" + str(l) + ") = " + str(sum))
    if (sum == 0):
        root = l
        break
    sum = 0
    for m in range(najwyzsza_potega):
        if (m == (najwyzsza_potega - 1)):
            sum += wspolczynniki[m]
        else:
            sum += wspolczynniki[m] * (l ** potegi[m])

print("Dzielniki wyrazu wolnego: " + str(dzielniki_wyrazu_wolnego))
print("Pierwiastek: " + str(root))
