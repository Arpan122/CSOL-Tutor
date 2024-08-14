$(document).ready(function() {

    //Home screen typing text
    var elems = $(".typeText").data('txt')
    if (elems){    
        elems = elems.split(',')

        $(".typeText").each(function () {
            var $this = $(this);
            $this.typed({
                strings: elems,
                typeSpeed: 75, // typing speed
                backDelay: 3000 // pause before backspacing
            })
        })
    }

});