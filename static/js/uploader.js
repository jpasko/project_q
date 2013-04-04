$(document).ready(function(){
    var jqXHR = null;
    var numFiles = 0;

    $('#fileupload').fileupload({
	dataType: 'json',
	acceptFileTypes: /(\.|\/)(gif|bmp|jpe?g|png)$/i,
	maxFileSize: maxFileSize * 1024 * 1024,
	maxNumberOfFiles: maxNumberOfFiles,
	progress: function (e, data) {
	    var progress = parseInt(data.loaded / data.total * 100, 10);
	    data.context.find('.js-progress').css('width', progress + '%');
	},
	add: function (e, data) {
	    if (data.files[0].size < maxFileSize * 1024 * 1024) {
		numFiles++;
		var file = data.files[0];
		var fileDetails = '<tr><td class="filename-cell">' + file.name + '</td>' +
		    '<td class="progress-cell"><div class="js-progress" style="width: 0%"></div></td>' +
		    '<td class="status-cell">in progress</td></tr>';
		data.context = $(fileDetails).appendTo('#file-status-list');
		jqXHR = data.submit();
	    }
	},
	done: function (e, data) {
	    data.context.find('.status-cell').text('complete');
	},
	fail: function (e, data) {
	    var error = 'failed';
	    if (numFiles > maxNumberOfFiles) {
		error = 'only ' + maxNumberOfFiles + ' images per upload';
	    }
	    data.context.find('.status-cell').text(error);
	},
	stop: function (e, data) {
	    numFiles = 0;
	    window.location.reload(true);
	}
    });
    $('button.cancel').click(function (e) {
	jqXHR.abort();
    });
});
