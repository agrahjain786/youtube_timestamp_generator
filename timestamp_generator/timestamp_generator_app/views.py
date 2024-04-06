from django.shortcuts import render
from django.http import JsonResponse
from pytube import YouTube
import requests
import json
from openai import OpenAI
import os

# Create your views here.
# def home(request):
#     return render(request, 'timestamp_generator_app/home.html')

def generate_timestamp(request):
    if request.method == 'POST' :
        youtubeUrl = request.POST.get('youtubeUrl')
        # Call OpenAI API to generate timestamp (replace API_KEY with your OpenAI API key)
        if youtubeUrl:
            # Call OpenAI API to generate timestamp (replace API_KEY with your OpenAI API key)
            yt = YouTube(youtubeUrl)
            yt.streams.filter(file_extension='mp4')
            stream = yt.streams.get_by_itag(139)
            stream.download('', "youtubevideo.mp4")
            OPENAI_API_KEY = ''
            with open('timestamp_generator_app/OPENAI.json', 'r') as file_to_read:
                json_data = json.load(file_to_read)
                OPENAI_API_KEY = json_data["OPENAI_API_KEY"]
            
            client = OpenAI(api_key=OPENAI_API_KEY)
            audio_file = open("youtubevideo.mp4","rb")
            transcript = client.audio.transcriptions.create(
                model = "whisper-1",
                file = audio_file
            )
            print(transcript.text)
            return render(request, 'timestamp_generator_app/home.html', {'message': transcript.text})
            # return render(request, 'timestamp_generator_app/result.html', {'timestamp': transcript.text})
        else:
            error_message = 'Please provide a YouTube URL.'
            return render(request, 'timestamp_generator_app/home.html', {'message': error_message})
            # return JsonResponse({'message': error_message}, status=400)
            # return render(request, 'timestamp_generator_app/result.html', {'error_message': error_message})
    else:
        error_message = ''
        return render(request, 'timestamp_generator_app/home.html', {'message':error_message})
        # return JsonResponse({'message': error_message}, status=400)
        # return render(request, 'timestamp_generator_app/result.html', {'error_message': error_message})