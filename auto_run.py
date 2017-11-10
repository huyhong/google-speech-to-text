import os
from sys import argv
from goog import transcribe_gcs

directory = argv[1]

#Runs transcription for each file inside the specified directory
def auto_run(directory):
    print "Starting run"
    files = os.listdir(directory)
    for file in files:
        os.rename(os.path.join(directory, file), os.path.join(directory, file.replace(' ', '_')))#Removes any spaces in the file names

    print "Starting processing"
    for file in os.listdir(directory):     # Get each .mp4 file in directory and run transcription
        file_path = os.path.join(directory, file)
        print "Processing " + file_path
        if file.endswith(".mp4"):
            transcribe_gcs(file_path)
            print(file_path)
        else:
            print "Not an MP4"
            continue

auto_run(directory)