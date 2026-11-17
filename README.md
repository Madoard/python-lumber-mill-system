<div align="center">

  <p>｡ﾟ☁︎｡⋆｡ ﾟ☾ ﾟ｡⋆ ──────────── ꒰ 🪵 ꒱ ──────────── ⋆｡ﾟ☾ ﾟ｡⋆｡☁︎｡ﾟ</p>

  <h1>˚₊‧꒰ა 🌲 Python Lumber Mill System 🌲 ໒꒱‧₊˚</h1>

  <p>
    <i>✧･ﾟ: *✧･ﾟ:* Modular command-line Python application for lumber order management featuring wood catalog pricing, progressive volume discounts, and freight calculation *:･ﾟ✧*:･ﾟ✧</i>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-FFB7C5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Architecture-Modular%20Functions-E6E6FA?style=for-the-badge&logoColor=555555" alt="Modular Functions" />
    <img src="https://img.shields.io/badge/Console-CLI%20System-FFD1DC?style=for-the-badge&logoColor=white" alt="CLI System" />
  </p>

</div>

<br/>

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 🍂 ꒱ Pricing & Business Rules

#### Wood Catalog (`per log`)
| 🌲 Code | 🪵 Wood Type | 🍃 Unit Price |
| :---: | :--- | :---: |
| `PIN` | Pine *(Pinho)* | `$ 150.40` |
| `PER` | Peroba | `$ 170.20` |
| `MOG` | Mahogany *(Mogno)* | `$ 190.90` |
| `IPE` | Ipe *(Ipê)* | `$ 210.10` |
| `IMB` | Imbuia | `$ 220.70` |

#### Volume Discounts & Freight Tiers
* **₊˚🪓 Under `100` logs:** `0%` discount
* **₊˚🪓 `100` to `499` logs:** `4%` discount
* **₊˚🪓 `500` to `999` logs:** `9%` discount
* **₊˚🪓 `1,000` to `2,000` logs:** `16%` discount *(orders exceeding `2,000` logs are rejected)*
* **₊˚🚚 Freight Options:** Road (`$ 1,000.00`), Rail (`$ 2,000.00`), or Waterway (`$ 2,500.00`)

<p align="center">‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾. ─────────────────────── ‧₊˚ ☁️⋅♡𓂃 ࣪ ִֶָ☾.</p>

### ╰┈➤ ꒰ 🍃 ꒱ How It Was Built

* **₊˚🌲 Modular Design (`def`):** Separated wood selection, log quantity validation, and shipping mode calculation into dedicated functions with single and tuple return values.
* **₊˚🪵 Exception & Bounds Handling:** Combined `while True` loops with `try / except ValueError` blocks to catch non-numeric inputs and enforce order quantity limits.
* **₊˚🌲 Order Total Consolidation:** Applied arithmetic expressions integrating unit log costs, progressive discount tiers, and fixed freight fees.

<br/>

<div align="center">
  <p>°•. 🌲 .•° ────── ꒰ 💗 ꒱ ────── °•. 🌲 .•°</p>
  <p><i>made with 💗 by <b>Maria Eduarda Gonçalves</b></i></p>
</div>
