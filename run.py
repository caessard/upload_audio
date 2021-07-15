from __future__ import unicode_literals

import ffmpeg as ffmpeg
from pytube import YouTube
import ssl
import os
import subprocess

DESTINATION = './results/'


class Person:
    """
    Entity to a person voice data.
    """
    def __init__(self, name, url):
        self.name = name
        self.url = url


def get_length(input_audio):
    """
    Calculate duration audio in seconds
    :param input_audio: The paht of audio
    :return:
    """
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_audio], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)


if __name__ == '__main__':
    voices = [Person('LUIS FERNANDO VELASCO',
                     'https://youtu.be/VEn5epIlBHs')]
    try:
        ssl._create_default_https_context = ssl._create_unverified_context

        for voice in voices:
            # Create destination directory
            dir = os.path.join(DESTINATION, voice.name)
            if not os.path.exists(dir):
                os.mkdir(dir)

            yt = YouTube(voice.url)
            # extract only audio
            video = yt.streams.filter(only_audio=True).first()

            video.download(dir)
            # Get default name
            default_filename = video.default_filename

            duration = get_length(os.path.join(dir, default_filename))
            new_filename = f"{voice.name}-{duration}.wav"

            # using pytube API
            stream = ffmpeg.input(os.path.join(dir, default_filename))
            stream = ffmpeg.output(stream,
                                   os.path.join(dir, new_filename))
            ffmpeg.run(stream)
            os.remove(os.path.join(dir, default_filename))

    except Exception as ex:
        print("Not could download audio file")
        print(ex)
