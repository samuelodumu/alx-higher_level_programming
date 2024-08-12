$(function () {
  $('input#btn_translate').click(function () {
    const lang = '?lang=' + $('input#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/' + lang;
    $.get(url, (data, status) => {
      $('div#hello').text(data.hello);
    });
  });
});
