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