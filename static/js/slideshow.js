$(document).ready(function(){
    $('body > div:not(#contact-form)').on('click', function(e) {
	var target  = $(e.target);
	if (!target.is('#contact-link') && !target.is('#footer-logo') && !target.is('#blog-link')) {
	    $('#skip-text-display').hide();
	    $('#background-container').fadeOut(300, function () {
		$(this).remove();
		$('.wrapper').css('background', $('.wrapper').data('background'));
		$('.wrapper').css('cursor', 'auto');
		$('#hidden-by-slideshow').show();
	    });
	}
    });
});
