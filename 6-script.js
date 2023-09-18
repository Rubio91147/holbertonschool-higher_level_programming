
const character = document.body.querySelector("#character");
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';


fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Response was not ok');
        }
        return response.json();
    })
    .then(data => {
        character.textContent = data.name;
    })
    .catch(error => {
        console.error('There was a problem with the fetch:', error);
    });
