const themeBtn = document.querySelector('.theme-toggler');
const prefersDarkTheme = window.matchMedia('(prefers-color-scheme: dark)');

if (prefersDarkTheme.matches) {
  localStorage.setItem('theme', 'dark');
}

const currentTheme = localStorage.getItem('theme');

if (currentTheme == 'dark') {
  // set dark theme
  document.body.setAttribute('data-theme', 'dark');
  themeBtn.innerHTML = 'Light Mode';
} else {
  // set light theme
  document.body.setAttribute('data-theme', 'light');
  themeBtn.innerHTML = 'Dark Mode';
}

themeBtn.addEventListener('click', function () {
  const theme = document.body.getAttribute('data-theme');

  toggleTheme(theme);
});

function toggleTheme(theme) {
  if (theme == 'dark') {
    document.body.setAttribute('data-theme', 'light');
    themeBtn.innerHTML = 'Dark Mode';
    localStorage.setItem('theme', 'light');
  } else {
    document.body.setAttribute('data-theme', 'dark');
    themeBtn.innerHTML = 'Light Mode';
    localStorage.setItem('theme', 'dark');
  }
}
