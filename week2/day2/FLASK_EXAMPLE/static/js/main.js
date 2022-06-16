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
    let element = document.getElementById("task-box");
    element.classList.toggle("hidden");
    console.log("dsfasgdqg");
};

function darkMode () {
    let element = document.getElementById("base-body");
    element.classList.toggle("dark-mode");
};

const date = Date()

function displayDate() {
    document.getElementById("date").innerHTML = Date();
};