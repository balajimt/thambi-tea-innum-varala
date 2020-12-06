# Arc Hack by Thambi Tea Innum Varala
The Why:
Being stuck at homes and not being able to meet people have been a bummer. Seeing each other via video helps in bonding as a team and developing connections.
Not everyone switches on their videos due to multitude of reasons sometimes it being as simple as not being dressed up properly. Enter live fake where you can morph your face into an image of yourself dressed up or someone else for fun meetings!
Other times there isn't simple enough bandwidth to facilitate video transmission, enter Lip Sync which can be extended to build videos at a server before being routed to participants.

The Hack has 3 components:
1. Lip Sync - generates a video from  an audio + photo
2. Live Fake - generates transformed video stream from a photo (model) + live video input
3. Electron.js wrapper - a wrapper application to hit the above 2 models run via Collab

Architecture: 
<img src="Architecture.png">
## To Use
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

