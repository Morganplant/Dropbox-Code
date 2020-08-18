import os
from gtts import gTTS
import subprocess
import argparse
import re

LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))

def convert(input_file_path, filename, output_dir, content):
	speech = gTTS(text = content, lang ='en', slow = False)
	if '.mp3' not in filename:
		filename = filename + '.mp3'
	
	if re.search(r'\w+\W\d+', content):
		filename = re.search(r'\w+\W\d+', content).group(0)

	full_path = os.path.join(output_dir, filename)

	speech.save(full_path)

def read_file(input_file_path):
	with open(input_file_path) as file:
		content = file.read()
	return content

def auto_play(filename):
	subprocess.call(["afplay", filename])

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input-file",
						help="path of the text file to be converted into a .mp3",
						required=True)
	parser.add_argument("--filename",
						help="name of the .mp3 file",
						default='audio_file.mp3')
	parser.add_argument("-a", "--autoplay",
						help="automatically starts playing the audio file",
						action="store_true")
	parser.add_argument("--output-dir",
						help="the output directory for the .mp3 file",
						default=LOCAL_DIR)
	args = parser.parse_args()

	input_file = args.input_file
	convert(input_file, args.filename, args.output_dir, read_file(input_file))


	if args.autoplay:
		auto_play(args.filename)

if __name__ == "__main__":
    main()