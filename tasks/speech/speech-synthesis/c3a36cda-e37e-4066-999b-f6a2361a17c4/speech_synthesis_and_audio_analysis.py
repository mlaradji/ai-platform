#!/usr/bin/env python
# coding: utf-8




from gtts import gTTS
import os 
import mlflow 
import soundfile as sf
from mutagen.flac import FLAC
import aubio 
import sksound 
from sksound.sounds import Sound 
import argparse 





def read_utterences_file():

    parser = argparse.ArgumentParser()

    parser.add_argument("--utterences_text_data_file_path", type=str, default = "utterences.txt", help='input a string')

    args = parser.parse_args()

    print(args.utterences_text_data_file_path)
    
    
    utterences_data_file = open(args.utterences_text_data_file_path, "r")
    
    utterences = utterences_data_file.read()
    
    utterences_data_file.close()
    
    return utterences





def convert_utterences_text_to_audio_data(utterences):
    
    tts = gTTS(utterences, lang="en-us")
    
    output_path = "audio_output_data"
    
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
        
    tts.save("audio_output_data/summary1.flac")
    
    os.system("ffmpeg -i audio_output_data/summary1.flac -c:a flac audio_output_data/summary.flac")
    
    os.remove("audio_output_data/summary1.flac")
    
    audio = FLAC("audio_output_data/summary.flac")
    
    return audio





def analysis_on_the_audio_data(audio):
    
    summary_audio_length = audio.info.length
    
    print("summary_audio_length = {}".format(summary_audio_length))

    summary_audio_bitrate_in_kbps = (audio.info.bitrate)/1000
    
    print("summary_audio_bitrate_in_kbps = {}".format(summary_audio_bitrate_in_kbps))
    
    audio_by_sksound = Sound("audio_output_data/summary.flac")
    
    info = audio_by_sksound.get_info() 

    print(info)
    
    (source, rate, numChannels, totalSamples, duration, bitsPerSample) = info
    
    print("source = {}".format(source))

    print("rate = {}".format(rate))

    print("numChannels = {}".format(numChannels))

    print("totalSamples = {}".format(totalSamples))

    print("duration = {}".format(duration))

    print("bitsPerSample = {}".format(bitsPerSample))

    print(audio_by_sksound.summary())
    
    print("---------------------ok 1 ---------------------")
    
    statbuf = os.stat("audio_output_data/summary.flac")
    
    print("---------------------ok 2 ---------------------")
    
    size_in_MB = statbuf.st_size / (1024 * 1024)
    
    print("---------------------ok 3 ---------------------")
    
    print("size_in_MB = {}".format(size_in_MB))
    
    print("---------------------ok 35 ---------------------")
    
    f_wav = sf.SoundFile("audio_output_data/summary.wav")
    
    print('samples = {}'.format(len(f_wav)))
    print('sample rate = {}'.format(f_wav.samplerate))
    print('seconds = {}'.format(len(f_wav) / f_wav.samplerate))
    print('channels = {}'.format(f_wav.channels))
    print('format = {}'.format(f_wav.format))
    print('subtype = {}'.format(f_wav.subtype))
    print('endian = {}'.format(f_wav.endian))
    
    f_flac = sf.SoundFile("audio_output_data/summary.flac")

    samples = len(f_flac)
    sample_rate = f_flac.samplerate
    seconds = (len(f_flac) / f_flac.samplerate)
    channels = f_flac.channels
    format_output = f_flac.format
    subtype = f_flac.subtype
    endian = f_flac.endian
    
    print('samples = {}'.format(samples))
    print('sample rate = {}'.format(sample_rate))
    print('seconds = {}'.format(seconds))
    print('channels = {}'.format(channels))
    print('format = {}'.format(format_output))
    print('subtype = {}'.format(subtype))
    print('endian = {}'.format(endian))
    
    return summary_audio_bitrate_in_kbps, sample_rate, channels, summary_audio_length, samples, endian, subtype, format_output, seconds, size_in_MB 





if __name__ == "__main__":
    
    utterences = read_utterences_file()    
        
    audio = convert_utterences_text_to_audio_data(utterences)   
    
    summary_audio_bitrate_in_kbps, sample_rate, channels, summary_audio_length, samples, endian, subtype, format_output, seconds, size_in_MB = analysis_on_the_audio_data(audio)
 

    with mlflow.start_run():
        mlflow.log_param("text_data_file_input_path", "utterences.txt")
        mlflow.log_artifact("utterences.txt")

