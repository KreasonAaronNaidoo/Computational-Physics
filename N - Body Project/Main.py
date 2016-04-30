import NBody


system = NBody.N_Body()

for x in range(1,101,1):

    system.add(5, x, 10)

print
print
print system.tot_pot_energy()



