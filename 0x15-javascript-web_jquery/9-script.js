/** displays the value of hello  */
$(document).ready(function () {
  const target = $('DIV#hello');
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (response) {
      target.text(response.hello);
    }
  });
});
