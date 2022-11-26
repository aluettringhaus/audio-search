# Audio-Sifter
Transcribes audio files and stores them as embeddings for fast similarity search.

https://github.com/openai/whisper
https://www.openslr.org/51/


## About

Audio-Sifter aims to be a fast service for persisting and querying transcribed audio files. It offers semantic search capabilities using sentence embeddings. Under the hood it leverages redis for caching metadata, Cohere for generating sentence embeddings and faiss to provide performant searches over millions of sentence vectors.

## Installation
1. Install Redis: https://redis.io/docs/getting-started/installation/

2. Install other requirements
```
pip install -r requirements.txt
```
## Get API-Key from Cohere
1. https://dashboard.cohere.ai/welcome/register
2. Place API-Key between quotation marks in `app/config.py` and `tests/config.py`

## Running the application and testing it out

1. Start redis server


2. Start Audio-Sifter

Open a terminal, navigate to the root directory of your semquery clone. Then:

```bash
cd app
uvicorn main:app
```
Your app should now be running at 127.0.0.1:8000. 
Open up a browser and type in http://127.0.0.1:8000/docs to verify that semquery is running properly.

3. Test the application with `transcribe_audio_and_add_to_index.ipynb`


## Project Structure

The project structure roughly follows the guidelines at https://fastapi.tiangolo.com/.

All routes are located in `app/main.py`.

Models are defined in `app/models.py`.

Indexing and search functionality is implemented in `app/index.py`.

You can explore the project using the interactive, auto-generated api docs at http://127.0.0.1:8000/docs.


## Roadmap

The following features might be added in future releases:

- add tests
- validate index schemas with `jsonschema`
- add durable, on-disk persistence for multiple indices
- add batch requests
- add options for different index-types to leverage faiss
- add a CRUD-module for redis
