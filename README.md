<div align="center">

  <p>｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ──────────── ꒰ 🪵 ꒱ ──────────── ⋆｡ﾟ☾ ﾟ｡⋆｡☁︎｡ﾟ</p>

  <h1>˚₊‧꒰ა 🌲 Sistema de Madeireira em Python 🌲 ໒꒱‧₊˚</h1>

  <p>
    <i>✧･ﾟ: *✧･ﾟ:* Aplicação modular em Python via linha de comando para gestão de pedidos de madeira com tabela de preços por tipo, descontos progressivos por volume e cálculo de frete *:･ﾟ✧*:･ﾟ✧</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Arquitetura-Fun%C3%A7%C3%B5es%20Modulares-E6E6FA?style=for-the-badge&logoColor=555555" alt="Funções Modulares" />
    <img src="https://img.shields.io/badge/Console-Sistema%20CLI-FFD1DC?style=for-the-badge&logoColor=white" alt="Sistema CLI" />
  </p>

</div>

<br/>

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 🍂 ꒱ Preços & Regras de Negócio

#### Catálogo de Madeiras (`por tora`)
| 🌲 Código | 🪵 Tipo de Madeira | 🍃 Preço Unitário |
| :---: | :--- | :---: |
| `PIN` | Pinho *(Pine)* | `R$ 150,40` |
| `PER` | Peroba | `R$ 170,20` |
| `MOG` | Mogno *(Mahogany)* | `R$ 190,90` |
| `IPE` | Ipê *(Ipe)* | `R$ 210,10` |
| `IMB` | Imbuia | `R$ 220,70` |

#### Descontos por Volume & Faixas de Frete
- **₊˚🪓 Abaixo de `100` toras:** `0%` de desconto
- **₊˚🪓 De `100` a `499` toras:** `4%` de desconto
- **₊˚🪓 De `500` a `999` toras:** `9%` de desconto
- **₊˚🪓 De `1.000` a `2.000` toras:** `16%` de desconto *(pedidos acima de `2.000` toras são recusados)*
- **₊˚🚚 Opções de Frete:** Rodoviário (`R$ 1.000,00`), Ferroviário (`R$ 2.000,00`) ou Hidroviário (`R$ 2.500,00`)

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 🍃 ꒱ Como Foi Construído

- **₊˚🌲 Design Modular (`def`):** Separação da escolha da madeira, validação da quantidade de toras e cálculo do modal de transporte em funções dedicadas com retornos simples e em tupla.
- **₊˚🪵 Tratamento de Exceções e Limites:** Combinação de laços `while True` com blocos `try / except ValueError` para capturar entradas não numéricas e aplicar os limites de quantidade do pedido.
- **₊˚🌲 Consolidação do Total do Pedido:** Aplicação de expressões aritméticas integrando custo unitário das toras, faixas progressivas de desconto e taxas fixas de frete.

<br/>

<div align="center">
  <p>°•. 🌲 .•° ────── ꒰ 💗 ꒱ ────── °•. 🌲 .•°</p>
  <p><i>feito com 💗 por <b>Maria Eduarda Gonçalves</b></i></p>
</div>
