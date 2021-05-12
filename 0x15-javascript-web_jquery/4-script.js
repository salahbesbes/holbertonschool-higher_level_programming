/** on click check for color and change it  */
$(document).ready(function () {
  const header = $('header');

  $('div#toggle_header').click(() => {
    const currentColor = header.css('color');
    if (currentColor === 'rgb(0, 255, 0)') {
      header.css({ color: 'rgb(255, 0, 0)' });
    } else if (currentColor === 'rgb(255, 0, 0)') { header.css({ color: 'rgb(0, 255, 0)' }); }
  });
});
