document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('#single');
  const mapDiv = document.querySelector('#map');
  const welcomeDiv = document.querySelector('#welcome');
  let playerName = '';
  let formSubmitted = false;
  let airport;

  // Initialize the map
function initMap() {
    const map = L.map('map').setView([60.23, 24.74], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);
    // Make API call to get European airports
    fetch('/european_airports')
        .then(response => response.json())
        .then(data => {
        // Loop through airport data and create markers on the map
        data.forEach(a => {
          const marker = L.marker([a.latitude_deg, a.longitude_deg]).addTo(map);
          marker.bindPopup(`<b>${a.name} (${a.ident})</b><br>${a.municipality}, ${a.iso_country}`).on('click', function() {
            // Create the infobox content
            var content = '<h2>Airport Name:</h2>' + a.name;
            // Check if the airport is the one assigned to the player
            if (airport.ident === a.ident) {
              // Add the player name to the infobox content
              content += '<h2>Player Name:</h2>' + playerName;
            }
            // Create the infobox and set its position
            var infobox = L.popup().setLatLng([a.latitude_deg, a.longitude_deg]).setContent(content);
            // Open the infobox on the map
            infobox.openOn(map);
          });
        });

        })
        .catch(error => console.error(error));

    // Assign a random airport to the player and display their name in the infobox
    fetch('/random', {
      method: 'POST',
      body: JSON.stringify({playerName}),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      airport = data;
      // Create the infobox content
      var content = '<h2>Airport Name:</h2>' + airport.name;
      // Add the player name to the infobox content
      content += '<h2>Player Name:</h2>' + playerName;
      // Create the infobox and set its position
      var infobox = L.popup().setLatLng([airport.latitude_deg, airport.longitude_deg]).setContent(content);
      // Open the infobox on the map
      infobox.openOn(map);
    })
    .catch(error => console.error(error));

    // Hide form element if already submitted
    if (formSubmitted) {
      form.style.display = 'none';
    }
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    playerName = event.target.elements.nimi.value;
    const welcomeMsg = document.createElement('h1');
    welcomeMsg.textContent = `Welcome to flight game, ${playerName}!`;
    welcomeDiv.appendChild(welcomeMsg);
    mapDiv.style.display = 'block';
    initMap();
  });

}); // Closing curly brace for DOMContentLoaded event listener

