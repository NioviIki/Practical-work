$(function () {

  /* Functions */

  var loadForm = function () { // грузит всплывающее окно с формой
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),  //в бук листе, в баттоне есть data-url с сылкой на запрос
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book .modal-content").html(""); // вызывает штмл с этим классом, он находится в  конце
        $("#modal-book").modal("show"); // открывает запрос
      },
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form); // бэкэнд запрос
      }
    });
  };

  var saveForm = function () { // сейвит без перехода
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#book-table tbody").html(data.html_book_list);
          $("#modal-book").modal("hide");
        }
        else {
          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  // .js-create-book -- класс в бук листе. баттон
  $(".js-create-book").click(loadForm); //get
  $("#modal-book").on("submit", ".js-book-create-form", saveForm); //post

  // Update book
  $("#book-table").on("click", ".js-update-book", loadForm);
  $("#modal-book").on("submit", ".js-book-update-form", saveForm);

  // Delete book
  $("#book-table").on("click", ".js-delete-book", loadForm);
  $("#modal-book").on("submit", ".js-book-delete-form", saveForm);

});