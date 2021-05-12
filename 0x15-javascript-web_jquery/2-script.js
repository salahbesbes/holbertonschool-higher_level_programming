/* updates the text color of the <header> element to red on click  */

const header = $('header');

$(document).ready(() =>
  $('div#red_header').click(() => {
    header.css({ color: '#FF0000' });
  })
);
