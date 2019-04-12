## Why it event exsists?
For a long since i've been looking for a good vocabulary app for my Android phone. But there was none (_oviously there are some apps out there but none of them satisfy me enough so that i had to build my own_). What a vocuabulary app do?! teaches us vocabulary!!! and where does it get those vocabulary?! well here comes this `word_parser`. This tool parse the vocabulary from the internet.

For my app idea i wanted to have these: 
- the word
- short definition or meaning of the word
- a detailed definition of the word
- some example sentences 
- and audio of pronunciation


## Setup
Just follow this flow of instructions and you are good to go

```
$ git clone https://github.com/mahabubulhasan/word_parser.git
$ cd word_parser
$ pip install setup.py
```

## Steps to parse words
1. run `doc_reader.py` to parse the *words* and *short definitions* from files in the `doc` directory and save them into a sqlite database.
1. run `main.py`, it will read the *words* from the sqlite file, which is generated in step 1, and scrape the example sentences, detailed definition, and audio file url from a remote site, and update them into the sqlite database
1. run `audio_download.py` will download the audio from remote site and saves them into `audio` directory
1. finally run the `json_builder.py` will build the `json` file using everything in the sqlite database in the following format and save in the `data` directory:
```json
[
  {
    "word": "abase",
    "definition": "cause to feel shame",
    "details": "To <i>abase</i> something or someone is to humiliate them \u2014 no, more than just humiliate them. If you <i>abase</i> another person you are bringing them low, humbling them in a mean, <i>base</i> manner. Not nice at all.",
    "examples": [
      "Why do you need to <strong>abase</strong> and demean me?",
      "His spokesman Seumas Milne flew to Russia in 2014 to <strong>abase</strong> himself before Putin and tried to spread conspiracy theories about the Salisbury chemical attack.",
      "And yet when he says, \u201cI am from outer space,\u201d some of you actually shut your eyes, <strong>abase</strong> your intellects, and believe!",
      "How dare McCain say I am a na\u00efve egotist with a sympathy for autocrats who abjectly <strong>abased</strong> myself before a tyrant and failed to defend American values?"
    ]
  },
  
  ...
]
```

**NOTE:** After download audio files are named as according to the word it stands for, for example if the word is `abase` them the audio file name of this word will be `abase.mp3`
