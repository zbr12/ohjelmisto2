'use strict';
const name = prompt('Type your name.');
let numero = Math.floor(Math.random() *  4) + 1;
let tupa;
if (numero == 1) {
    tupa = "Gryffindor";
} else if (numero == 2) {
    tupa = "Slytherin";
} else if (numero == 3) {
    tupa = "Ravenclaw";
} else {
    tupa = "Hufflepuff";
}
document.querySelector('#target').innerHTML = name + ', you are ' + tupa + '.';