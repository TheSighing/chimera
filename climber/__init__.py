from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("config")

from app.module.controllers import module

app.register_blueprint(module)
