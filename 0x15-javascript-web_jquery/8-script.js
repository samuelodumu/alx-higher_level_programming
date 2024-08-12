$(function () {
  $.get(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    (data, status) => {
      for (const movie of data.results) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      }
    }
  );
});
