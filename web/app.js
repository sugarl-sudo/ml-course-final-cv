// web/app.js
document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData();
    const fileField = document.getElementById('video-file');

    formData.append('video', fileField.files[0]);

    fetch('http://api:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('api-response').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});