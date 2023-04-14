'use strict';

const haku = document.querySelector('#haku');
let div = document.querySelector('#results');
haku.addEventListener('submit', async function(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    // get value of input element
    const nimi = document.querySelector('input[name=nimi]').value;
    div.innerHTML = '';
    try {                                               // error handling: try/catch/finally
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${nimi}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        for (let i =0; i<jsonData.length; i++) {
            console.log(jsonData[i]);
            let ohjelma = jsonData[i];
            let nimi = ohjelma.show.name;
            let linkki = ohjelma.show.url;
            let kuva = ohjelma.show.image && ohjelma.show.image.medium ? ohjelma.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
            let yhteenveto = ohjelma.show.summary;

            let h2 = document.createElement('h2'); 
            let t = document.createTextNode(nimi);  // create text node
            h2.appendChild(t);
            let a = document.createElement('a');
            let link = document.createTextNode(linkki);
            a.appendChild(link);
            a.href = linkki;
            a.target = "_blank";
            let im = document.createElement('img');
            im.src = kuva;               // set src attribute
            im.alt = nimi;                                        // set alt attribute
            let yhtveto = document.createElement('div');
            yhtveto.innerHTML = yhteenveto;
            let artikkeli = document.createElement('article')
            artikkeli.appendChild(h2);
            artikkeli.appendChild(a);
            artikkeli.appendChild(im);
            artikkeli.appendChild(yhtveto);
            div.appendChild(artikkeli);  
        }
    } catch (error) {
        console.log(error.message);
    }
});
