/** add li to some tag */
$(document).ready(function () {
  const ul = $('UL.my_list');
  const newElement = '<li>Item</li>';

  $('DIV#add_item').click(() => {
    ul.append(newElement);
  });
});
