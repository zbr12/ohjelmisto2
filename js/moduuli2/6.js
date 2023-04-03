'use strict';

function heitaNoppaa() {
    let tulos = Math.floor(Math.random() *  6) + 1;
    return tulos;
}
let teksti = ''
while (true) {
    let tulos = heitaNoppaa()
    teksti = teksti + '<li>'+tulos+'</li>'
    if (tulos == 6) {
        break;
    }
}
document.querySelector('#luvut').innerHTML = teksti;