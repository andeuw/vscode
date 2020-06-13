summe = 0
for feld in range(64):
    reiskorn = 2**feld
    summe += reiskorn
    print("In Feld {} sind = {} Reiskörner und damit auf dem Schachbrett insgesamt {} Reiskörner".format(feld+1, reiskorn, summe))
