from veiculo import Veiculo
from carro import Carro

v1 = Veiculo('rosa', 4, 'ford', 12)

print(v1)
print(type(v1))
v1.abastecer(234)

print(v1.tanque)

car1 = Carro('azul', 'bmw', 30)

car1.abastecer(10)

car1.abastecer(70)