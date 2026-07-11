# AI Dictionary Collector — Automated English-Hungarian Dictionary and Training Data Generator

**Status:** ⚠️ Prototype — translation pipeline works, needs API keys for Google Translate


**An automated tool for building English-Hungarian dictionaries and generating AI training data. Capable of bulk-translating words, collecting synonyms, and generating example sentences.**

## 📚 Description

AI Dictionary Collector is a tool that:

- Provides **English → Hungarian** automatic word translation
- **Collects synonyms** in both languages
- **Generates example sentences** for every word
- Produces **structured JSON output** for AI training
- Supports **batch processing** — thousands of words at once
- Is **configurable** — customizable source/target language, output format

## 📁 File Structure

```
ai_dictionary_collector/
├── config.py                    # Configuration (API keys, settings)
├── quick_test.py                # Quick test with 50 words
├── run.bat                      # Windows launcher
├── requirements.txt             # Python dependencies
├── data/                        # Generated data directory
└── README.md
```

## 🚀 Usage

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run quick test

```bash
python quick_test.py
```

This tests the system with 50 English words:
- English → Hungarian translation
- Synonym lookup
- Example sentence generation
- Results saved in JSON format

### Batch launch

```bash
run.bat
```

### Configuration

The following can be set in `config.py`:

```python
# API settings
API_KEY = "your-api-key"
TARGET_LANGUAGE = "hu"

# Collection settings
MAX_WORDS = 5000
INCLUDE_SYNONYMS = True
INCLUDE_EXAMPLES = True

# Output
OUTPUT_DIR = "data/"
OUTPUT_FORMAT = "json"
```

## 📦 Dependencies

```bash
pip install requests python-dotenv
```

- **Python 3.8+**
- **requests** — for API calls
- **python-dotenv** — environment variable management

## 📊 Output Format

```json
{
  "word": "computer",
  "translation": "számítógép",
  "synonyms": {
    "english": ["PC", "machine", "processor"],
    "hungarian": ["PC", "gép", "processzor"]
  },
  "examples": [
    {"english": "I use my computer every day.", "hungarian": "Minden nap használom a számítógépemet."},
    {"english": "The computer is running slowly.", "hungarian": "A számítógép lassan fut."}
  ],
  "part_of_speech": "noun",
  "difficulty": "A1"
}
```

## 🎯 Use Cases

- **AI training datasets** — fine-tuning language models
- **Dictionary building** — source material for online/offline dictionaries
- **Language learning** — generating flashcards and practice exercises
- **Translation memory** — expanding machine translation systems

## 🔧 Customization

By modifying `config.py`:

- Switch to a different language pair (e.g., English-German, English-French)
- Change output format (JSON, CSV, SQLite)
- Apply filtering criteria (part of speech, difficulty level)

## Author
Zsombi & Hermes Agent (Nous Research)
