//
$(document).ready(function () {
  $("span").hide();
  $("#new").hide();

  $("#add").click(function () {
    $("ul").append("<li>" + $("#new").val() + "</li>");
  });

  $("#add-icon").click(function () {
    $("#new").toggle();
    $("#new").focus();
  });

  $("#new").keypress(function (event) {
    if (event.which === 13) {
      $("ul").append(
        '<li> <span><i class="fa fa-trash"></i></span><div class="todos">' +
          $("#new").val() +
          "</div></li>"
      );
      $("#new").val("");
      $("span").hide();
    }
  });

  $("ul").on("click", "li", function () {
    $(this).toggleClass("done");
  });
  $("ul").on("click", "span", function () {
    $(this).parent().remove();
  });

  $("ul").on("mouseenter", "li", function () {
    $(this).find("span").show();
  });
  $("ul").on("mouseleave ", "li", function () {
    $(this).find("span").hide();
  });
});
