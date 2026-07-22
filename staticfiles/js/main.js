// ======================
// HEADER
// ======================

const header = document.querySelector(".header");

function updateHeader() {

    if (!header) return;

    const isHome = document.body.classList.contains("home");

    if (isHome) {

        if (window.scrollY > 80) {
            header.classList.add("active");
        } else {
            header.classList.remove("active");
        }

    } else {

        header.classList.add("active");

    }

}

window.addEventListener("scroll", updateHeader);
window.addEventListener("load", updateHeader);


// ======================
// SWIPER
// ======================

if (document.querySelector(".propertySwiper")) {

    new Swiper(".propertySwiper", {

        slidesPerView: 3,
        spaceBetween: 30,
        loop: false, // موقتاً false

        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },

        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },

        breakpoints: {

            0: {
                slidesPerView: 1,
            },

            768: {
                slidesPerView: 3,
            },

            1200: {
                slidesPerView: 2,
            }

        }

    });

}


// ======================
// BACK TO TOP
// ======================

const backToTop = document.getElementById("backToTop");

if (backToTop) {

    window.addEventListener("scroll", () => {

        if (window.scrollY > 400) {
            backToTop.classList.add("show");
        } else {
            backToTop.classList.remove("show");
        }

    });

    backToTop.addEventListener("click", () => {

        window.scrollTo({

            top: 0,
            behavior: "smooth"

        });

    });

}


// ==========================
// SCROLL REVEAL
// ==========================

const reveals = document.querySelectorAll(".reveal");

function revealSections() {

    reveals.forEach((section) => {

        const top = section.getBoundingClientRect().top;

        if (top < window.innerHeight - 120) {
            section.classList.add("active");
        }

    });

}

window.addEventListener("scroll", revealSections);
window.addEventListener("load", revealSections);
// ======================
// MOBILE MENU
// ======================

const menuToggle = document.getElementById("menuToggle");
const navMenu = document.getElementById("navMenu");


if(menuToggle && navMenu){

    menuToggle.addEventListener("click", ()=>{

        navMenu.classList.toggle("active");

    });

}