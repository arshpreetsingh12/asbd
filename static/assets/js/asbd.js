$(document).ready(function(){
			var selectedClass = "";
			$(".filter").click(function(){
				selectedClass = $(this).attr("data-rel");
				$("#gallery").fadeTo(100, 0.1);
				$("#gallery div").not("."+selectedClass).fadeOut().removeClass('animation');
				setTimeout(function() {
					$("."+selectedClass).fadeIn().addClass('animation');
					$("#gallery").fadeTo(300, 1);
				}, 300);
			});
		});
		


	$("#other_search").on("click", function(e){
	if ( $('.other_pages_search').css('display') == 'none'){
		$(".other_pages_search").css('display','block');
		$(".other_pages_search").show(50);
		 e.stopPropagation();
		   
	}
	else{
		$(".other_pages_search").css('display','none');
	}
	});


$(".other_pages_search").click(function(e){
    e.stopPropagation();
});

$(document).click(function(){
    $(".other_pages_search").hide();
});



$(document).ready(function(){
			var selectedClass = "";
			$(".filter").click(function(){
				selectedClass = $(this).attr("data-rel");
				$("#gallery").fadeTo(100, 0.1);
				$("#gallery div").not("."+selectedClass).fadeOut().removeClass('animation');
				setTimeout(function() {
					$("."+selectedClass).fadeIn().addClass('animation');
					$("#gallery").fadeTo(300, 1);
				}, 300);
			});
			var textAreas = document.getElementsByTagName('textarea');

Array.prototype.forEach.call(textAreas, function(elem) {
    elem.placeholder = elem.placeholder.replace(/\\n/g, '\n');
});
		});





$(document).ready(function() {
   $('#example').DataTable();
} );
		$("#other_search").on("click", function(e){
	if ( $('.other_pages_search').css('display') == 'none'){
		$(".other_pages_search").css('display','block');
		$(".other_pages_search").show(50);
		 e.stopPropagation();
		   
	}
	else{
		$(".other_pages_search").css('display','none');
	}
	});


$(".other_pages_search").click(function(e){
    e.stopPropagation();
});

$(document).click(function(){
    $(".other_pages_search").hide();
});

// ===================================

  // match password and email 

$("#registration_form").submit(function(){
  var email = $.trim($('#email').val());
  var remail = $.trim($('#remail').val());
  var password = $.trim($('#password').val());
  var cpassword = $.trim($('#confirm_password').val());
   if (email != remail) {
      $("#mismatch_email").css("display",'block');
      return false;   
    }
    else if(password != cpassword) {
      $("#mismatch_pass").css("display",'block');   
      return false;
    }
    else{
      return true;
    }
    return false;
});



// pagesapp js ====================	
 
// select all checkboxes


function selectAllBoxes(source) {
	var checkboxes = document.querySelectorAll('input[type="checkbox"]');
	for (var i = 0; i < checkboxes.length; i++) {
		if (checkboxes[i] != source)
			checkboxes[i].checked = source.checked;
		}
}


   
// // Create url on add page
$(document).ready(function() {
	$("#page_title").on('keyup',function(){
		var title=$(this).val();
		var url=title.replace(/ /g,"-");
		$("#page_url").val(url);
	})
	
	// Create  page url on edit page
	$("#edit_page_title").on('keyup',function(){
		var title=$(this).val();
		var url=title.replace(/ /g,"-");
		$("#edit_page_url").val(url);
	})
	});


 // delete- single-page
	$("#manage_page_tbody").on('click','.delete-page',function(){
			var page_id=$(this).attr("data-id");
			$.ajax({
				url: "delete_page",
				method: "GET",
				data:{
					"page_id":page_id
				}, 
			success: function(result){
				if (result.status==true) {
					$("#manage_page_tbody").load(location.href+" #manage_page_tbody>*", "");
				}
			}
		})
      });


		// #change single page status 
	    $("#manage_page_tbody").on('click','.page-status',function(){
      		var page_id=$(this).attr("data-id");
			$.ajax({
				url: "single_page_status",
				method: "GET",
				data:{
					"page_id":page_id
				}, 
			success: function(result){
				if (result.status==true) {
					$("#manage_page_tbody").load(location.href+" #manage_page_tbody>*", "");
				}
			}
		})
	});


  // change all pages status
	  $(".all-page-status").click(function(){
			var status=$(this).attr('data-id');
			var selected_pages = [];
			$.each($("input[name='select_page']:checked"), function(){
				selected_pages.push($(this).val());
				});
			console.log(selected_pages);
			$.ajax({
				url: "selected-pages-status",
				method: "POST",
				data:{
					"selected_pages":selected_pages,
					"status":status,
					"csrfmiddlewaretoken":token
				}, 
				success: function(result){
					if (result.status==true) {
						$("#manage_page_tbody").load(location.href+" #manage_page_tbody>*", "");
					}
				}
			})
	});