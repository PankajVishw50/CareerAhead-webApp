// Main script which request for counsellor using ajax to server

let counsellor_container = $(".counsellor-container");
let filter_submit_button = $("#filter-submit");
let nav_input = $(".page-input-field")
let something;


$(document).ready(function () {
    let load_widget, previous_button, next_button, gender;

    load_widget = $(".loading");
    previous_button = $(".nav-previous-btn")
    next_button = $(".nav-next-btn")
    gender = 0;

    set_nav(1)

    // Activate when user clicks previous navigation button
    previous_button.click(function () {
        load_counsellors(1, get_nav());
    })

    // Activate when user clicks next navigation button
    next_button.click(function () {
        load_counsellors(2, get_nav());
    })

    // This even listener is called when user presses submit button
    filter_submit_button.click(function () {
        load_counsellors(0, 1);
    })

    // Main function to request and load counsellor to page
    /*
    It accept 2 arguments -
    direction: This tells in which direction user wants to navigate.
                0 for no change in page
                1 for previous page
                2 for next page
     */
    function load_counsellors(direction, current_page) {

        counsellor_container.hide()
        flash_placeholder.hide();

        load_widget.css("display", "flex")

        if ($("input[name=gender]:checked").val()) {
            gender = $("input[name=gender]:checked").val();
        }

        console.log("Value of gender is ")
        console.log(gender)

        $.ajax({
            type: "post",
            url: "/get-info",
            contentType: "application/json",
            data: JSON.stringify({
                type: filters,
                gender: gender,
                name: $("input[name=name]").val(),
                price_upto: slider.val()
            }),

            success: function (response) {
                let next_page;
                console.log(response)
                if (current_page < 0) {
                    next_page = navigate_page_util(direction, response["page"], response["maxPage"]);
                } else {
                    next_page = navigate_page_util(direction, current_page, response["maxPage"])
                }

                /*
                First condition checks if current page same as next demanding page
                Second condition is because when we load the page first condition will be true,
                but we don't have current_page data
                 */
                if (next_page === response["page"] && direction !== 0) {
                    load_widget.hide();
                    counsellor_container.show();
                    return 0;
                }

                $.ajax({
                    type: "post",
                    url: "/get-counsellors",
                    contentType: "application/json",
                    data: JSON.stringify({
                        page: next_page,
                        base: 10
                    }),
                    success: function (request_2) {
                        load_widget.hide();
                        counsellor_container.html(request_2);
                        counsellor_container.fadeIn(500);
                        set_nav(next_page);
                        something = request_2

                        if (something.length < 10) {
                            flash("No counsellor with this specification.Please try to change filters.")
                        }

                    }
                })
            }
        });
    }

    // This function helps in finding legit next and previous pages
    function navigate_page_util(direction, cur_page, max_page) {
        if (direction === 0) {
            return cur_page
        } else if (direction === 1) {
            if (cur_page <= 1) {
                flash("No previous page available")
                return cur_page
            }
            return cur_page - 1
        } else if (direction === 2) {
            if (cur_page >= max_page) {
                flash("No more counsellors")
                return cur_page
            }
            console.log("cur_page + 1 is returning ", cur_page)
            return cur_page + 1
        }
    }

    // This function sets page number to navigation element in our page
    function set_nav(cur_page) {
        nav_input.val(cur_page)
    }

    // Retrieve page number from nav element
    function get_nav() {
        return parseInt(nav_input.val());
    }

    load_counsellors(0, get_nav())
})

