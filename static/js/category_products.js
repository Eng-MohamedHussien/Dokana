function highlight(element) {
    const product_name = element.querySelector("span");
    product_name.style.color = "#aaa";
}

function backward(element) {
    const product_name = element.querySelector("span");
    product_name.style.color = "black";
}


window.addEventListener("load", productShowhandler);
window.addEventListener("resize", productShowhandler);

function productShowhandler() {
    if (document.getElementsByClassName("products").length > 0) {
        const main_container = document.querySelector(".container");
        const products_container = document.querySelector(".products");
        const full_width = main_container.getBoundingClientRect().width;
        const width = (200 + 2 * 1 + 2 * 16 + 2 * 1) + 2 * 8;
        let no_elements = Math.trunc(full_width / width);
        if (no_elements > document.getElementsByClassName("product").length) {
            no_elements = document.getElementsByClassName("product").length;
        }
        products_container.style.width = `${no_elements * width}px`;
    }
}


function showPagination() {
    if (document.getElementsByClassName("pagination").length > 0) {
        const page_numbers = document.getElementsByClassName("page-link");
        const index = parseInt(document.getElementsByClassName("current")[0].innerHTML);
        let i;
        for (i = 0; i < page_numbers.length; i++) {
            page_numbers[i].style.display = "none";
        }

        let max_pages;
        if (page_numbers.length < 5) {
            max_pages = page_numbers.length;
        } else {
            max_pages = 5;
        }

        if (((index - 1) + max_pages) <= page_numbers.length) {
            i = index - 1;
        } else {
            i = index % max_pages;
        }

        for (let j = 0; j < max_pages; j++) {
            page_numbers[i + j].style.display = "inline-block";
        }
    }
}

showPagination();

function toggle() {
    const mobile_menu = document.getElementsByClassName("mobile-menu")[0];
    if (mobile_menu.style.display == "none") {
        mobile_menu.style.display = "block";
    } else {
        mobile_menu.style.display = "none";
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function add_to_cart(element, id) {
    const url = element.getAttribute("data-url");
    const data = { 'id': id, 'quantity': 1 };
    const props = {
        method: 'POST',
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        mode: "same-origin",
        body: JSON.stringify(data)
    };

    fetch(url, props).then(function(response) {
        /* redirect to cart detail page */
        window.location = element.getAttribute("redirect-url");
    });
}