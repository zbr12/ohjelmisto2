let gameId;
let hevosenkenka = 0;
let timantti = 0;
let lahtokentta;

document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('#single');
  const mapDiv = document.querySelector('#map');
  const welcomeDiv = document.querySelector('#welcome');
  let playerName = 'Jari';
  let formSubmitted = false;
  let airport;
  let markers = [];

  // Initialize the map
function initMap() {
  const map = L.map('map').setView([60.23, 24.74], 13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  const redMarkerIcon = L.icon({
    iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
  });

  async function getData() {
    // Make API call to get European airports
    const response = await fetch('/european_airports');
    const data = await response.json();
    gameId = data[1]['id'];
    console.log(gameId, "EUROPEAN AIRPORTS");
    // Loop through airport data and create markers on the map
    data[0].forEach(a => {
      markerColor = 'blue';
      if (data[0]['ident'] === a['ident']) {
        markerColor = 'red';
      }
      //console.log(a);
      const markerIcon = new L.Icon({
        // create a new marker icon with the selected color
        iconUrl: `https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${markerColor}.png`,
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
      });
      const marker = L.marker([a.latitude_deg, a.longitude_deg], {
        icon: markerIcon,
        ident: a.ident // add ident property to marker
      }).addTo(map);
      //Add marker to markers array
      markers.push(marker);
      marker.bindPopup(`<b>${a.name} (${a.ident})</b><br>${a.municipality}, ${a.iso_country}`).on('click', function () {
        updatePopup(marker, a);

      });
    });

    // Assign a random airport to the player and display their name in the infobox
    const randomResponse = await fetch('/random', {
      method: 'POST',
      body: JSON.stringify({playerName}),
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const randomData = await randomResponse.json();
    airport = randomData;
    console.log(gameId, "get name gameid");
    const {ident, latitude_deg, longitude_deg} = randomData;
    lahtokentta = randomData.ident;
    await fetch('/get_player_name', {
      method: 'POST',
      body: JSON.stringify({playerName, ident, gameId}),
      headers: {
        'Content-Type': 'application/json'
      }
    });

  currentLocation = {ident, latitude_deg, longitude_deg};
  console.log(currentLocation, "NYKYINEN SIJAINTI");
  //console.log(data);
  // Create the infobox content
  var content = '<h2>Airport Name:</h2>' + airport.name;
  // Add the player name to the infobox content
  content += '<h2>ICAO:</h2>' + airport.ident;
  content += '<h2>Player Name:</h2>' + playerName;

  // Create the infobox and set its position
  var infobox = L.popup().setLatLng([airport.latitude_deg, airport.longitude_deg]).setContent(content);
  // Open the infobox on the map
  infobox.openOn(map);

  // Center the map on the airport assigned to the player
  map.setView([airport.latitude_deg, airport.longitude_deg], 7);

  // Hide form element if already submitted
  if (formSubmitted) {
    form.style.display = 'none';
  }
  }

  getData();
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

async function hae_palkinto(icao, id) {
  let vastaus = await fetch(`/palkinto?icao=${icao}&game_id=${id}`);
  let jsonData = await vastaus.json();
  console.log(jsonData);
  let avattu = jsonData[0].avattu;
  let palkintoid = jsonData[0].palkinto;
  console.log(avattu);
  console.log(palkintoid);
    if (avattu == 0) {
      if (palkintoid == 1 && hevosenkenka == 0) {
        window.alert("Löysit hevosenkengän!");
        hevosenkenka = 1;
        await fetch(`/avattu?icao=${icao}&game_id=${id}`);
      } else if (palkintoid == 1 && hevosenkenka == 1) {
        window.alert("Olisit löytänyt hevosenkengän mutta mitä tekisit toisella")
        await fetch(`/avattu?icao=${icao}&game_id=${id}`);
      } else if (palkintoid == 2) {
        window.alert("Tyhjää täynnä");
        await fetch(`/avattu?icao=${icao}&game_id=${id}`);
      } else if (palkintoid == 3) {
        window.alert("Löysit timantin!");
        timantti = 1;
        await fetch(`/avattu?icao=${icao}&game_id=${id}`);
      } else if (palkintoid == 4) {
        vastaus = await fetch(`/encounter`);
        jsonData = await vastaus.json();
        let teksti = jsonData[0].teksti;
        let kysymys = jsonData[0].kysymys;
        let min_raha = jsonData[0].min_raha;
        let max_raha = jsonData[0].max_raha;
        if (window.confirm(teksti + "\n" + kysymys)) {
          await fetch(`/avattu?icao=${icao}&game_id=${id}`);
        }
      }
    }
  }  

function updatePopup(marker, a) {
      console.log(marker, "marker data inside");
      console.log(a, "a data inside");
  const latlng = marker.getLatLng();
  const destination = L.latLng(latlng.lat, latlng.lng);
  const origin = L.latLng(currentLocation.latitude_deg, currentLocation.longitude_deg);

  // Make the API request to get the distance and fuel cost
    fetch(`/haehinta?lat1=${origin.lat}&lng1=${origin.lng}&lat2=${destination.lat}&lng2=${destination.lng}&iso=${a.iso_country}`, {
      method: 'POST',
      body: JSON.stringify({}),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
      const distance = Math.round(data['distance_km']);
      const fuelCost = data['fuel'];
      const country = data['country'];
      money = 1500;
      // Update the content of the popup
      let content = `<b>${a.name}</b><br><b>ICAO: ${a.ident}</b><br><b>${country}</b><br><b>${marker.options.title}</b><br>
      <div>Distance: ${distance} km</div>
      <div>Fuel cost: ${fuelCost} €</div>`;

      // Show the button if the player's money is greater than or equal to the flight cost
      // and if the marker ident does not match the current airport ident
      if (money >= fuelCost && marker.options.ident !== airport.ident) {
        content += '<div><button id="flyButton">Fly here</button></div>';
        marker.getPopup().setContent(content);
        setTimeout(() => {
          const flyButton = document.getElementById('flyButton');
          flyButton.addEventListener('click', function() {
            if (timantti == 1 && marker.options.ident == lahtokentta) {
              alert("Onneksi olkoon! Voitit pelin!");
              return;
            }
            hae_palkinto(marker.options.ident, gameId);
            fly(a, distance, fuelCost);
            //console.log("A = " + a.ident);
                      // Close and reopen the infobox
            marker.closePopup();
            setTimeout(() => marker.openPopup(), 1000);
          });
        }, 100);
      }

      marker.getPopup().setContent(content);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }

function fly(a, distance, fuelCost) {
  fetch(`/lennakohteeseen?icao=${a.ident}`, {
    method: 'POST',
    body: JSON.stringify({distance, fuelCost, latitude_deg: a.latitude_deg, longitude_deg: a.longitude_deg, ident: a.ident}),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    // Update the player's location with the new airport data
    airport = data;
    console.log(airport, "DATA")
    const { ident, latitude_deg, longitude_deg } = data;
    currentLocation = {ident, latitude_deg, longitude_deg};
  console.log(currentLocation, "NYKYINEN SIJAINTI")
  //console.log(data);
  // Create the infobox content
  var content = '<h2>Airport Name:</h2>' + airport.name;
  // Add the player name to the infobox content
  content += '<h2>ICAO:</h2>' + airport.ident;
  content += '<h2>Player Name:</h2>' + playerName;

  // Create the infobox and set its position
  var infobox = L.popup().setLatLng([airport.latitude_deg, airport.longitude_deg]).setContent(content);
  // Open the infobox on the map
  infobox.openOn(map);

  // Center the map on the airport assigned to the player
  map.setView([airport.latitude_deg, airport.longitude_deg], 7)

    // Loop through all markers and update their icons
    markers.forEach(marker => {
      let markerColor = 'blue';
      if (marker.options.ident === ident) {
        markerColor = 'red';
      }
      const markerIcon = new L.Icon({
        iconUrl: `https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${markerColor}.png`,
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
      });
      marker.setIcon(markerIcon);

      // Call the updatePopup() function here for each marker
      console.log(marker, "marker data");
      console.log(a, "a data");
      updatePopup(marker, a);
    });
  })
  .catch(error => console.error(error));
}

const resetButton = document.querySelector('#resetButton');
resetButton.addEventListener('click', function() {
  fetch('/removekentat', {
    method: 'POST',
    body: JSON.stringify({}),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    // Add any additional code here to update the UI or map
  })
  .catch(error => console.error(error));
})
})// Closing curly brace for DOMContentLoaded event listener
