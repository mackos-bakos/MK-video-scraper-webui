from flask import Flask, render_template, request, session, redirect, url_for

from utilities.funcs import *


app = Flask(__name__)
app.secret_key = "ReplaceMeIfNeeded"

@app.route('/')
def render_ui():
    return render_template('menu.html')

@app.route('/scrape', methods=["POST"])
def scrape():
    video_link = request.form.get("Link")
    should_resume = request.form.get("Resume")

    if video_link == "":
        print("empty required argument video_link, command refused")
        return redirect(url_for('render_ui'))
    
    handle_process(video_link, should_resume)
    
    return redirect(url_for('render_ui'))
if __name__ == '__main__':
    app.run(host='localhost', port=8000)
