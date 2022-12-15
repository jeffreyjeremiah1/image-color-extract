from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from palette import Palette
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['UPLOAD_FOLDER'] = 'static/img/'
Bootstrap(app)


@app.route("/", methods=["POST", "GET"])
def home():
    background_img = "static/img/pexels-francesco-ungaro-1525043.jpg"
    if request.method == "POST":
        file = request.files['files']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        full_image_path = f"static/img/{file.filename}"
        num_of_colors = request.form.get('num_colors')
        delta = request.form.get('fdelta')
        print(file.filename)
        print(num_of_colors)
        print(delta)
        colors = Palette(numb_of_color=num_of_colors, file=full_image_path, delta=delta)
        color_list = colors.show_colors()[0]
        color_perc = colors.show_colors()[1]
        print(color_list)
        return render_template("index.html", colors=color_list, file=full_image_path, percentage=color_perc)
    return render_template("index.html", file=background_img)


@app.route("/colors", methods=["POST", "GET"])
def show_colors():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
