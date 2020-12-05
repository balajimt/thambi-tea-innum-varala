#@markdown 1. Choose an audio source:
#@markdown <br> You can type in youtube audio sources https://www.youtube.com/watch?v=2rkQn-43ixs <br>
#@markdown Or choose the 'Default' audio piece <br>
#@markdown Or choose 'Own Source'
audio = 'Default' #@param ['Default', 'Own Source'] {allow-input: true}
#@markdown 2. Press play icon on the left after choosing
																   
from google.colab import files
%cd /content/sample_data

if (audio == 'Own Source'):
  print("Choose audio file")
  audio_file = files.upload()
  audio = ""
  for name in audio_file.keys():
    audio = '/content/' + name 
  print(audio)

print("Choose face photo")
images = files.upload()

%tensorflow_version 1.x
%cd /content

!git clone --depth 1 https://github.com/balajimt/thambi-tea-innum-varala.git
!mkdir /content/thambi-tea-innum-varala/LipSync/checkpoints/
!mkdir /content/thambi-tea-innum-varala/LipSync/temp/

import os
model_path = "/content/thambi-tea-innum-varala/LipSync/checkpoints/wav2lip_gan.pth"
print(model_path)
if not os.path.exists(model_path):
  !gdown https://drive.google.com/uc?id=1dwHujX7RVNCvdR1RR93z0FS2T2yzqup9 -O /content/thambi-tea-innum-varala/LipSync/checkpoints/wav2lip_gan.pth
						 
!wget --no-check-certificate -nc https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth -O /content/thambi-tea-innum-varala/LipSync/face_detection/detection/sfd/s3fd.pth

!pip install -U youtube-dl
# Downloading default video
!youtube-dl --extract-audio --audio-format mp3 https://www.youtube.com/watch?v=2rkQn-43ixs -o /content/default.mp3

if 'youtube.com' in audio:
  if os.path.exists('/content/custom.mp3'):
    os.remove('/content/custom.mp3')
  !youtube-dl --extract-audio --audio-format mp3 '$audio' -o /content/custom.mp3
  audio = 'custom'
										

if (not audio.endswith('.mp3')):
  audio = '/content/'+audio.lower()+'.mp3'

print("Using audio file", audio)

%cd /content/thambi-tea-innum-varala/LipSync/
outputs = []
for im in images:
  infile = '/content/sample_data/'+im
  outfile = '/content/'+im.rsplit('.')[0]+'_out.mp4'
  !python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face '$infile' --audio '$audio' --pads 0 20 0 0 --outfile \"'$outfile'\" 2>&1 | tee /content/out.txt
  bad = !cat /content/out.txt | grep 'Face not detected'
  if bad:
    import cv2
    print('\nFace not detected - will use whole frame')
    if infile.split('.')[1] in ['jpg', 'png', 'jpeg']:
      frame = cv2.imread(infile)
    else:
      video_stream = cv2.VideoCapture(infile)
      still_reading, frame = video_stream.read()
    x1 = 0
    h,x2 = frame.shape[:2]
    if x2>h:
      x1 = (x2-h)//2
      x2 = x1+h
    !python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face '$infile' --audio '$audio' --box 0 $h $x1 $x2 --pads 0 20 0 0 --outfile \"'$outfile'\"
  outputs.append(outfile)
  os.remove(infile)

from IPython.display import HTML, clear_output
from base64 import b64encode

clear_output()
print("Inference successful. Generating video output....")
for file in outputs:
  with open(file, 'rb') as f:
    data_url = "data:video/mp4;base64," + b64encode(f.read()).decode()
  display(HTML("""
  <video width=600 controls loop>
        <source src="%s" type="video/mp4">
  </video>""" % data_url))
