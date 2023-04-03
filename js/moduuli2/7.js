'use strict';

function heitaNoppaa(sivut) {
    let tulos = Math.floor(Math.random() *  sivut) + 1;
    return tulos;
}
let sivut = parseInt(prompt("Kuinka monta sivua nopassa?"))
let teksti = ''
while (true) {
    let tulos = heitaNoppaa(sivut)
    teksti = teksti + '<li>'+tulos+'</li>'
    if (tulos == sivut) {
        break;
    }
}
document.querySelector('#luvut').innerHTML = teksti;