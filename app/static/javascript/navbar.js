// Script for responsive navbar

$(".hamburger").click(function(){
    $(".navigation").toggleClass("navigation-active")

    $(".first-line").toggleClass("rotate-down")
    $(".third-line").toggleClass("rotate-up")
})
