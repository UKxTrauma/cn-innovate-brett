function funcExample () {
    console.log("Hello World");
};

let myName = "Brett"

const myLastName = "Garrett"

if (myName === "Brett") {
    console.log(` Hello, ${myName}!`);
} else {
    console.log("You're not Brett!");
};

function reallyGodFunction (num1, num2) {
    let result = num1 + num2;
    return result;
};

function taskHider () {
    let element = document.getElementId("task-box")
    element.classList.toggle("hidden")
}

function darkMode () {
    let element = document.getElementsByTagName("body")
    element.classList.toggle("dark-mode")
}