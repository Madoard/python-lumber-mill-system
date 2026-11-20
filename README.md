<div align="center">

  <p>─────────────────────── ✦ ───────────────────────</p>

  <h1>꒰ა Sistema de Madeireira em Python ໒꒱</h1>

  <p>
    <i>Aplicação modular em Python via linha de comando para pedidos de madeira com descontos por volume e cálculo de frete.</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Arquitetura-Fun%C3%A7%C3%B5es%20Modulares-E6E6FA?style=for-the-badge&logoColor=555555" alt="Funções Modulares" />
    <img src="https://img.shields.io/badge/Console-Sistema%20CLI-FFD1DC?style=for-the-badge&logoColor=white" alt="Sistema CLI" />
  </p>

</div>

<br/>

### ✦ Resumo

Permite registrar pedidos de madeira diretamente no terminal com seleção do tipo de madeira, validação da quantidade de toras, aplicação de descontos progressivos por volume e cálculo do valor final somando o modal de frete escolhido.

### ✦ Tecnologias

- **Python 3.x:** Linguagem principal para funções modulares, tratamento de exceções (`try / except`), laços de validação e interação via terminal (sem dependências externas).

### ✦ Regras

#### Catálogo de Madeiras (por tora)

| Código | Tipo de Madeira | Preço Unitário |
| :---: | :--- | :---: |
| `PIN` | Pinho | `R$ 150,40` |
| `PER` | Peroba | `R$ 170,20` |
| `MOG` | Mogno | `R$ 190,90` |
| `IPE` | Ipê | `R$ 210,10` |
| `IMB` | Imbuia | `R$ 220,70` |

#### Descontos por Volume

- **Abaixo de `100` toras:** `0%` de desconto
- **De `100` a `499` toras:** `4%` de desconto
- **De `500` a `999` toras:** `9%` de desconto
- **De `1.000` a `2.000` toras:** `16%` de desconto *(pedidos acima de `2.000` toras não são aceitos)*

#### Opções de Frete

- **Rodoviário:** `R$ 1.000,00`
- **Ferroviário:** `R$ 2.000,00`
- **Hidroviário:** `R$ 2.500,00`

<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Executar

1. **Pré-requisitos:** Tenha o **Python 3.x** instalado na máquina.
2. **Clone o repositório:**
   ```bash
   git clone https://github.com/Madoard/python-lumber-mill-system.git
   cd python-lumber-mill-system
   ```
3. **Execute o script (`madeireira.py`):**
   ```bash
   python madeireira.py
   ```

### ✦ Exemplo de Uso

```text
Bem-vindo à Madeireira de Maria Eduarda Gonçalves!
Por favor, informe o tipo de madeira desejado:
PIN - Tora de Pinho
PER - Tora de Peroba
MOG - Tora de Mogno
IPE - Tora de Ipê
IMB - Tora de Imbuia

Informe o tipo de madeira desejado: mog

Informe a quantidade de toras: 200

Escolha a opção de frete:
 1 - Transporte Rodoviário - R$ 1000.00
 2 - Transporte Ferroviário - R$ 2000.00
 3 - Transporte Hidroviário - R$ 2500.00
Opção: 1

Total: R$ 37652.80
```

O cálculo do exemplo: `190,90 × 200 = 38.180,00`, menos 4% de desconto = `36.652,80`, mais `1.000,00` de frete = `37.652,80`.

<p align="center">─────────────────────── · ───────────────────────</p>

### ✦ Como Foi Construído

O código completo está em [`madeireira.py`](./madeireira.py). Abaixo está a estrutura principal e como cada parte funciona:

```python
def escolher_tipo_madeira():
    while True:
        tipo_madeira = input("\nInforme o tipo de madeira desejado: ").strip().upper()
        if tipo_madeira == "PIN":
            return 150.40
        elif tipo_madeira == "PER":
            return 170.20
        elif tipo_madeira == "MOG":
            return 190.90
        elif tipo_madeira == "IPE":
            return 210.10
        elif tipo_madeira == "IMB":
            return 220.70
        else:
            print("Escolha inválida, informe o tipo de madeira novamente.")
            print("PIN - Tora de Pinho")
            print("PER - Tora de Peroba")
            print("MOG - Tora de Mogno")
            print("IPE - Tora de Ipê")
            print("IMB - Tora de Imbuia")


def quantidade_toras():
    while True:
        try:
            qtd = int(input("\nInforme a quantidade de toras: "))
            if qtd <= 0 or qtd > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras. Tente novamente.")
                continue
            elif qtd < 100:
                return qtd, 0.0
            elif 100 <= qtd < 500:
                return qtd, 0.04
            elif 500 <= qtd < 1000:
                return qtd, 0.09
            elif 1000 <= qtd <= 2000:
                return qtd, 0.16
        except ValueError:
            print("Pedido inválido. Informe um número inteiro para a quantidade de toras.")


def opcao_frete():
    while True:
        try:
            opcao = int(input(
                "\nEscolha a opção de frete:\n"
                " 1 - Transporte Rodoviário - R$ 1000.00\n"
                " 2 - Transporte Ferroviário - R$ 2000.00\n"
                " 3 - Transporte Hidroviário - R$ 2500.00\n"
                "Opção: "
            ))
            if opcao == 1:
                return 1000
            elif opcao == 2:
                return 2000
            elif opcao == 3:
                return 2500
            else:
                print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Informe um número inteiro.")


preco_unitario = escolher_tipo_madeira()
quantidade, desconto = quantidade_toras()
custo_frete = opcao_frete()

total = ((preco_unitario * quantidade) * (1 - desconto)) + custo_frete

print(f"\nTotal: R$ {total:.2f}")
```

- **Funções modulares (`escolher_tipo_madeira`, `quantidade_toras`, `opcao_frete`):** Organizam cada etapa do pedido em funções próprias, com sanitização `.strip().upper()` na madeira e retorno em tupla `(qtd, desconto)` na quantidade.
- **Validação e tratamento de exceções (`while True` / `try / except`):** Impede entradas não numéricas com `ValueError`, bloqueia quantidades inválidas (`<= 0` ou `> 2000`) e valida as opções de frete.
- **Cálculo e formatação final:** Aplica o desconto progressivo sobre o subtotal (`preco_unitario * quantidade`), soma o frete e exibe o valor com `f-strings` (`:.2f`).

<br/>

<div align="center">
  <p>°•. ✦ .•° ────── ꒰ ✦ ꒱ ────── °•. ✦ .•°</p>
  <p><i>Feito por <b>Eduarda Gonçalves</b></i></p>
</div>
