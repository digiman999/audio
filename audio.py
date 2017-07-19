

class Audio:   # an Audio object (not a file system file)
    def data(self):
        pass

    def metadata(self):
        pass

    def other(self):
        pass

'''
Fingerprinting
- uses
    - phrases/sentences that trigger something ex applauding, anger
    - voice recognition
    - object recognition
        - different voices: ex phone conversation
    - noise/gap removal
        - auto edit recordings ex phone conversations to quickly navigate to important parts
    - security
    - legal
    - monitoring any streams
    - intellectual copyright
        - royalty collection
        - enforce copyright
    - forensics
        -
- how
    - Industrial Strength AUdio Search Algorithm - Andrew Wang, 7 pages long, from Shazam
    - analyse different dimensions
        - pitch
        - dynamics
        - spectrum
        - tempo/time span of all other dimensions

'''

from dejavu import Dejavu

