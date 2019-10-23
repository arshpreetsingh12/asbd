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

	
 
// Add and Edit page 


$('.selectall').click(function() {
    if ($(this).is(':checked')) {
        $('div input').attr('checked', true);
    } else {
        $('div input').attr('checked', false);
    }
});




   $(document).ready(function() {
        $("#multiple").click(function(){
            var page_id = [];
            var status = 'false';
            $.each($("input[name='checked_groups']:checked"), function(){
                page_id.push($(this).val());
            });

           
           console.log(page_id);
           $.ajax({
		    url: "change_multiple",
		    type: "GET", 
		    data: {'page_id':page_id , 'status':status},
		    success: function(data) {
		    	console.log(data);
				window.location.reload();
    		}
    	});
        });
    });



   $(document).ready(function() {
        $("#multiple_change").click(function(){
            var page_id = [];
            var status = 'true';
            $.each($("input[name='checked_groups']:checked"), function(){
                page_id.push($(this).val());
            });

           
           console.log(page_id);
           $.ajax({
		    url: "change_multiple",
		    type: "GET", 
		    data: {'page_id':page_id , 'status':status},
		    success: function(data) {
		    	console.log(data);
				window.location.reload();
    		}
    	});
        });
    });