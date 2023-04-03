'use strict';

let numerot = [];
let numero;
while (true) {
    numero = parseInt(prompt('Anna numero'));
    if (numerot.includes(numero)) {
        alert("Number already entered!");
        break;
    }
    numerot.push(numero);
};numerot.sort((a,b) => a-b);
for (let i = 0; i<numerot.length; i++) {
    console.log(numerot[i]);
}