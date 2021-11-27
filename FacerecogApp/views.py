from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import json
import pyrebase
import os
import asyncio
from asgiref.sync import sync_to_async

from FacerecogApp.models import Timecheckin
from FacerecogApp.serializers import TimecheckinSerializer

import base64,io
from django.core.files.base import ContentFile
from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True
# Create your views here.

config ={
  "apiKey": "AAAAOMrNumc:APA91bFQlicU4R6LkKcdULHC0sob-4r4QjZDYLpOwkPZG98H80CPnUK-WAp0Iunb6SFz6xUzRpB_t2eN3k6khcSNXbplOcRC7VnY-dksRQTZs-QBMESG-OPmRUw6DsvlupS6fGf9Tlm8",
  "authDomain": "https://accounts.google.com/o/oauth2/auth",
  "databaseURL": "https://daktht.firebaseio.com",
  "projectId": "daktht",
  "storageBucket": "daktht.appspot.com",
  "messagingSenderId": "243920648807",
  "appId": "1:243920648807:android:31dffb2bfdf2769a7332c2"
}


async def fetchImageFirebase(userId):
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    dirname =f'dataset/{userId}'
    try:
        # Create target Directory
        os.makedirs(dirname)
        print("Directory " , dirname ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirname ,  " already exists")
    for i in range(0,19):
        my_image = f'Users/{userId}/Models/{i}.jpg'
        path =f'dataset/{userId}/{i}.jpg'
        storage.child(my_image).download(path)
  

@csrf_exempt
def train(request,id=0):
    if request.method =='POST':
        data = JSONParser().parse(request)
        userId = data['userId']
        print(userId)
        asyncio.run(fetchImageFirebase(userId))
            
        return JsonResponse("Trained successfully", safe= False)    
      
@csrf_exempt
def identify(request,id=0):
    if request.method =='POST':
        data= JSONParser().parse(request)
        string= data['photo']
        string += '=' * (-len(string) % 4) 
        format, imgstr = string.split(';base64,')
        print(imgstr)
        ext = format.split('/')[-1]
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(imgstr, "utf-8"))))
        img.save(f'my-image.{ext}')
        return JsonResponse("received successfully", safe= False) 