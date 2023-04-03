'use strict';

function concat(array) {
    let teksti = ''
    for (let i = 0; i<array.length;i++) {
        teksti = teksti + array[i];
    }
    return teksti
}
let array1 = ["Johnny", "DeeDee", "Joey", "Marky"]
let teksti = concat(array1);
document.querySelector('#teksti').innerHTML = teksti;