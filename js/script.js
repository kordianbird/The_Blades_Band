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