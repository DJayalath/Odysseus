# Odysseus
A content-based file type detector utilising artificial neural networks

## Quick Start
<b>THIS PROGRAM IS CURRENTLY HIGHLY EXPERIMENTAL. RUN AT YOUR OWN RISK.</b>
1. Clone this repository
2. Run `install.sh`

## Usage
`odysseus [OPTIONS] FILE`

Example: `odysseus ~/Pictures/cat.jpg` will predict the real file type of `cat.jpg`

## Detection Support
Images: `PNG, JPEG, GIF`

Documents: `PDF, DOC, DOCX`

Audio: `MP3`

odysseus is currently capable of identifying any of the above file types.

Although this repository is public, everything in it is still VERY EXPERIMENTAL. Support is being worked on for many more file types.

## Requirements
- Python 3

## Purpose
<b>Security</b>: Applications can be fooled when using extensions and magic numbers for file type detection. Harmful files spoofed to look like other file types can be detected.

<b>Labelling</b>: Mislabelled files can be detected using Odysseus and used to correctly set extensions.

<b>File Systems</b>: A secure file system might label file types using odysseus' content-based detection system rather than insecure methods like reading extensions or magic numbers.
