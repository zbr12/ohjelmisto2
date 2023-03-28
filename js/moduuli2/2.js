'use strict';

let maara = parseInt(prompt("Anna osallistujien määrä"));
let nimet = [];
for (let i = 0; i<maara; i++) {
    let nimi = prompt("Anna osallistujan " + (i+1) + " nimi");
    nimet.push(nimi);
}
nimet.sort();
let teksti = "";
for (let i = 0; i<nimet.length; i++) {
    teksti = teksti + "<li>" + nimet[i] +"</li>"
}
document.querySelector('#nimet').innerHTML = teksti;