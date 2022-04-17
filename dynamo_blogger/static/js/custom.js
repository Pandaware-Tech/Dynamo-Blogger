let toggleBtn = document.getElementById("toggelBtn");
let closeAsideNavBtn = document.querySelector(".nav-aside-close");
let navAside = document.getElementById("nav-aside");


// Click event listener
toggleBtn.addEventListener("click", toggleNavAside);
closeAsideNavBtn.addEventListener("click", closeNavAside);

// Function to toggle nav aside
function toggleNavAside() {

    // Toggle aside nav
    navAside.classList.toggle("top_350");
}

// Function to close nav aside
function closeNavAside() {

    // RHide aside nav
    navAside.classList.remove("top_350");
}