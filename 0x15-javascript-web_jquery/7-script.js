/** fetch ccontent from some url */
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: function (response) {
      $('DIV#character').text(response.name);
    }
  });
});
