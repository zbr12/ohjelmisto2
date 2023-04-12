'use strict';

const haku = document.querySelector('#haku');
haku.addEventListener('submit', async function(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    // get value of input element
    const nimi = document.querySelector('input[name=nimi]').value;
    try {                                               // error handling: try/catch/finally
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${nimi}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        for (let i =0; i<jsonData.length; i++) {
            let nimi = jsonData[i].show.name;
            let linkki = jsonData[i].show.url;
            let kuva = jsonData[i].image?.medium;
            let yhteenveto = jsonData[i].summary;
            let div = document.querySelector('#results');       // get element whose id is 'example'

            let h2 = document.createElement('h2'); 
            let t = document.createTextNode(nimi);  // create text node
            h2.appendChild(t);
            let a = document.createElement('a');
            t = document.createTextNode(linkki);
            a.appendChild(t);
            let i = document.createElement('img');
            i.src = kuva;               // set src attribute
            i.alt = nimi;                                        // set alt attribute
            let yhtveto = document.createElement('div');
            t = document.createTextNode(yhteenveto);
            yhtveto.appendChild(t);
            let artikkeli = document.createElement('article')
            artikkeli.appendChild(h2);
            artikkeli.appendChild(i);
            artikkeli.appendChild(yhtveto);
            div.appendChild(artikkeli);  
        }
    } catch (error) {
        console.log(error.message);
    }
});
