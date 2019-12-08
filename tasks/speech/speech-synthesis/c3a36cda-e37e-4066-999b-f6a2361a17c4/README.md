input:

   input text file path:

       utterences.txt
.

output:

   2 audio files in 'flac' and 'wav' format in 'audio_output_data' folder. path to these audio files are-

   audio_output_data/summary.flac

   and

   audio_output_data/summary.wav
.



command:

     mlflow run .


     for diffrent parameter input from command-line-

     mlflow run . -P utterences_text_data_file_path="utterences.txt"

# Editor Notes
AI-Platform Task UUID: `c3a36cda-e37e-4066-999b-f6a2361a17c4`

This task uses [Google's Text-to-Speech python library](https://pypi.org/project/gTTS/).
