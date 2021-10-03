function selectItem() {
    const selected_elements = document.getElementsByClassName("selected");
    if (selected_elements.length == 0) {
        const classes = ["desc", "details", "how-to-use", "product-video"]
        for (let i = 0; i < classes.length; i++) {
            const element = document.getElementsByClassName(classes[i]);
            if (element.length > 1) {
                element[0].classList.add("selected");
                element[1].style.display = "block";
                break;
            }
        }
    }
}

selectItem();

function preview(element) {
    const class_list = element.classList;
    const selected_element = document.getElementsByClassName("selected")[0];
    selected_element.classList.remove("selected");
    document.getElementsByClassName(selected_element.classList[0])[1].style.display = "none";
    element.classList.add("selected");
    if (class_list[0] == "desc") {
        document.getElementsByClassName("desc")[1].style.display = "block";
    } else if (class_list[0] == "details") {
        document.getElementsByClassName("details")[1].style.display = "block";
    } else if (class_list[0] == "how-to-use") {
        document.getElementsByClassName("how-to-use")[1].style.display = "block";
    } else if (class_list[0] == "product-video") {
        document.getElementsByClassName("product-video")[1].style.display = "block";
    }
}

let index = 0;

function slideshow() {
    const images = document.getElementsByClassName("product-img");
    if (index < 0) {
        index = images.length - 1;
    } else if (index >= images.length) {
        index = 0;
    }
    let i;
    for (i = 0; i < images.length; i++) {
        if (i == index) {
            continue;
        } else {
            images[i].style.display = "none"
        }
    }
    images[index].style.display = "block"
}

function plus(val) {
    index += val;
    slideshow();
}

slideshow();

document.getElementById("increase").addEventListener("click", function(event) {
    event.preventDefault();
    const quantity_element = document.getElementsByClassName("num")[0];
    const quantity_val = parseInt(quantity_element.innerHTML) + 1;
    quantity_element.innerHTML = quantity_val.toString();
});

document.getElementById("decrease").addEventListener("click", function(event) {
    event.preventDefault();
    const quantity_element = document.getElementsByClassName("num")[0];
    const quantity_val = parseInt(quantity_element.innerHTML) - 1;
    if (quantity_val >= 1) {
        quantity_element.innerHTML = quantity_val.toString();
    }
});

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
    const quantity = parseInt(document.getElementsByClassName("num")[0].innerHTML);
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
        /* redirect to cart detail page */
        window.location = element.getAttribute("redirect-url");
    });
}