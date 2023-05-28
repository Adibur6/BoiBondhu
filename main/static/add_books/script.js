setTimeout(() => {
    const msg = document.getElementById('msg');
  
    // 👇️ removes element from DOM
    msg.style.display = 'none';
  
    // 👇️ hides element (still takes up space on page)
    // box.style.visibility = 'hidden';
  }, 3000); // 👈️ time in milliseconds

searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
}

let loginForm = document.querySelector('.login-form-container');

document.querySelector('#login-btn').onclick = () => {
    loginForm.classList.toggle('active');
}

document.querySelector('#close-login-btn').onclick = () => {
    loginForm.classList.remove('active');
}

window.onscroll = () => {

    searchForm.classList.remove('active');

    if (window.scrollY > 80) {
        document.querySelector('.header .header2').classList.add('active');
    } else {
        document.querySelector('.header .header2').classList.remove('active');
    }

}

window.onload = () => {

    if (window.scrollY > 80) {
        document.querySelector('.header .header2').classList.add('active');
    } else {
        document.querySelector('.header .header2').classList.remove('active');
    }

    fadeOut();

}

function loader() {
    document.querySelector('.loader-container').classList.add('active');
}

function fadeOut() {
    setTimeout(loader, 4000);
}

var swiper = new Swiper(".books-slider", {
    loop: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    },
});



