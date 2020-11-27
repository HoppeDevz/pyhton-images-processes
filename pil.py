import os
import PIL
from PIL import Image
from flask import Flask, request

app = Flask("ImgAPI")
print('Pillow Version:', PIL.__version__)

@app.route("/imgRotate", methods=['POST'])
def imgRotateRoute():
    body = request.get_json()
    imgid = body["imgId"]
    rotateconst = body["rotateconst"]
    imgformat = body["imgformat"]

    imgpath = "assets/" + imgid + "." + imgformat

    if not os.path.isfile(imgpath): return { 'edit_image': False, 'reason': 'invalid directory' }

    if (imgid != None and rotateconst != None and imgformat != None):
        img = Image.open(imgpath)
        image_edited = img.rotate(rotateconst)
        image_edited.save("assets/e" + imgid + ".png", format="PNG")
        return { 'edit_image': True }

    return { 'edit_image': False, 'reason': 'some paramters null' }

app.run() 