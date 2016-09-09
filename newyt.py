#!/usr/bin/env python
# coding: utf-8

from gi.repository import Notify # Dependences: apt-get install python-gobject

import requests  # Dependences: pip install requests


class NewYt():

    def __init__(self, channels):
        self.channels = channels
        Notify.init("Notification")
        Notify.Notification.new('Buscando novos vídeos, aguarde!').show()
        Notify.uninit()

    def read_channels(self):
        self.log_txt = []

        try:
            arquive = open('log_newyt.txt', 'r')
            text = arquive.readlines()
        except:
            arquive = open('log_newyt.txt','w')
            arquive.close()
            arquive = open('log_newyt.txt', 'r')
            text = arquive.readlines()

        for linha in text:
            self.log_txt.append(linha)

        arquive.close()

        self.num_new_videos = len(self.channels) - len(self.log_txt)

    def not_new_channels(self):
        for i in range(self.num_new_videos):
            self.simple_not('Novo canal adicionado: ' + self.channels[-(i + 1)])

    def not_new_videos(self):
        arquive = open('log_newyt.txt', 'w')
        new_video = False

        for channel in self.channels:
            r = requests.get('https://www.youtube.com/user/' + channel + '/videos')
            title = channel + ' : ' + ((r.text.split('<div class="yt-lockup-content">')[1]).split('title="')[1]).split('"')[0].encode('utf-8')
            if not (title + '\n' in self.log_txt):
                new_video = True
                self.complex_not('Novo vídeo !', title)
            arquive.write(title + '\n')

        if not new_video:
            self.simple_not('Nenhum vídeo novo disponível !')

        arquive.close()

    def simple_not(self, title):
        Notify.init("Notification")
        Notify.Notification.new(title).show()
        Notify.uninit()

    def complex_not(self, title, text):
        Notify.init("Notification")
        Notify.Notification.new(title, text).show()
        Notify.uninit()

if __name__ == '__main__':
    channels = ['ForeverPlayerGames', 'Viniccius13', 'HDDaviGamer', 'Nightblue3', 'Patopapao', 'Yetzlol', 'Picocalol', 'Barbixas']

    yt = NewYt(channels)

    yt.read_channels()
    yt.not_new_channels()
    yt.not_new_videos()
