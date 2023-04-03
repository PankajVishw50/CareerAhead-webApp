// Script for price slider in filter panel of market page

let slider = $("#slider")
let start = $(".starting-price")
let end = $(".ending-price")

slider.change(function(){
    set()
})

function set(){
    if (slider.val() === slider.attr("max")){
        end.text("no limits")
        return
    }
    end.text("> " + slider.val() + "$");
}

set();