$('document').ready(function(){
    var nombre_reunion = $('.lista-reuniones.active > a').text();
    $('#nombre-reunion-active').text(nombre_reunion);

    $('#agregar_tema').on('click',function(data) {
        descripcion_tema = $('#descripcion-tema').summernote('code');
        var descripcion_tema_input = htmlEscape(descripcion_tema);
        $('#descripcion-tema-input').val(descripcion_tema_input);
    })

});
