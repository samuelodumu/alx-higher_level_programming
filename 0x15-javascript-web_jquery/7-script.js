$(function () {
  $.get(
    'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    (data, status) => {
      $('div#character').text(data.name);
    }
  );
});
