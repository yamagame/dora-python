# Dora Engine Python Module

Dora Engine をコントロールする Python モジュールです。

## サンプル

```python
import dora

host = "http://localhost:3090/"

robo.textToSpeech("こんにちは")
robo.textToSpeech("わたしは、おしゃべりができるダンボールロボットです")
robo.wait(1)
robo.textToSpeech("どうぞ、よろしくお願いいたします")
```

## リファレンス

### robo.textToSpeech(speech)

音声読み上げします。

```python
robo.textToSpeech('こんにちは')
```

### robo.speechToText()

音声認識を開始します。

```python
word = robo.speechToText()
```

デフォルトタイムアウトは10秒です。

単位はナノ秒でタイムアウト値を変更できます。

```python
word = robo.speechToText(30000)
```

0にするとタイムアウトしません。

```python
word = robo.speechToText(0)
```

### robo.slide(imagePath)

スライド画像を表示します。

```python
robo.slide('images/xavier/001.jpeg')
```

### robo.playSound(soundFileName)

サウンドを再生します。

```python
robo.playSound('Quiz-Buzzer.wav')
```

### robo.runScript(userName, scriptFileName)

スクリプトを実行します。

```python
robo.playSound('yamagame', 'introduction.dora')
```

### robo.stop()

実行中のスクリプトを停止します。

### robo.sleep(second)

指定秒数待ちます。

```python
robo.sleep(1)
```
