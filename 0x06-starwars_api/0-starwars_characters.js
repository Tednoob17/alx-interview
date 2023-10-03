#!/usr/bin/node
/* Starwars Characters */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, async (error, _, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;

    if (characters.length === 0) { return; }
    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, function (error, _, body) {
          if (error) { console.log(error); } else { console.log(JSON.parse(body).name); resolve(); }
        });
      });
    }
  }
});
