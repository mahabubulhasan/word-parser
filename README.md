## Why it even exsists?
For a long since i've been looking for a good vocabulary app for my Android phone. But there was none (_oviously there are some apps out there but none of them satisfy me enough so that i had to build my own_). What a vocuabulary app do?! teaches us vocabulary!!! and where does it get those vocabulary?! well here comes this `word-parser`. This tool parse the vocabulary from the internet.

For my app idea i wanted to have these: 
- the word
- short definition or meaning of the word
- a detailed definition of the word
- some example sentences 
- and audio of pronunciation


## Setup
First make sure you have __Python 3__ and then just follow this flow of instructions and you are good to go

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

**NOTE:** After download the audio files are named after the word it stands for, for example if the word is `abase` then the audio filename of this word will be `abase.mp3`

## Caveats
In `main.py` take a look at this code block, 
```python
    for index in range(1482, 2000, 10):
        print("scrapping started from {}".format(index))
        words = get_words(index)
        scrape_words(words, scrapper)
```
Here `range(1482, 2000, 10)` means scrape `10` words at a time starting form index in the sqlite `1482` to `2000`.

I know it looks weird but it is important since the site we are scrapping sending too many request to that site will end us by getting blocked by them. In `range(start, end, stepping)`, the start and end part is important. You need to look at the sqlite database and just make sure you are not sending the same word scrape request twice, by that i mean if a word is already scrapped don't do it again for that word.

In the `audio_download.py` take a look at this code block for the same reason mentioned earlier,
```python
    for w in Words.select().order_by(Words.word).limit(500, 1000):
        word_dict[w.word] = w.audio
```
Here `limit(start, offset)` is a `ponyorm` method, and `limit(500, 1000)` means get me `500` words from the sqlite database starting from index `1000`
