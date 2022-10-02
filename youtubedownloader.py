from pytube import YouTube
from sys import argv

ytlink = (input ("Youtube Link: "))
link = src=(ytlink)
yt = YouTube(link)
ytpath = (input("Path: "))

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download(ytpath)