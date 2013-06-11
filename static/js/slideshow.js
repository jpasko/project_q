$(document).ready(function(){
    $('body > div:not(#contact-form)').on('click', function(e) {
	var target  = $(e.target);
	if (!target.is('#contact-link') && !target.is('#footer-logo') &&
	    !target.is('#blog-link') && !target.is('#banner') &&
	    !target.is('#fullname-home') && !target.is('#default-home')) {
	    $('#skip-text-container').remove();
	    $('.wrapper').css('cursor', 'auto');
	    if (!target.is('#about-link')) {
		$('#background-container').fadeOut(200, function () {
		    $(this).remove();
		    $('#hidden-by-slideshow').show();
		});
	    } else if ($('#background-container').is(':visible')) {
		e.preventDefault();
		var $self=$('#about-link');
		$('#background-container').fadeOut(200, function () {
		    $(this).remove();
		    document.location = $self.attr('href');
		});
	    }
	    $('.wrapper').animate( {backgroundColor: $('.wrapper').data('background')} , 200);
	}
    });
});
