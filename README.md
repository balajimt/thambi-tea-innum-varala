# Arc Hack by Thambi Tea Innum Varala - Covid Special Edition
## The Why:
<img src="https://cultofthepartyparrot.com/parrots/hd/confusedparrot.gif" alt="why">\
Being stuck at homes and not being able to meet people have been a bummer. Seeing each other helps in bonding as a team and developing connections, even if its via video.
Not everyone switches on their videos due to multitude of reasons sometimes it being as simple as not being dressed up properly. Enter *Live Fake* where you can morph your face into an image of yourself dressed up or someone else for fun meetings!
Other times there isn't simple enough bandwidth to facilitate video transmission, enter *Lip Sync* which can be extended to build videos at a server before being routed to participants.

The Hack has 3 components:
1. Lip Sync - generates a video from  an audio + photo
2. Live Fake - generates transformed video stream from a photo (model) + live video input
3. Electron.js wrapper - a wrapper application to hit the above 2 models run via Google Collab

Architecture: 
<img src="doc_images/Architecture.png" alt="architecture">
### Launching the electron.js app
```bash
# Clone this repository
git clone https://github.com/balajimt/thambi-tea-innum-varala/tree/main/arc-hack-electron-wrapper
# Go into the repository
cd electron-wrapper
# Install dependencies
npm install
# Run the app
npm start
```

### Authentication:
Authentication is done via Google-sign in.

### Running the models in collab:
- Sign in via Google account
- Run the cells by clicking <img src="doc_images/button.png" alt="collab run button">
- For Lip Sync, audio and image needs to be provided. Audio source can be youtube links, Custom, or you can use the default clip.
- For Live Fake, images maybe uploaded otherwise default avatars will be used. Live video stream is captured via webcam.

### Live Fake specific tips:
- Center the face and calibrate with face zoomed-in as much as possible for best results.

A Hack by Amal, Balaji and Prajwala 