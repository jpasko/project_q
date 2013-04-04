$(document).ready(function(){
    var jqXHR = null;

    $('#fileupload').fileupload({
	dataType: 'json',
	acceptFileTypes: /(\.|\/)(gif|bmp|jpe?g|png)$/i,
	maxFileSize: 2 * 1024 * 1024,
	progressall: function (e, data) {
	    var progress = parseInt(data.loaded / data.total * 100, 10);
	    $('#progress .bar').css(
		'width',
		progress + '%'
	    );
	},
	progress: function (e, data) {
            $.each(data.files, function (index, file) {
		var progress = parseInt(data.loaded / data.total * 100, 10);
		$('#individual-progress .individual-bar').css(
		    'width',
		    progress + '%'
		);
            });
	},
	add: function (e, data) {
            jqXHR = data.submit();
	    var filename = data.files[0].name;
	    data.context = $('<p/>').text(filename).appendTo($('#indicator'));
	    data.context.attr('id', filename);
	    data.submit();
	},
	done: function (e, data) {

	},
	fail: function (e, data) {
            $.each(data.files, function (index, file) {
		$('#loader').hide();
		$('#prog_rate').text("There was some error uploading the picture.")
            });
	}
    });
    $('button.cancel').click(function (e) {
	jqXHR.abort();
    });
});
