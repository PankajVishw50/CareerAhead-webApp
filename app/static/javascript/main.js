

let flash_placeholder = $(".flash-placeholder");

// Helps in flashing message without reloading page
function flash(message) {
    console.log("inside flash")
    flash_placeholder.show();
    $(".flash-placeholder-data").text(message)
}
