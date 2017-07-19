import requests
import os
import re
from flask import Flask, request

'''
- Radio Recorder
    - should it be a generic recorder, incl video, radio, images, TV, browsers, screencasts ie any stream.  That woul be organising by function rather than domain.  Might be cleaner if things were organised by domain then I compose them into function
    - downloading & streaming, or just streaming
    - handle hardware recording also, or just digital?

- incl
    - metadata:
        - recording source/location, time stamps, permissions, legal contract


- Anti Piracy Activities
    - monitoring sites & other clients
    - intelligence/inference rules to spot thieves/cases/etc
    - check PRO/MRO databases to see fake/duplicate claims etc, others posing as me etc
    - illegal download/streaming/upload sites; take down notices & further legal action
    
    - pre-release theft, logs of those who've done it so can sue them
    - search my assets online, do the websites belong to my clients list; no>takedown/sue?
    
    
have a list of sources to download
    - manually/auto added
    

- identify infringer ex Youtube Channel
- take down procedure ex YouTube have specific methods, letter, email etc
- 

- laws worldwide
    - implimentation date per law item (old/current)
    - structured in a way they can be reasoned over/used for analysis/auto print off infringement notices


LEGAL
- contract (license, PRO/MRO etc) details, infringement & consequences
- CR laws worldwide
- keeping up to date with ongoing legal concerns

- CR Protection
    - Watermarking implimentation, analyzing, 


'''

app = Flask('__main__')
  
@app.route('/add', methods=['POST'])
def add():
    r = request.form.get
    new = {'url':r('url'), 'title':r('title')}
    with open('queue.txt', 'a') as f: 
        f.write(str(new)+'\n')
    return 'Thanks'

@app.route('/delete/<uid>')
def delete():
    return 'return success if item deleted, else error'

@app.route('/getInfo')
def getInfo():
    f = open('queue.txt')
    return f.read()
    
@app.route('/getData')
def getData():
    return 'return file(s), maybe as zip'

def logger():
    'write requests to log file (or db even better)?'

'''
getExisting
getItems (queued, downloading, finished)
'''

#RECORD_DIR = 'C:/Users/Eddie/Desktop/dev/musicCompany/src/logic/radioRecorder/recordings'
RECORD_DIR = os.getcwd() + '/recordings'

class Stream():  #put this class in a more generic location
    def __init__(self, url, recordDir, fileLabel, record=True):
        self.url = url
        self.recordDir = recordDir
        self.fileLabel = fileLabel
        if record: self.record()
        
    def record(self):
        self.request = requests.get(self.url, stream=True)
        
        os.chdir(self.recordDir)
        if not os.path.exists(self.fileLabel): os.makedirs(self.fileLabel)
        os.chdir(self.fileLabel)
        if len(os.listdir(os.getcwd())) > 0:
            largest = max(os.listdir(os.getcwd())).split('.')[-2]
            largest = int(largest.split()[-1]) + 1
            #largest = max(files, key=lambda files:re.split(r"_|\.",files)[1])
            #largest = largest.split('.')[-2]
            #largest = int(largest.split()[-1]) + 1
            print largest
                        
            # step here to get the last number, then +1
        else: 
            largest = 1
        
                    
        '''
        - if gets interrupted, start a new file
        - split files into horus so they're a) easier to analyse, b) minimize lost data from interrupted stream, iii) have an entire hour to send stations as proof of their radio usage
        - multi-threading etc: using KeyboardInterrupt seems to fail beacuse the second stream doesn't run unless the first is complete
        '''
        
        
        try: 
            with open('%s %s.mp3' % (self.fileLabel, largest), 'wb') as f:
                for block in self.request.iter_content(1024):
                    f.write(block)
                    print largest #'saving'
        except KeyboardInterrupt:
            pass
        
                    
        '''            
        with open(self.fileLabel+'.mp3', 'wb') as f:
            try: 
                for block in self.request.iter_content(1024):
                    f.write(block)
                    print 'saving'
            except KeyboardInterrupt:
                pass
        '''
        
        
#stream = Stream('http://streaming.radionomy.com/Cheche-International-Radio', RECORD_DIR, 'Radio Station')

app.run(debug=True) 

                
                
