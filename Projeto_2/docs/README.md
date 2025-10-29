
# Sistema de Gerenciamento de Seguros

Este repositório contém uma implementação didática de um pequeno sistema de seguros de veículos.

O objetivo desta versão é ser simples e fácil de entender para quem está iniciando em Python. Ela implementa as classes básicas:

- `Carro` — representa um veículo (ano, marca, modelo, cor, placa).
- `Cliente` — representa um cliente (nome, CPF e lista de seguros).
- `SeguroVeiculo` — representa uma apólice de seguro (carro, cliente, valor, vigência).

## Estrutura do projeto

```
Projeto_2/
├─ src/
│  ├─ carro.py         # classe Carro
│  ├─ cliente.py       # classe Cliente
   └─ seguro.py        # classe SeguroVeiculo
├─ tests/
│  └─ test.py          # script de exemplo que cria objetos e imprime informações
└─ docs/
	 └─ README.md        # este arquivo
```

## Encapsulamento

Nesta versão simples usei encapsulamento para proteger atributos sensíveis:

- `Cliente` armazena o CPF em `_cpf` (privado) e expõe `get_cpf()` e `atualizar_cpf(novo_cpf)`.
- `Carro` armazena a placa em `_placa` (privado) e expõe `get_placa()` e `atualizar_placa(nova_placa)`.

Isso significa que, em vez de acessar `cliente._cpf` diretamente, você deve usar `cliente.get_cpf()` — o que é uma boa prática pois permite validar/formatar o CPF no futuro sem mudar o resto do código.

## Como executar (modo simples)

É importante executar os testes a partir da raiz do projeto para que o Python encontre o pacote `src`.

Abra um terminal na pasta `Projeto_2` e rode:

```bash
python3 tests/test.py
```

## Exemplo de uso

No `tests/test.py` há um exemplo completo. Abaixo um snippet mostrando como usar os getters/atualizadores:

```python
from src.cliente import Cliente
from src.carro import Carro

cliente = Cliente("João Silva", "123.456.789-00")
carro = Carro(2020, "Toyota", "Corolla", "Branco", "XYZ-1234")

print(cliente.get_cpf())       # lê o CPF através do método público
print(carro.get_placa())       # lê a placa através do método público

carro.atualizar_placa("ABC-0001")
cliente.atualizar_cpf("000.000.000-00")
```

