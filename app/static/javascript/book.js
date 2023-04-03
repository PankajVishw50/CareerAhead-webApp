
let book = $(".book-btn")
let counsellorMail = $("#mail")

// This function helps in sending booking request to server
book.click(function(){
    $.ajax({
        type: "GET",
        url: "/book",
        contentType: "application/json",
        data: {
            counsellorMail: counsellorMail.text()
        },
        success: function(response){
            flash(response)
        },
        error: function(response){
            if (response.status == 403){
                flash("You don't have Permission to perform this feature")
                return
            }
            flash("Error:" + response.responseText)
        }
    })
})