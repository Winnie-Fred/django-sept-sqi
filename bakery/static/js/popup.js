document.addEventListener("DOMContentLoaded", function () {
    const popUpElem = document.getElementById("popUp");
    console.log(popUpElem);
    popUpElem.style.visibility = "visible";

    const closeBtn = document.getElementsByClassName("close")[0]
    closeBtn.addEventListener("click", function () {
        popUpElem.style.visibility = "hidden";
    })
})