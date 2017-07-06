# Raspberry Pi: Timelapse Scripts

## Scripts

### lapse.sh

converting images to different framerate videos according to variables set in env.sh

### shutter.sh

taking a picture according to settings in env.sh

### server.sh

starting local web server using python3's http.server module on port 8122

### env.sh

configuration script

## Configuration

See env.sh

### Execution

I'm using crontab

## Requirements

- ffmpeg (for the shutter and timelapse)
- python3 (only for the managing files and hosting)
- imagemagick (for cleaning similar pictures)
- *some kind of shell*

## Roadmap

- [ ] reworking the markdown file
- [ ] wrapping in python module
- [ ] timestamp printing
- [ ] streaming current picture seperately

