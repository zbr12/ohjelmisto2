'use strict';

const kohde = document.querySelector('#target');

const eka = document.createElement('li');
eka.textContent = 'First item';
kohde.appendChild(eka);

const toka = document.createElement('li');
toka.textContent = 'Second item';
toka.classList.add('my-item');
kohde.appendChild(toka);

const kolmas = document.createElement('li');
kolmas.textContent = 'Third item';
kohde.appendChild(kolmas);