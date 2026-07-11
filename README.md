# AI Dictionary Collector — Automatikus Angol-Magyar Szótár és Tanítóadat Generátor

**Automatizált eszköz angol-magyar szótár építésére és AI tanítóadat előállítására. Képes tömegesen fordítani szavakat, szinonimákat és példamondatokat gyűjteni.**

## 📚 Leírás

Az AI Dictionary Collector egy olyan eszköz, amely:

- **Angol → Magyar szavak** automatikus fordítása
- **Szinonimák gyűjtése** mindkét nyelven
- **Példamondatok** generálása minden szóhoz
- **Strukturált JSON kimenet** AI tanításhoz
- **Batch feldolgozás** — több ezer szó egyszerre
- **Konfigurálható** — testreszabható forrás- és célnyelv, kimeneti formátum

## 📁 Fájlszerkezet

```
ai_dictionary_collector/
├── config.py                    # Konfiguráció (API kulcsok, beállítások)
├── quick_test.py                # Gyorsteszt 50 szóval
├── run.bat                      # Windows indító
├── requirements.txt             # Python függőségek
├── data/                        # Generált adatok könyvtára
└── README.md
```

## 🚀 Használat

### Függőségek telepítése

```bash
pip install -r requirements.txt
```

### Gyorsteszt futtatása

```bash
python quick_test.py
```

Ez 50 angol szóval teszteli a rendszert:
- Fordítás angol → magyar
- Szinonimák keresése
- Példamondatok generálása
- Eredmények mentése JSON formátumban

### Batch indítás

```bash
run.bat
```

### Konfiguráció

A `config.py` fájlban állítható be:

```python
# API beállítások
API_KEY = "your-api-key"
TARGET_LANGUAGE = "hu"

# Gyűjtési beállítások
MAX_WORDS = 5000
INCLUDE_SYNONYMS = True
INCLUDE_EXAMPLES = True

# Kimenet
OUTPUT_DIR = "data/"
OUTPUT_FORMAT = "json"
```

## 📦 Függőségek

```bash
pip install requests python-dotenv
```

- **Python 3.8+**
- **requests** — API hívásokhoz
- **python-dotenv** — környezeti változók kezelése

## 📊 Kimenet formátum

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

## 🎯 Felhasználási terület

- **AI tanító adathalmaz** — nyelvi modellek finomhangolása
- **Szótár építés** — online/offline szótárak alapanyaga
- **Nyelvtanulás** — tanulókártyák és gyakorló feladatok generálása
- **Fordítási memória** — gépi fordító rendszerek bővítése

## 🔧 Testreszabás

A `config.py` módosításával:

- Más nyelvpárra állítható (pl. angol-német, angol-francia)
- Kimeneti formátum váltható (JSON, CSV, SQLite)
- Szűrési feltételek állíthatók (szófaj, nehézségi szint)
