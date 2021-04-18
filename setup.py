import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="ZaloTTS",
    version="0.0.1",
    description="Zalo Text To Speech",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/iconclub/zalo-tts",
    author="Hieu Nguyen",
    author_email="hieunguyen1053@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=[
        "zalo_tts",
    ],
    include_package_data=True,
    install_requires=[
        "PyAudio==0.2.11",
        "python-dotenv==0.17.0",
    ],
    entry_points={},
)