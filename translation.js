const form = document.querySelector('form');
const button = document.querySelector('#translate-button');
const translationDisplay = document.querySelector('#translation');

button.addEventListener('click', () => {
  const englishText = document.querySelector('#english-text').value;
  const data = {
    english_text: englishText
  };
  fetch('/translate/en-fr', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(data => {
      translationDisplay.textContent = data.french_text;
    })
})
