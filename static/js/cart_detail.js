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

function remove(element, id) {
    const url = element.getAttribute("data-url");
    const redirect = element.getAttribute("redirect-url");
    const data = { 'id': id };
    const props = {
        method: 'POST',
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        mode: "same-origin",
        body: JSON.stringify(data)
    };

    fetch(url, props).then(function() {
        window.location = redirect;
    });
}

function update_quantity(element, id, val) {
    const url = element.getAttribute("data-url");
    const redirect = element.getAttribute("redirect-url");
    const quantity = parseInt(document.getElementsByClassName(id.toString())[0].innerHTML) + val;
    if (quantity >= 1) {
        const data = { 'id': id, 'quantity': quantity };
        const props = {
            method: 'POST',
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            mode: "same-origin",
            body: JSON.stringify(data)
        };

        fetch(url, props).then(function() {
            window.location = redirect;
        });
    }
}

if (document.getElementsByClassName("cart-empty").length == 0) {
    document.getElementsByTagName("main")[0].style.position = "static";
} else {
    document.getElementsByTagName("main")[0].style.position = "relative";
}