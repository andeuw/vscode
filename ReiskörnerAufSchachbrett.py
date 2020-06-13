import matplotlib.pyplot as plt

summe = 0
feldliste = []

for feld in range(64):
    reiskorn = 2**feld
    feldliste.append(reiskorn)
    summe += reiskorn
    print(f"In Feld {feld+1} sind = {reiskorn:>30,} \
    Reiskörner und damit auf dem Schachbrett insgesamt \
    {summe:>30,} Reiskörner")

gewicht = summe * 0.025 / 1000000
print()
print(f'Wenn ein Reiskorn 0,025 Gramm wiegt, \
wiegen die gesammten Reiskörner {gewicht:,.0f} Tonnen')

plt.plot(feldliste)
plt.show()
