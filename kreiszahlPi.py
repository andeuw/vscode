import turtle as tu

lines = 100

with open('pi.txt',"r") as f:
    pi = f.read()

# Länge der (Nachkommastellen-1) und der ersten und letzten 10 Ziffern
print(len(pi))
print(pi[1:11])
print(pi[-11:])

tu.mode('logo')
tu.tracer(False)

for n in range(lines):
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(30)
    
tu.done()
