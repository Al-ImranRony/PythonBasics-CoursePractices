'''
Use of Python module Youtube
'''


from pytube import YouTube

videoLink = "https://www.youtube.com/watch?v=ubV-8EYzTyc"

YouTube(videoLink).streams.first().download(filename="pdv1")