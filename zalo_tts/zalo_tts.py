import json
import os
import urllib.parse
import urllib.request
import wave

import pyaudio
from dotenv import load_dotenv

load_dotenv()


class ZaloTTS:
    SOUTH_WOMEN = 1
    NORTHERN_WOMEN = 2
    SOUTH_MEN = 3
    NORTHERN_MEN = 4

    _SAMPWIDTH = 2
    _NCHANNELS = 1
    _FRAMERATE = 16000
    _CHUNK = 1024
    _URL = 'https://api.zalo.ai/v1/tts/synthesize'

    def __init__(self, speed: float = 1.0, speaker: int = 1, api_key: str = None):
        """Constructor

        Args:
            speed (float, optional): float value inside range [0.8, 1.2], larger is faster. Defaults to 1.0.
            speaker (int, optional): standard encoding for audio files. Defaults to 1.
            api_key (str, optional): authentication token to access API <https://zalo.ai/docs/api/getting-started>. Defaults to None.
        """
        self.speed = speed
        self.speaker = speaker
        self.api_key = api_key
        if self.api_key is None:
            self.api_key = os.getenv("ZALO_API_KEY")

    def _get_streaming_url(self, text: str) -> str:
        """Get streaming url

        Args:
            text (str): text content to synthesize

        Returns:
            str: generated streaming url
        """
        headers = {'apikey': self.api_key}
        payload = {
            'input': text,
            'speed': self.speed,
            'speaker_id': self.speaker
        }
        payload = urllib.parse.urlencode(payload).encode('utf-8')

        req = urllib.request.Request(
            method='POST',
            url=self._URL,
            headers=headers,
        )
        response = urllib.request.urlopen(url=req, data=payload)
        res_json = json.loads(response.read())
        if res_json['error_code'] == 0:
            return res_json['data']['url']
        elif res_json['error_code'] == 155:
            pass
        elif res_json['error_code'] == 401:
            pass
        elif res_json['error_code'] == 500:
            pass
        return ""

    def text_to_audio(self, text: str, filepath: str = 'audio.wav'):
        """Save the audio file

        Args:
            text (str): text content to synthesize
            filepath (str, optional): path of the audio file. Defaults to 'audio.wav'.
        """
        url_audio = self._get_streaming_url(text)
        response = urllib.request.urlopen(url=url_audio)
        file = open(filepath, 'wb')
        file.write(response.read())
        file.close()

    def play_audio(self, filepath: str = 'audio.wav'):
        """Play the audio file

        Args:
            filepath (str, optional): path of the audio file. Defaults to 'audio.wav'.
        """
        wf = wave.open(filepath, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(self._SAMPWIDTH),
                        channels=self._NCHANNELS,
                        rate=self._FRAMERATE,
                        output=True)
        while True:
            chunk = wf.readframes(self._CHUNK)
            if not chunk: break
            stream.write(chunk)
        stream.stop_stream()
        stream.close()
        p.terminate()

    def text_to_speech(self, text: str):
        """Text to speech

        Args:
            text (str): text content to synthesize
        """
        url_audio = self._get_streaming_url(text)
        response = urllib.request.urlopen(url=url_audio)
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(self._SAMPWIDTH),
                        channels=self._NCHANNELS,
                        rate=self._FRAMERATE,
                        output=True)
        while True:
            chunk = response.read(self._CHUNK)
            if not chunk: break
            stream.write(chunk)
        stream.stop_stream()
        stream.close()
        p.terminate()
