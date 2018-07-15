# -*- coding: utf-8 -*-
import urllib.request
import time
import json

class Robot():
  headers = {"Content-Type" : "application/json"}

  def __init__(self, host="http://localhost:3090/"):
    self.host = host

  def sendRequest(self, request):
    with urllib.request.urlopen(request) as response:
      html = response.read()
    return html.decode("utf-8")
  
  def sendCommand(self, data):
    request = urllib.request.Request(self.host+'command', data=json.dumps(data).encode("utf-8"), method="POST", headers=self.headers)
    return self.sendRequest(request)

  def textToSpeech(self, speech):
    """ ロボットに話をさせるメッセージを送信します """
    data = {"message": speech}
    request = urllib.request.Request(self.host+'text-to-speech', data=json.dumps(data).encode("utf-8"), method="POST", headers=self.headers)
    return self.sendRequest(request)

  def speechToText(self, timeout=10000):
    """ ロボットに話を聞くメッセージを送信します """
    data = {"payload": { "timeout": timeout }}
    request = urllib.request.Request(self.host+'speech-to-text', data=json.dumps(data).encode("utf-8"), method="POST", headers=self.headers)
    return self.sendRequest(request)

  def micSensitivity(self, sensitivity=2000):
    """ マイク感度を変更するメッセージをロボットに送信します """
    request = urllib.request.Request(self.host+'mic-threshold', data=str(sensitivity).encode("utf-8"), method="POST")
    return self.sendRequest(request)

  def sendSpeech(self, speech):
    """ 話を聞いているロボットに割り込みするメッセージを送信します """
    request = urllib.request.Request(self.host+'speech', data=speech.encode("utf-8"), method="POST")
    return self.sendRequest(request)

  def slide(self, image):
    """ スライドを表示するメッセージを送信します """
    return self.sendCommand({
      'type': 'quiz',
      'action': 'slide',
      'photo': image,
    })
  
  def playSound(self, sound):
    """ 音を鳴らすメッセージを送信します """
    return self.sendCommand({
      'type': 'sound',
      'sound': sound,
    })
  
  def stopSound(self):
    """ 音を止めるメッセージを送信します """
    return self.sendCommand({
      'type': 'sound',
      'sound': 'stop',
    })

  def playMovie(self, movie):
    """ 動画再生を開始するメッセージを送信します """
    return self.sendCommand({
      'type': 'movie',
      'action': 'play',
      'movie': movie,
    })

  def isMoviePlaying(self):
    """ 動画再生中かどうがを調べるメッセージを送信します """
    html = self.sendCommand({
      'type': 'movie',
      'action': 'check',
    })
    msg = json.loads(html)
    print(msg)
    return (msg["state"] == 'play')

  def stopMovie(self):
    """ 動画再生を止めるメッセージを送信します """
    return self.sendCommand({
      'type': 'movie',
      'action': 'cancel',
    })
  
  def stop(self):
    """ 全ての再生を停止するメッセージを送信します """
    return self.sendCommand({
      'type': 'scenario',
      'action': 'stop',
    })
  
  def runScript(self, name, filename, range={ 'start': 0 }):
    """ スクリプトを実行するメッセージを送信します """
    return self.sendCommand({
      'type': 'scenario',
      'action': 'play',
      'filename': filename,
      'name': name,
      'range': range,
    })

  def wait(self, second=1):
    """ 指定秒数待ちます """
    time.sleep(second)

  def sleep(self, second=1):
    """ 指定秒数待ちます """
    time.sleep(second)
