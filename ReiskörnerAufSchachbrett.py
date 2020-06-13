summe = 0

for feld in range(64):
    reiskorn = 2**feld
    summe += reiskorn
    print("In Feld {} sind = {:>30,} \
    Reiskörner und damit auf dem Schachbrett insgesamt \
    {:>30,} Reiskörner".format(feld+1, reiskorn, summe))

gewicht = summe * 0.25 / 1000000
print()
print('Wenn ein Reiskorn 0,25 Gramm wiegt, \
wiegen die gesammten Reiskörner {:,.0f} \
Tonnen'.format(gewicht))
