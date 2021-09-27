let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    const slides = document.getElementsByClassName("design");
    const dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
    setTimeout(showSlides, 2500);
}


window.addEventListener("resize", () => {
    let height = getComputedStyle(document.getElementsByClassName("designs")[0]).height;
    let x = getComputedStyle(document.getElementsByClassName("designs")[0]).top;
    height = (parseInt(height) / 2 + parseInt(x) + 16).toString() + "px";
    document.getElementsByClassName("slider-controller")[0].style.top = height;
});

window.addEventListener("load", () => {
    let height = getComputedStyle(document.getElementsByClassName("designs")[0]).height;
    let x = getComputedStyle(document.getElementsByClassName("designs")[0]).top;
    height = (parseInt(height) / 2 + parseInt(x) + 16).toString() + "px";
    document.getElementsByClassName("slider-controller")[0].style.top = height;
});