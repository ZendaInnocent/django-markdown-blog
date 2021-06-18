const codehilites = document.querySelectorAll('div.codehilite');

codehilites.forEach((div) => {
  const copy = document.createElement('button');
  copy.innerHTML = 'copy';
  copy.classList.add('copy-btn');
  copy.addEventListener('click', handleCopyClick);
  div.append(copy);
});

function copyToClipboard(copiedText) {
  const el = document.createElement('textarea');
  el.value = copiedText;
  el.setAttribute('readonly', '');
  el.style.position = 'absolute';
  el.style.left = '-9999px';
  document.body.appendChild(el);

  const selected =
    document.getSelection().rangeCount > 0
      ? document.getSelection().getRangeAt(0)
      : false;

  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);

  if (selected) {
    document.getSelection().removeAllRanges();
    document.getSelection().addRange(selected);
  }
}

function handleCopyClick(e) {
  const { children } = e.target.parentElement;
  const { innerText } = Array.from(children)[0];
  copyToClipboard(innerText);
}
