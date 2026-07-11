import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Dictionary sources
    DICTIONARY_URLS = [
        "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt",
        "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt",
        "https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/en/en_50k.txt"
    ]
    
    # Translation settings
    TRANSLATION_DELAY = 0.1  # másodperc szavanként (API rate limiting)
    MAX_WORKERS = 5          # párhuzamos fordítók száma
    BATCH_SIZE = 100         # kötegméret fordításhoz
    
    # Data generation
    MAX_WORDS = 10000        # maximum feldolgozandó szavak száma
    GENERATE_EXAMPLES = True # példamondatok generálása
    
    # Output
    OUTPUT_DIR = "data"
    SAVE_PARTIAL = True      # részleges eredmények mentése
    PARTIAL_INTERVAL = 500   # hány szónként mentse részlegesen
    
    # Logging
    LOG_LEVEL = "INFO"
    LOG_FILE = "dictionary_collector.log"