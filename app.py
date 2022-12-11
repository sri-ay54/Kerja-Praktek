import argparse
import io
import os
from PIL import Image
from detect import run
from flask import Flask, render_template, request
import torch


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    print(request.method)
    if request.method == 'GET':
        print("Identifikasi jenis batuan")
        return render_template("batu-classification.html")
        
    elif request.method == 'POST':
        print("ini method POST")
        x=request.files["image"]
        print(x.save("upload/hasil.jpg"))

        print("test")

        run(weights='best.pt', source= 'upload/hasil.jpg', exist_ok=True)

    return render_template("batu-classification.html")

if __name__ == '__main__':
      app.run(port=1111, debug=True)

