function cargarImagenesProductos(){


	var imgTabla = $(".imgTabla");
	var limiteStock = $(".limiteStock");

	 for(var i = 0; i < imgTabla.length; i ++){


	    $(imgTabla[i]).elevateZoom({zoomWindowPosition: 2,tint:true, tintColour:'#F90', tintOpacity:0.5,	zoomWindowFadeIn: 500,
				zoomWindowFadeOut: 500,
				lensFadeIn: 500,
				lensFadeOut: 500, zoomWindowWidth:550,
	            zoomWindowHeight:550});
	  	}
  	}


setTimeout(function(){

  cargarImagenesProductos()

},500);

/*=============================================
CARGAMOS LAS IMÁGENES CUANDO INTERACTUAMOS CON EL PAGINADOR
=============================================*/

$(".dataTables_paginate").click(function(){

	cargarImagenesProductos()
})

/*=============================================
CARGAMOS LAS IMÁGENES CUANDO INTERACTUAMOS CON EL BUSCADOR
=============================================*/
$("input[aria-controls='DataTables_Table_0']").focus(function(){

	$(document).keyup(function(event){

		event.preventDefault();

		cargarImagenesProductos()

	})


})

/*=============================================
CARGAMOS LAS IMÁGENES CUANDO INTERACTUAMOS CON EL FILTRO DE CANTIDAD
=============================================*/

$("select[name='DataTables_Table_0_length']").change(function(){

	cargarImagenesProductos()

})

/*=============================================
CARGAMOS LAS IMÁGENES CUANDO INTERACTUAMOS CON EL FILTRO DE ORDENAR
=============================================*/

$(".sorting").click(function(){

	cargarImagenesProductos()

})
