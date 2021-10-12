function highlight(element) {
    element.style.color = "#aaa";
    element.style.textDecoration = "none";
}

function backward(element) {
    element.style.color = "black";
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