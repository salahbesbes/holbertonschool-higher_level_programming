/** add li to some tag */
$(document).ready(function () {
  const ul = $('UL.my_list');
  const newElement = '<li>Item</li>';

  $('DIV#add_item').click(() => {
    ul.append(newElement);
  });
  $('DIV#remove_item').click(() => {
    $('UL.my_list li:last-child').css({ color: 'red' });
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
