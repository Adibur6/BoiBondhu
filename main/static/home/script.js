searchForm = document.querySelector(".search-form");

setTimeout(() => {
  const msg = document.getElementById("msg");
  if (msg==null) return;
  // 👇️ removes element from DOM
  msg.style.display = "none";

  // 👇️ hides element (still takes up space on page)
  // box.style.visibility = 'hidden';
}, 3000); // 👈️ time in milliseconds

document.querySelector("#search-btn").onclick = () => {
  searchForm.classList.toggle("active");
};

let loginForm = document.querySelector(".login-form-container");

document.querySelector("#login-btn").onclick = () => {
  loginForm.classList.toggle("active");
};

document.querySelector("#close-login-btn").onclick = () => {
  loginForm.classList.remove("active");
};

window.onscroll = () => {
  searchForm.classList.remove("active");

  if (window.scrollY > 80) {
    document.querySelector(".header .header2").classList.add("active");
  } else {
    document.querySelector(".header .header2").classList.remove("active");
  }
};

window.onload = () => {
  if (window.scrollY > 80) {
    document.querySelector(".header .header2").classList.add("active");
  } else {
    document.querySelector(".header .header2").classList.remove("active");
  }

  fadeOut();
};

function loader() {
  const c=document.querySelector(".loader-container");
  if (c==null) return;
  c.classList.add("active");
}

function fadeOut() {
  setTimeout(loader, 4000);
}

var swiper = new Swiper(".books-slider", {
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 3000,
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

let signupForm = document.querySelector(".signup-form-container");

document.querySelector("#signup-btn").onclick = () => {
    if(signupForm==null) return;
  signupForm.classList.toggle("active");
};

document.querySelector("#signup-btn2").onclick = () => {
  loginForm.classList.remove("active");
  signupForm.classList.toggle("active");
};

document.querySelector("#close-signup-btn").onclick = () => {
  signupForm.classList.remove("active");
};
function submit_form() {
  document.search.submit();
}
