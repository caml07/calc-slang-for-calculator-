const screen = document.querySelector(".screen");
const buttons = document.querySelectorAll("button");

const OPERATORS = ["+", "−", "×", "÷", "^"];
const FUNCTIONS = ["sin", "cos", "tan", "log", "ln", "√"];
const ERRORS = ["Math Error", "Syntax Error", "Error"];

const MODEL_SYNTAX = {
    "×": "*",
    "÷": "/",
    "−": "-",
    "√": "sqrt",
    "π": "pi",
};

let justEvaluated = false;

function show(text) {
    screen.textContent = text;
}

function isError(text) {
    return ERRORS.includes(text);
}

function toExpression(text) {
    return text.replace(/[×÷−√π]/g, (char) => MODEL_SYNTAX[char]);
}

function formatResult(result) {
    if (typeof result === "string") {
        return result;
    }
    return String(Number(Number(result).toPrecision(12)));
}

function clearAll() {
    show("0");
    justEvaluated = false;
}

function deleteLast() {
    if (justEvaluated || isError(screen.textContent)) {
        clearAll();
        return;
    }
    const text = screen.textContent.slice(0, -1);
    show(text === "" ? "0" : text);
}

function baseForOperand() {
    let text = screen.textContent;
    if (isError(text) || justEvaluated || text === "0") {
        text = "";
        justEvaluated = false;
        show(text);
        return text;
    }
    if (/[\d.)%π]$/.test(text)) {
        return text + "×";
    }
    return text;
}

function appendDigit(digit) {
    const text = screen.textContent;
    if (isError(text) || justEvaluated) {
        justEvaluated = false;
        show(digit);
        return;
    }
    show(text === "0" ? digit : text + digit);
}

function appendDecimal() {
    const text = screen.textContent;
    if (isError(text) || justEvaluated) {
        justEvaluated = false;
        show("0.");
        return;
    }
    const trailing = text.match(/\d*\.?\d*$/)[0];
    if (trailing.includes(".")) {
        return;
    }
    show(text + ".");
}

function appendOperator(operator) {
    let text = screen.textContent;
    if (isError(text)) {
        justEvaluated = false;
        show("0");
        text = "0";
    } else if (justEvaluated) {
        justEvaluated = false;
    }
    const last = text.slice(-1);
    if (OPERATORS.includes(last) && operator !== "−") {
        show(text.slice(0, -1) + operator);
        return;
    }
    show(text + operator);
}

function appendOpenParen() {
    show(baseForOperand() + "(");
}

function appendCloseParen() {
    const text = screen.textContent;
    if (isError(text) || justEvaluated) {
        return;
    }
    const opens = (text.match(/\(/g) || []).length;
    const closes = (text.match(/\)/g) || []).length;
    if (opens <= closes || OPERATORS.includes(text.slice(-1)) || text.endsWith("(")) {
        return;
    }
    show(text + ")");
}

function appendPercent() {
    const text = screen.textContent;
    if (isError(text) || justEvaluated || !/\d$/.test(text)) {
        return;
    }
    show(text + "%");
}

function appendPi() {
    show(baseForOperand() + "π");
}

function appendFunction(name) {
    show(baseForOperand() + name + "(");
}

function toggleSign() {
    const text = screen.textContent;
    if (isError(text)) {
        return;
    }
    justEvaluated = false;
    if (/^\d*\.?\d*$/.test(text) && text !== "0" && text !== "") {
        show("-" + text);
        return;
    }
    if (/^-\d*\.?\d*$/.test(text)) {
        show(text.slice(1));
        return;
    }
    if ("+−×÷^(".includes(text.slice(-1))) {
        show(text + "−");
    }
}

async function evaluate() {
    if (justEvaluated || isError(screen.textContent)) {
        return;
    }
    const expression = toExpression(screen.textContent);
    try {
        const res = await fetch("/calculate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ expression: expression }),
        });
        if (!res.ok) {
            throw new Error("request failed");
        }
        const data = await res.json();
        show(formatResult(data.result));
    } catch (error) {
        show("Error");
    }
    justEvaluated = true;
}

buttons.forEach((button) => {
    button.addEventListener("click", () => {
        const value = button.textContent.trim();

        if (value === "AC") return clearAll();
        if (value === "DEL") return deleteLast();
        if (value === "=") return evaluate();
        if (value === "±") return toggleSign();
        if (value === "(") return appendOpenParen();
        if (value === ")") return appendCloseParen();
        if (value === ".") return appendDecimal();
        if (value === "π") return appendPi();
        if (value === "%") return appendPercent();
        if (OPERATORS.includes(value)) return appendOperator(value);
        if (FUNCTIONS.includes(value)) return appendFunction(value);
        if (/^\d$/.test(value)) return appendDigit(value);
    });
});
