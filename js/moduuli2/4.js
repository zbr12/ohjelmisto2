'use strict';

let numerot = [];
let numero;
do {
    numero = parseInt(prompt('Anna numero tai syötä 0'));
    numerot.push(numero);
} while (numero != 0);
numerot.sort((a,b) => b-a);
for (let i = 0; i<numerot.length; i++) {
    console.log(numerot[i]);
}