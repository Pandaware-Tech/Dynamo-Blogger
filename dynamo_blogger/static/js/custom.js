let toggleBtn = document.getElementById("toggelBtn");
let navAside = document.getElementById("nav-aside");


// Click event listener
toggleBtn.addEventListener("click", toggleNavAside);


// Function to toggle nav aside
function toggleNavAside() {

    // Toggle aside nav
    navAside.classList.toggle("top_350");
}