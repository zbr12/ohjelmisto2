'use strict';

let eka = parseInt(prompt("Anna ensimmäinen numero"));
let toka = parseInt(prompt("Anna toinen numero"));
let kolmas = parseInt(prompt("Anna kolmas numero"));
let neljas = parseInt(prompt("Anna neljäs numero"));
let viides = parseInt(prompt("Anna viides numero"));
let numerot = [eka, toka, kolmas, neljas, viides];
for (let i = 0; i<numerot.length; i++) {
    console.log(numerot[numerot.length-i-1]);
}