searchForm = document.querySelector(".search-form");

document.querySelector("#search-btn").onclick = () => {
  searchForm.classList.toggle("active");
};

function fadeOut() {
  setTimeout(loader, 4000);
}
function submit_form() {
  document.search.submit();
}
setTimeout(() => {
  const msg = document.getElementById("msg");
  if (msg == null) return;
  // 👇️ removes element from DOM
  msg.style.display = "none";

  // 👇️ hides element (still takes up space on page)
  // box.style.visibility = 'hidden';
}, 3000); // 👈️ time in milliseconds
