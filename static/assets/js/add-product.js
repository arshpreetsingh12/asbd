

 // add product  

$(document).ready(function() {
	var product_id=0;
   $("#add_new_product").click(function(){ 
	var add_div = '';
	var product_name ='';
	var width = '';
	var height = '';
	var weight = '';
	var price = '';
	var process_time = '';
	var backdrop_type = '';



	product_id= product_id+1

	add_div =   '<table class="table" id="product_box'+product_id+'">' + '<thead>' +
				'<tr>' +
     
		      '<th scope="col">Product Name</th>'+
		      '<th scope="col">Dimension (W / H)</th>' +
		     '<th scope="col">Weight</th>' +
		      '<th scope="col">Price</th>'+
		     '<th scope="col">Process Time</th>' +
		      '<th scope="col">Type of Backdrop</th>' +
		    '</tr>' +
		 '</thead>' +
		  '<tbody>' +
		    '<tr>' +
		      
		      '<td><input type="text" class="form-control" id="product_name'+product_id+'" name="product_name'+product_id+'" placeholder=""></td>' +
		      '<td class="d-flex price_asbd"><span><input type="text" id="width'+product_id+'" name="width'+product_id+'" class="form-control" placeholder="">' + 
		     '</span>' +
		        '<span class="ml-2"><input type="text" class="form-control" id="height'+product_id+'" name="height'+product_id+'" placeholder="">' + '</span>' +
		      '</td>' +
		      '<td class="price_asbd"><input type="text" class="form-control" id="weight'+product_id+'" name="weight'+product_id+'" placeholder="">' + '</td>' +
		      '<td class="price_asbd"><input type="text" class="form-control" id="price'+product_id+'" name="price'+product_id+'" placeholder="">' + '</td>' +
		      '<td class="price_asbd"><input type="text" class="form-control" id="process_time'+product_id+'" name="process_time'+product_id+'" placeholder="">' + '</td>' +
		      '<td class="d-flex align-items-center">' + '<div class="form-check">' +
		            '<input class="form-check-input" type="radio" id="backdrop_type'+product_id+'" name="backdrop_type'+product_id+'" value="Regular">' + 
		            '<label class="form-check-label" for="exampleRadios1">'+
		            'Regular' + '</label>' +
		          '</div>' +
		        '<div class="form-check ml-3">' +
		            '<input class="form-check-input" type="radio" id="backdrop_type'+product_id+'" name="backdrop_type'+product_id+'" value="Gree">' +
		            '<label class="form-check-label" for="exampleRadios1">'+ 'Gree' +
		            '</label>' +
		          '</div>' + 
		        '</td>' +
		      
		    '</tr>' +
		   
		  '</tbody>' +
		'</table>' ;
		$("#add_div").append(add_div);

		$('#total_product_boxes').val(product_id);

})

});

