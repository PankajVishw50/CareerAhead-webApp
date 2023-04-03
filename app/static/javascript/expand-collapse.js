// This script helps in expanding and collapsing the counsellor type filter names in market page

let filter_container = $(".filter-names")
let overflow = filter_container.children().slice(8);
let all_filters = $(".type")
overflow.hide();

let exp_col_btn = $(".expand-collapse")
let filters = []

// This page loaded with "market" url so it needs to set all filter to 0 == none selected
for (let index = 0; index < all_filters.length; index++){
    filters[all_filters[index].value] = 0
}

// This click event listener expand and collapse list of counsellor's types
exp_col_btn.click(function() {
    let value= $(this).val()

    if (value == 1){
        overflow.show();
        $(this).val(0).text("collapse...");
    }
    else{
        overflow.hide();
        $(this).val(1).text("expand...");
    }

})


// This click event listener toggle value of clicked counsellor type button to 0 or 1 respectively and changes styling
all_filters.click(function(){
    if (filters[$(this).val()] === 0){
        filters[$(this).val()] = 1
        $(this).css("background", getComputedStyle(this).getPropertyValue("--border-light-blue"))
    }
    else if (filters[$(this).val()] === 1){
        filters[$(this).val()] = 0
        $(this).css("background", "#fafafa")
    }
})


















