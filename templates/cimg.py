from flask import Flask
import random 
import os

app = Flask(_name_)
@app.route("/")
def casual_img():

    image_paths=['../static/img/meme_2.webp', '../static/img/meme_3.webp', '../static/img/meme_1.webp']
    random_img_path = random.choice(image_paths)
   
    return f'<img src="/static/img/{random_img_path}" alt="Random Image">'

app.run(debug=True)


