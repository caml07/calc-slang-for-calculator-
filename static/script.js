const screen = document.querySelector(".screen");
const buttons = document.querySelectorAll("button");

buttons.forEach((button) => {
    button.addEventListener("click", () => {
        const value = button.textContent.trim();

        if ("0123456789".includes(value) && value.length === 1) {
            if (screen.textContent === "0") {
                screen.textContent = value;
            } else {
                screen.textContent += value;
            }
        }

      if (value === "DEL") {
        if (screen.textContent.length == 1) {
          screen.textContent = 0
        } else {
          screen.textContent = screen.textContent.slice(1, screen.textContent.length);
        }
        }

        if (value === "AC") {
            screen.textContent = "0";
        }

        if (value === ".") {
            screen.textContent += value;
        }
    });
});
