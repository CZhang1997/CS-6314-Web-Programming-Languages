/**
 * @Author Churong Zhang
 * @Date 03-17-2021
 */

$(document).ready(function () {
  $.ajax({
    url: "js/data.json",
    dataType: "json",
    success: function (data) {
      $(".gallery").children().remove();
      data.forEach((pic) => {
        const { description, path, title, id } = pic;
        const item = `<li><img id="${id}" alt="${title}" src="images/square/${path}" /></li>`;
        $(".gallery").append(item);
      });
    },
    error: function () {
      alert("error loading file");
    },
  });
});
