import dora

host = "http://localhost:3090/"

robo = dora.Robot()

robo.textToSpeech("こんにちは")
robo.textToSpeech("わたしは、おしゃべりができるダンボールロボットです")
robo.wait(1)
robo.textToSpeech("どうぞ、よろしくお願いいたします")
