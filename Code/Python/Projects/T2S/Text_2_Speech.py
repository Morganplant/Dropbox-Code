from gtts import gTTS 
import os
import subprocess
import platform
import argparse
import random
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
parser = argparse.ArgumentParser()

parser.add_argument("--output-dir", help="the output direcory of the mp3 file")
parser.add_argument("-a", "--autoplay", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-Text", help="Text that is turned into speech")
args = parser.parse_args()

filelist = [ f for f in os.listdir(dir_path) if f.endswith(".mp3") ]
for f in filelist:
    os.remove(os.path.join(dir_path, f))

def text_2_speach(text, filename, output_dir, language='en',autoplay=False):

    if args.autoplay:
        autoplay = True

    if not filename.endswith('.mp3'):
        filename = filename + '.mp3'

    audio_file = os.path.join(output_dir,filename)
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save(audio_file)
    

    if platform.system() == 'Darwin':
        if autoplay == True:
            subprocess.call(["afplay", audio_file])
    if platform.system() == 'Windows':
        if autoplay == True:
            os.system("start %s" % (audio_file))
    if platform.system() == 'Linux':
        print('No support for Linux')

if args.output_dir:
    output_dir = args.output_dir
else:
    output_dir = dir_path

if args.Text:
    Text = str(args.Text).replace('_',' ')
    filename = re.search(r'\w+\W\d+', Text)
    if filename:
        filename = filename.group(0)
    else:
        filename = 'filename'
else:
    Text = 'Testing, Testing, 1 2 3'


text_2_speach(Text, filename, output_dir, autoplay=False)
