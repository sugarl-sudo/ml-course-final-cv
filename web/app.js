// web/app.js
fetch('http://api:5000/api')
    .then(response => response.json())
    .then(data => {
        document.getElementById('api-response').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
