const settings = {
  async: true,
  crossDomain: true,
  url: 'https://free-to-play-games-database.p.rapidapi.com/api/games',
  method: 'GET',
  headers: {
    'X-RapidAPI-Key': 'ef846b702amsh93d7e05db5d8b44p1200d5jsn56ec0d4e1748',
    'X-RapidAPI-Host': 'free-to-play-games-database.p.rapidapi.com'
  }
};

$(document).ready(function () {

  $("#btn-obtener").click(function () {
    $.get(settings,
      function (data) {
        data.sort(function (a, b) {
          return a.id - b.id;
        });
        $.each(data, function (i, item) {
          var fila =
            "<tr><td>" + item.id +
            "</td><td>" + item.title +
            "</td><td>" + item.short_description +
            "</td><td>" + item.genre +
            "</td><td>" + item.publisher +
            "</td><td><img src='" + item.thumbnail + "'>" +
            "</td></tr>"
            
          $("#tabla-juegos").append(fila);
          return item.id;
        });
        console.log(data);
      });
  });

  $("#btn-limpiar").click(function () {
    $("#tbody").empty();
  });

  $('#BuscarJuegos').click(function (event) {
    event.preventDefault();
    var Buscador = $("#Buscador").val();
  
    $.ajax({
      url: settings.url + "?search=" + Buscador,
      headers: settings.headers,
      data: {
        format: 'json'
      },
      error: function () {
        alert("No se encontraron Datos sobre: "+Buscador);
      },
      dataType: 'json',
      success: function (data) {
        var Buscador = $("#Buscador").val();
  
        // Filtrar los juegos que coincidan con el título de búsqueda exacto
        var juegosFiltrados = data.filter(function(juego) {
          return juego.title.toLowerCase() === Buscador.toLowerCase();
        });
  
        if (juegosFiltrados.length === 0) {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            html: '<b class="color"> No se encontro el juego '+ Buscador +', intente con otro nombre</b>',
            confirmButtonColor: '#2C5364'
          })
          return;
        }
  
        var $Id = $('<td>').text(juegosFiltrados[0].id.common);
        var $Titulo = $('<td>').text(juegosFiltrados[0].title);
        var $Descripcion = $('<td>').text(juegosFiltrados[0].short_description)
        var $genero = $('<td>').text(juegosFiltrados[0].genre)
        var $publisher = $('<td>').text(juegosFiltrados[0].publisher)
        var $imagen = $("<td><img src='" + juegosFiltrados[0].thumbnail.png + "'>");
  
        // Para limpiar el contenedor antes de desplegar
        $("#tbody").empty();
  
        // Agregar la fila a la tabla
        var $fila = $('<tr>').append($Id, $Titulo, $Descripcion, $genero, $publisher, $imagen);
        $("#tabla-juegos").append($fila);
      },
      type: 'GET'
    });
  });
});  
