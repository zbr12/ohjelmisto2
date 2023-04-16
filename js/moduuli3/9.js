'use strict';

const laskutoimitus = document.querySelector('#calculation');
const aloita = document.querySelector('#start');
const tulos = document.querySelector('#result');

aloita.addEventListener('click', () => {
    let lasku = laskutoimitus.value;
    let vastaus;
    if (lasku.includes('+')) {
        let numerot = lasku.split('+');
        vastaus = parseInt(numerot[0]) + parseInt(numerot[1]);
    } else if (lasku.includes('-')) {
        let numerot = lasku.split('-');
        vastaus = parseInt(numerot[0]) - parseInt(numerot[1]);
    } else if (lasku.includes('*')) {
        let numerot = lasku.split('*');
        vastaus = parseInt(numerot[0]) * parseInt(numerot[1]);
    } else if (lasku.includes('/')) {
        let numerot = lasku.split('/');
        vastaus = parseInt(numerot[0]) / parseInt(numerot[1]);
    }
    tulos.textContent = vastaus;
});