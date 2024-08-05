var elems = $(".typeText").data('txt').split(',')

$(".typeText").each(function () {
    var $this = $(this);
    $this.typed({
        strings: elems,
        typeSpeed: 75, // typing speed
        backDelay: 3000 // pause before backspacing
    })
})
