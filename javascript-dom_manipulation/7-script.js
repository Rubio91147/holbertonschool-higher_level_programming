
const list_movies = document.body.querySelector("#list_movies");
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Response was not ok');
        }
        return response.json();
    })
    .then(data => {
        for (const movie of data.results) {
            const li = document.createElement("li");
            li.textContent = movie.title;
            list_movies.appendChild(li);
        }
    })
    .catch(error => {
        console.error('There was a problem with the fetch:', error);
    });
