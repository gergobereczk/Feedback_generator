let generate_feedback = document.querySelector('.generate');
generate_feedback.addEventListener("click", getFeedbackFromServer);

function getFeedbackFromServer(e) {

    fetch('http://127.0.0.1:5000/get_feedback')
        .then(function (response) {
            return response.json();
        })
        .then(function (myJson) {
            document.getElementById('meme').innerHTML = '';
            let feedback = JSON.stringify(myJson.feedback);
            document.getElementById('feedback').value = feedback.slice(1, -1);
            document.getElementById('meme').innerHTML = '<button class="btn-big-red">Meme</button>'
        });


}

let generate_meme = document.querySelector('.meme');
generate_meme.addEventListener('click', getMemeFromFeedback);

function getMemeFromFeedback(e) {
    let feedback = document.getElementById('feedback').value;
    let imageTitle = Math.floor(Math.random() * 1000) + 1;
    let url = '/get_meme_from_feedback';
    let data = {feedback: `${feedback}`, imageTitle: `${imageTitle}`};


    fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(data), // data can be `string` or {object}!
        headers: {
            'Content-Type': 'application/json'
        }

    });

    setTimeout(function () {
        document.getElementById('meme').innerHTML = `<img id='${imageTitle}' class="memeImage" src="/static/picture_with_string/${imageTitle}.jpg"  width="500" height="400">`;
        document.getElementById('mail').innerHTML = '<button class="btn-big-red">Mail to friend</button>';
    }, 200);


}


let mail = document.querySelector('.mail');
mail.addEventListener('click', openModal);

function openModal(e) {

    document.getElementById('id01').style.display = 'block';

}


document.getElementById('submitMail').addEventListener('click', sendMail);

function sendMail(e) {
    let imageNumber = document.querySelector('.memeImage').id;
    let name = document.getElementById('name').value;
    let mailAdress = document.getElementById('mailAdress').value;
    let body = document.getElementById('body').value;
    let url = '/send_mail';
    let data = {name: `${name}`, mailAdress: `${mailAdress}`, body: `${body}`, imageNumber: `${imageNumber}`};


    fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(data), // data can be `string` or {object}!
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(res => res.json())
        .then(response => console.log('Success:', JSON.stringify(response)))
        .catch(error => console.error('Error:', error));
    location.reload()

}