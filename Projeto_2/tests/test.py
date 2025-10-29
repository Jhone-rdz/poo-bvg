import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from src.carro import Carro
from src.cliente import Cliente
from src.seguro import Seguro


cliente1 = Cliente("João Silva", "123.456.789-00")

carro1 = Carro(2020, "Toyota", "Corolla", "Branco", "XYZ-1234")

seguro1 = Seguro(
    carro=carro1,
    cliente=cliente1,
    valor=1500.00,
    regencia=True
)


cliente1.exibir_informacoes()
carro1.exibir_detalhes()
print(f"Valor do seguro: R$ {seguro1.valor:.2f}")
print(seguro1.verificar_vigencia())
