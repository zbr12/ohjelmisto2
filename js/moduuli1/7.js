'use strict';

function heitaNoppaa(maara) {
    let summa = 0;
    for (let n = 0; n<maara; n++) {
        summa = summa + Math.floor(Math.random() *  6) + 1;
    }
    return summa;
}

let nopat = parseInt(prompt("Anna noppien määrä."));
let summa = heitaNoppaa(nopat);
document.querySelector('#target').innerHTML = 'Noppien summa on ' + summa;