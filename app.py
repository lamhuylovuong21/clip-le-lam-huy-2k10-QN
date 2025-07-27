# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 21:31:43 2025

@author: ASUS
"""
from flask import Flask, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'

@app.route("/")
def home():
    # Tạo thư mục nếu chưa có
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Lấy danh sách file trong thư mục
    files = os.listdir(UPLOAD_FOLDER)

    return render_template("index.html", files=files)





