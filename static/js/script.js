var currentView = 1,
    minView = 1,
    maxView = 6,
    frame = document.getElementById('frame');

function changeViewNext() {
    if (currentView >= minView && currentView < maxView) {
        currentView++;
        frame.src = currentView + '.html';
    }
}

function changeViewPrev() {
    if (currentView <= maxView && currentView > minView) {
        currentView--;
        frame.src = currentView + '.html';
    }
}


(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }
            form.classList.add('was-validated')
        }, false)
    })
})()


function store() {
    var name = document.getElementById("demo-hide");
    window.localStorage.setItem("username", name.value);
}

window.onload = function displayN() {

    document.getElementById("name").innerHTML =
        "Hello " + localStorage.getItem("username");
};