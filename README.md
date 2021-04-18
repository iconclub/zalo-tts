# Zalo Text-To-Speech

## I. Introduction

[Zalo Text-To-Speech (ZTTS)](https://zalo.ai/docs/api/text-to-audio-converter) engine delivers fast and premium quality audios from input Vietnamese text. ZTTS is optimized for realtime and high volume traffic applications such as news websites, voice streaming services, chatbots, and virtual assistants. ZTTS currently supports four Vietnamese voices including two Northern accents and two Southern accents.

## II. Install ZaloTTS

ZaloTTS supports python >= 3.7, <3.9

Installing from PyPI is the easiest option.

```bash
$ pip install ZaloTTS
```

## III. API_KEY

Get api key [here](https://zalo.ai/docs/api/getting-started).

You can use the api key as an argument to initialize the ZaloTTS object.

Or you can assign the environment variable ZALO_API_KEY in the `.env` file. The api key will be used when you initialize the ZaloTTS object.

```plaintext
# .env
ZALO_API_KEY = {your_api_key}
```

## III. Speakers

|ID|Name          |Constant              |
|--|--------------|----------------------|
|1 |South women   |ZaloTTS.SOUTH_WOMEN   |
|2 |Northern women|ZaloTTS.NORTHERN_WOMEN|
|3 |South men     |ZaloTTS.SOUTH_MEN     |
|4 |Northern men  |ZaloTTS.NORTHERN_MEN  |

## IV. Examples

```python
from zalo_tts import ZaloTTS

tts = ZaloTTS(speaker=ZaloTTS.NORTHERN_MEN)
tts.text_to_speech("Câu lạc bộ học thuật ICON xin chào các bạn.")
```