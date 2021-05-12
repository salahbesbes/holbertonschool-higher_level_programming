/** display all movies fetched  */
$(document).ready(function () {
  const ul = $('UL#list_movies');
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (response) {
      const listMovies = response.results;
      $.each(listMovies, (index, movie) => {
        ul.append(`<li> ${index + 1}: ${movie.title} </li>`);
      });
    }
  });
});
