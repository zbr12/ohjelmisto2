'use strict';
function heitaNoppaa(maara) {
    let summa = 0;
    for (let n = 0; n<maara; n++) {
        summa = summa + Math.floor(Math.random() *  6) + 1;
    }
    return summa;
}

let nopat = parseInt(prompt('Anna noppien määrä'));
let luku = parseInt(prompt('Anna haluamasi luku'));
let osumat = 0;
for (let i = 0; i < 10000; i++) {
    console.log(heitaNoppaa(nopat))
    if (heitaNoppaa(nopat) == luku) {
        osumat = (osumat + 1);
    }
}
let todennakoisyys = (osumat / 10000 * 100);
document.querySelector('#target').innerHTML = 'Todennäköisyys saada luku  ' + luku + ' ' + nopat + ':lla nopalla on ' + todennakoisyys + '%.';