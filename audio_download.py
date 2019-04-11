from wget import download
from database import *
import asyncio
from time import time


@db_session
def get_words():
    word_dict = dict()
    for w in Words.select().order_by(Words.word).limit(200, 300):
        word_dict[w.word] = w.audio

    return word_dict


async def downloader(word, audio):
    url = "https://audio.vocab.com/1.0/us/{}.mp3".format(audio)
    download(url, "audio/{}.mp3".format(word))
    print("downloaded {}".format(word))


async def download_audio():
    words = get_words()
    tasks = []
    for k in words:
        tasks.append(asyncio.create_task(downloader(k, words[k])))

    for task in tasks:
        await task


def main():
    start_time = time()
    asyncio.run(download_audio())
    print("duration: {}".format(time() - start_time))


if __name__ == '__main__':
    main()
