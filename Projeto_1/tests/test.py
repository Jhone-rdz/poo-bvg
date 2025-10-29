import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from src.projeto_um import Cliente

cliente1 = Cliente("João Silva", 30, 1000.0)
cliente1.mostrar_informacoes()
cliente1.atualizar_saldo(500.0)

cliente1.mostrar_informacoes()