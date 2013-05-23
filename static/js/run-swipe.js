var swipe = document.getElementById('swipe');
var swipe_nav = document.getElementById('swipe_nav');

window.mySwipe = new Swipe(swipe, {
    speed: 500,
    auto: 5000,
    continuous: true,
    disableScroll: false,
    callback: function(ind, elem) {
	for (var i = 0; i < swipe_nav.childNodes.length; i++) {
	    if (swipe_nav.childNodes[i].className == "colored") {
		swipe_nav.childNodes[i].className = "dull";
	    }
	}
	document.getElementById('swipe_nav_'+ (ind+1)).className = "colored";
    }
});
swipe.onclick = function() {
    mySwipe.next();
}
for (var x = 0; x < swipe_nav.children.length; x++) {
    addSwipeClick(x);		     
}
function addSwipeClick(x) {
    swipe_nav.children[x].onclick = function() {
	mySwipe.slide(x, 500);
    }
}
document.addEventListener("touchstart", function(){}, true);
