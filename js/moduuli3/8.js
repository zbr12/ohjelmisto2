'use strict';

const eka = document.querySelector('#num1');
const toka = document.querySelector('#num2');
const toimitus = document.querySelector('#operation');
const laske = document.querySelector('#start');
const tulos = document.querySelector('#result');

laske.addEventListener('click', () => {
  const ekanumero = Number(eka.value);
  const tokanumero = Number(toka.value);
  const operaatio = toimitus.value;
  let vastaus;

  if (operaatio === 'add') {
    vastaus = ekanumero + tokanumero;
  } else if (operaatio === 'sub') {
    vastaus = ekanumero - tokanumero;
  } else if (operaatio === 'multi') {
    vastaus = ekanumero * tokanumero;
  } else if (operaatio === 'div') {
    vastaus = ekanumero / tokanumero;
  }
  tulos.textContent = `Result: ${vastaus}`;
});