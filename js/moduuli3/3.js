'use strict';
const names = ['John', 'Paul', 'Jones'];

const kohde = document.querySelector('#target')
for (let i = 0; i<names.length; i++) {
    let lisays = document.createElement('li');
    lisays.textContent = names[i];
    kohde.appendChild(lisays);
}
