$(document).ready(function(){
    $('body > div:not(#contact-form)').on('click', function(e) {
	var target  = $(e.target);
	if (!target.is('#contact-link') && !target.is('#footer-logo') &&
	    !target.is('#blog-link') && !target.is('#banner') &&
	    !target.is('#fullname-home') && !target.is('#default-home')) {
	    $('#skip-text-container').hide();
	    $('.wrapper').css('cursor', 'auto');
	    $('#background-container').fadeOut(300, function () {
		$(this).remove();
		$('#hidden-by-slideshow').show();
	    });
	    $('.wrapper').animate( {backgroundColor: $('.wrapper').data('background')} , 300);
	}
    });
});
