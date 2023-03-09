const input = document.getElementById('file-input');
const preview = document.getElementById('preview');
const uploadButton = document.getElementById('upload-button');
const uploadForm = document.getElementById('upload-form');
const fileInput = document.getElementById('file-input');
const previewImage = document.getElementById('preview');
const dropdownButton = document.getElementById('dropdown-button');
const previewContainer = document.querySelector('.preview-container');
// console.log("hithere")
// Listen for changes to the dropdown button
dropdownButton.addEventListener('change', function() {
  
  const selectedOption = dropdownButton.value;
  console.log(selectedOption)
  // Replace the preview container's contents with the new form
  // previewContainer.innerHTML = formHtml;
});

fileInput.onchange = (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.addEventListener('load', (event) => {
    previewImage.src = event.target.result;
    previewImage.classList.remove('hidden');
  });

  reader.readAsDataURL(file);
};

uploadButton.addEventListener('click', function () {
  uploadForm.classList.toggle('hidden')
  const reader = new FileReader();
  reader.onload = function () {
    preview.src = reader.result;
    preview.classList.remove('hidden');
  };
  reader.readAsDataURL(input.files[0]);
});
