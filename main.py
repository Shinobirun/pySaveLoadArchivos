
import pickle

from clases.Vehiculo import Vehiculo





auto = Vehiculo('Fiat', 120)
f = open('dato.bin', 'wb')
pickle.dump(auto,f)
f.close()

f = open('dato.bin', 'rb')
autete= pickle.load(f)
f.close()

print(autete.getMarca())