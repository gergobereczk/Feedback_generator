from flask import Flask, render_template, request, session, escape, redirect, url_for
import random, json
import data_manager
import text_to_picture
import e_mail
app = Flask(__name__)




@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get_feedback")
def get_feedback():
    feedbacks = data_manager.get_feedbacks()
    random_number = random.randint(0, (len(feedbacks)-1))
    feedback = feedbacks[random_number]['feedback']
    json_included_feedback = json.dumps({"feedback":"{}".format(feedback)})
    return json_included_feedback

@app.route("/get_meme_from_feedback", methods=['GET', 'POST'])
def get_meme_from_feedback():
    feedback = request.get_json()['feedback']
    image_title = request.get_json()['imageTitle']
    text_to_picture.add_text_to_image(feedback, image_title)
    return "nothing"


@app.route("/send_mail",  methods=['GET', 'POST'])
def send_mail():
    name =request.get_json()['name']
    adress = request.get_json()['mailAdress']
    boady = request.get_json()['body']
    image_number = request.get_json()['imageNumber']
    e_mail.sendMail(name, adress, boady, image_number)
    return "nothing"


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
