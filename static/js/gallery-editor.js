$(document).ready(function(){
    $("#trigger-editable-title").on("click", function() {
	if ($("#title-input").is(":visible")) {
	    $("#cancel-title").click();
	} else {
	    if ($("#valid-title").length) {
		$("#valid-title").hide();
		$("#title-input").val($("#valid-title").text());
	    } else {
		$("#empty-title").hide();
	    }
	    $("#title-input").show();
	    $("#save-title").show();
	    $("#cancel-title").show();
	}
    });
    $("#cancel-title").on("click", function() {
	$("#title-input").hide();
	$("#save-title").hide();
	$("#cancel-title").hide();
	$("#editable-title").find("p").show();
    });
    $("#save-title").on("click", function() {
	$("#title-input").hide();
	$("#save-title").hide();
	$("#cancel-title").hide();
	if ($("#title-input").val()) {
	    if ($("#empty-title").length) {
		$("#empty-title").remove();
	    }
	    if (!$("#valid-title").length) {
		$("#editable-title").append('<p id="valid-title"></p>');
	    }
	    $("#valid-title").show();
	    $("#valid-title").text($("#title-input").val());
	} else {
	    if (!$("#empty-title").length) {
		$("#editable-title").append('<p id="empty-title"><em>Currently empty</em></p>');
	    }
	    if ($("#valid-title").length) {
		$("#valid-title").remove();
	    }
	    $("#empty-title").show();
	}
	$.ajax({
	    type: "POST",
	    url: "/update_gallery/" + $("#gallery-pk").text() + "/",
	    data: {'title': $("#title-input").val()},
	    success: function(data) {
		$("#ajax-alert > p").remove();
		if (!data.success) {
		    $("#ajax-alert").show();
		    $("#ajax-alert").append("<p><strong>Error: </strong>" + data['message'] + "</p>");
		} else {
		    $("#ajax-alert").hide();
		}
	    }
	});
    });

    $("#trigger-editable-description").on("click", function() {
	if ($("#description-textarea").is(":visible")) {
	    $("#cancel-description").click();
	} else {
	    if ($("#valid-description").length) {
		$("#valid-description").hide();
		$("#description-textarea").val(formattedText($("#valid-description")));
	    } else {
		$("#empty-description").hide();
	    }
	    $("#description-textarea").show();
	    $("#save-description").show();
	    $("#cancel-description").show();
	}
    });
    $("#cancel-description").on("click", function() {
	$("#description-textarea").hide();
	$("#save-description").hide();
	$("#cancel-description").hide();
	$("#editable-description").find("p").show();
    });
    $("#save-description").on("click", function() {
	$("#description-textarea").hide();
	$("#save-description").hide();
	$("#cancel-description").hide();
	if ($("#description-textarea").val()) {
	    if ($("#empty-description").length) {
		$("#empty-description").remove();
	    }
	    if (!$("#valid-description").length) {
		$("#editable-description").append('<p id="valid-description"></p>');
	    }
	    $("#valid-description").show();
	    $("#valid-description").html(formatAsHTML($("#description-textarea").val()));
	} else {
	    if (!$("#empty-description").length) {
		$("#editable-description").append('<p id="empty-description"><em>Currently empty</em></p>');
	    }
	    if ($("#valid-description").length) {
		$("#valid-description").remove();
	    }
	    $("#empty-description").show();
	}
	$.ajax({
	    type: "POST",
	    url: "/update_gallery/" + $("#gallery-pk").text() + "/",
	    data: {'description': $("#description-textarea").val()},
	    success: function(data) {
		$("#ajax-alert > p").remove();
		if (!data.success) {
		    $("#ajax-alert").show();
		    $("#ajax-alert").append("<p><strong>Error: </strong>" + data['message'] + "</p>");
		} else {
		    $("#ajax-alert").hide();
		}
	    }
	});
    });

    $("#trigger-editable-thumbnail").on("click", function() {
	$("#thumbnail-details").toggle();
	$("#thumbnail-form").toggle();
    });
    $("#cancel-thumbnail").on("click", function() {
	$("#thumbnail-details").toggle();
	$("#thumbnail-form").toggle();
    });

    $('#id_thumbnail').change(function() {
	$('#id_thumbnail_styled').val($(this).val().replace("C:\\fakepath\\", ""));
    });

    $('#delete-current').click(function() {
	if (!$(this).hasClass('active')) {
	    $(this).addClass('active btn-danger');
	    $(this).removeClass('btn-default');
	    $(this).find('i').addClass('icon-white');
	    $('#id_thumbnail').val('');
	    $('#id_thumbnail_styled').val('');
	    $('#input-delete-current').val('True');
	} else {
	    $(this).addClass('btn-default');
	    $(this).removeClass('active btn-danger');
	    $(this).find('i').removeClass('icon-white');
	    $('#input-delete-current').val('False');
	}
    });

    function formattedText(element) {
	var str = $(element).html();
	var regex = /<br\s*[\/]?>/gi;
	return str.replace(regex, "\n");
    }

    function formatAsHTML(text) {
	var htmls = [];
	var lines = text.split(/\n/);
	var tmpDiv = jQuery(document.createElement('div'));
	for (var i = 0 ; i < lines.length ; i++) {
            htmls.push(tmpDiv.text(lines[i]).html());
	}
	return htmls.join("<br>");
    }
});