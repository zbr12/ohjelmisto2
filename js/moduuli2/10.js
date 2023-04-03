'use strict';

let aanestettavat = [];
let aanestettavien_maara = parseInt(prompt("Anna ehdokkaiden määrä."))
for (let i = 0; i<aanestettavien_maara; i++) {
    aanestettavat.push({name: prompt("Anna nimi ehdokkaalle " + (i+1)), votes: 0,},);
}
let aanestajat = parseInt(prompt("Anna äänestäjien määrä."))
