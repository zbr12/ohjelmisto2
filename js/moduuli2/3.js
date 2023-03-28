'use strict';

let nimet = [];
for (let i = 0; i<6; i++) {
    let nimi = prompt("Anna koiran " + (i+1) + " nimi");
    nimet.push(nimi);
}
nimet.reverse();
let teksti = "";
for (let i = 0; i<nimet.length; i++) {
    teksti = teksti + "<li>" + nimet[i] +"</li>"
}
document.querySelector('#nimet').innerHTML = teksti;