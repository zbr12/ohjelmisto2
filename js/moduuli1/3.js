'use strict';
let ensimmainen = parseInt(prompt('Anna ensimmäinen luku'));
let toinen = parseInt(prompt('Anna toinen luku'));
let kolmas = parseInt(prompt('Anna kolmas luku'));
let summa = ensimmainen + toinen + kolmas;
let tulo = ensimmainen * toinen * kolmas;
let keskiarvo = summa/3;
document.querySelector('#target').innerHTML = 'Summa: ' + summa + ', Tulo: ' + tulo + ', Keskiarvo: ' + keskiarvo;