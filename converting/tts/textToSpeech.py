from gtts import gTTS

class TextToSpeech():
    def __init__(self, text, lang='en'):
        self.converter = gTTS(text=text, lang=lang)
        self.converter.save('test.mp3')
    

s = '''
Primarily on the basis of linguistic evidence, we have found that most of our ordinary conceptual system is metaphorical in nature. And we have found a way to begin to identify in detail just what the metaphors are that structure how we perceive, how we think, and what we do. 

To give some idea of what it could mean for a concept to be metaphorical and for such a 
concept to structure an everyday activity, let us start with the concept ARGUMENT and the 
conceptual metaphor ARGUMENT IS WAR. This metaphor is reflected in our everyday language 
by a wide variety of expressions: 
'''
t = TextToSpeech(s.rstrip('\n'))
