$('document').ready(function(){
    var nombre_reunion = $('.lista-reuniones.active > a').text();
    $('#nombre-reunion-active').text(nombre_reunion);
});