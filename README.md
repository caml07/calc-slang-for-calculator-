# calc-slang-for-calculator-
Una calculadora hecha con flask
Hola hare mi primer commit 

## How to install and run

First clone the repository and enter the project folder.

```bash
git clone https://github.com/caml07/calc-slang-for-calculator-.git
cd calc-slang-for-calculator-
python -m venv .venv
```

On macOS:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Then install the requirements and run Flask.

```bash
python -m pip install -r requirements.txt
flask --app app run --debug
```

## Model

The Model is in `models/calculator.py`. This is the part that handles the math logic of the calculator, so it stays separate from the interface. The rest of the project only needs to send an expression to:

```python
calculate(expression)
```

The Model supports addition, subtraction, multiplication, division, parentheses, powers, percentages, pi, square root, trigonometric functions in degrees, `log`, and `ln`. It follows the normal order of operations and also supports negative and decimal numbers.

When something cannot be calculated, the Model returns `Math Error`. If the expression is written incorrectly, it returns `Syntax Error`.

The Model tests are in `tests/test_calculator.py`. They check the operations and some invalid expressions so changes can be tested without depending on the interface.
