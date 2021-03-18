/**
 * @Author Churong Zhang
 * @Date 03-17-2021
 */

$(document).ready(function () {
  $(".dropdown-toggle").click((e) => {
    e.preventDefault();
    $(".dropdown-menu").toggle();
  });
  $.ajax({
    url: "js/data.json",
    dataType: "json",
    success: function (data) {
      $(".gallery").children().remove();
      data.forEach((pic) => {
        const { path, title, id, city, country, taken } = pic;
        const itemId = `#${id}`;
        const item = `<li><img id="${id}" alt="${title}" src="images/square/${path}" /></li>`;
        $(".gallery").append(item);
        $(itemId).mouseenter((e) => {
          $(itemId).toggleClass("gray");
          const preview = `<div id="preview"><img alt="${title}" 
          src="images/medium/${path}"/><p>${title} <br/>${city}, ${country} [${taken}]</p></div>`;
          $("body").append(preview);
          setTimeout(() => {
            $("#preview").fadeOut(1000);
          }, 2000);
        });
        $(itemId).mouseleave((e) => {
          $(itemId).toggleClass("gray");
          $("#preview").remove();
        });
        $(itemId).mousemove((e) => {
          const { clientX, clientY, pageX, pageY } = e;

          var newX = pageX + 20;
          var newY = pageY - 20;
          var width = $("#preview").width();
          var height = $("#preview").height();
          var docWidth = $(window).width();
          var docHeight = $(window).height();
          if (clientX > docWidth / 2) {
            newX = newX - width - 60;
          }
          if (clientY > docHeight / 2) {
            newY = newY - height * (clientY / docHeight);
          }
          $("#preview").css({
            top: newY,
            left: newX,
          });
        });
      });
    },
    error: function () {
      alert("error loading file");
    },
  });
});
