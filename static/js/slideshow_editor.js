$(document).ready(function(){
    var options = {
	success: function(data) {
	    var number = data.number;
	    var remove_id = '#remove-image-' + number;
	    var select_id = '#select-image-' + number;
	    if (data.success) {
		$(remove_id).siblings('.loading-image').remove();
		$(remove_id).css('display', 'inline');
		$(remove_id).before('<img class="image-preview" src="' + data.url + '">');
	    } else {
		$(select_id).siblings('.loading-image').remove();
		$(select_id).css('display', 'inline');
		$('#error-modal').modal('show');
	    }
	}
    };
    $('#ajax-form').ajaxForm(options);

    // Upload images
    $('.select-image').on('click', function() {
	var image_number = $(this).data('number');
	$('#ajax-form').attr('action', '/upload_slideshow_image/' + image_number + '/');
	$('#ajax-form').data('number', image_number);
	$('#image-input').click();
    });

    $('#image-input').change(function() {
	var image_number = $('#ajax-form').data('number');
	$('#select-image-' + image_number).css('display', 'none');
	$('#select-image-' + image_number).before('<img class="loading-image" src="https://s3.amazonaws.com/folio24/static/img/loading_slideshow.gif">');
	$('#ajax-form').submit();
    });

    // Remove images
    $('.remove-image').on('click', function() {
	var image_number = $(this).data('number');
	var remove_id = '#remove-image-' + image_number;
	var select_id = '#select-image-' + image_number;
	var url = '/delete_slideshow_image/' + image_number + '/';

	$(this).siblings('.image-preview').remove();
	$(this).before('<img class="removing-image" src="https://s3.amazonaws.com/folio24/static/img/loading_slideshow.gif">');
	$(this).prop('disabled', true);

	$.ajax({
	    type: "POST",
	    url: url,
	    success: function() {
		$(select_id).css('display', 'inline');
		$(remove_id).siblings('.removing-image').remove();
		$(remove_id).css('display', 'none');
		$(remove_id).prop('disabled', false);
	    }
	});
    });

    // Enable/Disable the slideshow.
    $("#slideshow-on").on("click", function() {
	if (!$(this).hasClass("active")) {
	    $(this).removeClass("btn-default");
	    $(this).addClass("btn-info active");
	    $("#slideshow-off").removeClass("btn-danger active");
	    $("#slideshow-off").addClass("btn-default");

	    $.ajax({
		type: "POST",
		url: "/configure_slideshow/",
		data: {'enable_slideshow': 'True'}
	    });
	}
    });
    $("#slideshow-off").on("click", function() {
	if (!$(this).hasClass("active")) {
	    $(this).removeClass("btn-default");
	    $(this).addClass("btn-danger active");
	    $("#slideshow-on").removeClass("btn-info active");
	    $("#slideshow-on").addClass("btn-default");

	    $.ajax({
		type: "POST",
		url: "/configure_slideshow/",
		data: {'enable_slideshow': 'False'}
	    });
	}
    });

   // Toggle fast vs. slow slideshow.
    $("#slideshow-fast").on("click", function() {
	if (!$(this).hasClass("active")) {
	    $(this).removeClass("btn-default");
	    $(this).addClass("btn-info active");
	    $("#slideshow-slow").removeClass("btn-info active");
	    $("#slideshow-slow").addClass("btn-default");

	    $.ajax({
		type: "POST",
		url: "/configure_slideshow/",
		data: {'slow_slideshow': 'False'}
	    });
	}
    });
    $("#slideshow-slow").on("click", function() {
	if (!$(this).hasClass("active")) {
	    $(this).removeClass("btn-default");
	    $(this).addClass("btn-info active");
	    $("#slideshow-fast").removeClass("btn-info active");
	    $("#slideshow-fast").addClass("btn-default");

	    $.ajax({
		type: "POST",
		url: "/configure_slideshow/",
		data: {'slow_slideshow': 'True'}
	    });
	}
    });

    // Change the skip text.
    $('#save-skip-text').on('click', function() {
	$(this).prop('disabled', true);
	$(this).text('Saving...');
	$.ajax({
	    type: "POST",
	    url: "/configure_slideshow/",
	    data: {'skip_text': $('#skip-text').val()},
	    success: function(data) {
		if (data.success) {
		    $('#save-skip-text').text('Saved');
		}
	    }
	});
    });
    $('#skip-text').on('focus', function() {
	$('#save-skip-text').text('Save');
	$('#save-skip-text').prop('disabled', false);
    });
});
