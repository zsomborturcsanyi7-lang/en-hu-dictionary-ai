# en-hu-dictionary-ai

Automated English-Hungarian dictionary dataset generator for machine translation.

## Overview & Purpose
en-hu-dictionary-ai processes raw bilingual text sources, builds structured dictionary entries, and outputs cleaned parallel corpora for training neural translation models.

## Key Features
- Bilingual sentence alignment and deduplication.
- Dictionary term extraction logic.
- Export to JSON and TSV dataset formats.

## Tech Stack & Dependencies
- **Language**: Python 3.8+

## Project Structure
```text
en-hu-dictionary-ai/
├── build_dictionary.py
├── utils/
└── README.md
```

## Installation & Setup

### Prerequisites
- Python 3.8+

### Steps
```bash
git clone https://github.com/zsomborturcsanyi7-lang/en-hu-dictionary-ai.git
cd en-hu-dictionary-ai
python build_dictionary.py
```

## Usage Examples
```bash
python build_dictionary.py --input raw_data/ --output dataset.json
```

## Status & License
Status: Functional Data Tool.
License: MIT
