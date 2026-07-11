# AI Dictionary Collector

Egy teljes angol-magyar szótárgyűjtő és tanító adatgeneráló rendszer AI modellek számára.

## Főbb funkciók

1. **Automatikus szótárletöltés** - Több forrásból (GitHub repositories)
2. **Automatikus fordítás** - Google Translate API használatával
3. **Példamondat generálás** - Mindkét nyelven értelmes mondatok
4. **Több kimeneti formátum** - JSON, JSONL, CSV, TXT
5. **Metaadatok** - Szófaj, nehézségi szint, címkék

## Telepítés

```bash
cd ai_dictionary_collector
pip install -r requirements.txt
```

## Használat

### Teljes futtatás (ajánlott)
```bash
python main.py
```

### Gyors teszt (50 szó)
```bash
python quick_test.py
```

### Konfigurálás
Szerkeszd a `config.py` fájlt:
- `MAX_WORDS`: Feldolgozandó szavak maximális száma
- `TRANSLATION_DELAY`: API rate limiting
- `MAX_WORKERS`: Párhuzamos fordítók száma

## Kimeneti formátumok

A `data/` mappában:
- `translations.json`: Teljes angol-magyar szótár
- `training_data.json`: Teljes tanító adatkészlet
- `training_data.jsonl`: JSON Lines formátum (AI training)
- `training_data.csv`: CSV formátum
- `word_pairs.txt`: Egyszerű szópárok

## Példa adat struktúra

```json
{
  "id": 1,
  "english_word": "algorithm",
  "hungarian_translation": "algoritmus",
  "english_example": "The word 'algorithm' means algoritmus in Hungarian.",
  "hungarian_example": "Az 'algorithm' szó magyarul algoritmust jelent.",
  "word_type": "noun",
  "difficulty": "intermediate",
  "tags": ["medium", "uncommon", "noun"]
}
```

## AI tanításhoz való felhasználás

### JSONL formátum (legjobb AI-hoz)
```json
{"english_word": "hello", "hungarian_translation": "szia", ...}
{"english_word": "world", "hungarian_translation": "világ", ...}
```

### CSV formátum
```csv
id,english_word,hungarian_translation,english_example,hungarian_example,word_type,difficulty
1,hello,szia,"The word 'hello' means szia in Hungarian.","A(z) 'hello' szó magyarul sziát jelent.",noun,beginner
```

## Teljesítmény

- **Kis méret**: 1,000 szó ~ 5-10 perc
- **Közepes**: 10,000 szó ~ 1-2 óra  
- **Nagy**: 50,000+ szó ~ 6-12 óra (API rate limiting miatt)

## Figyelmeztetések

1. **API Rate Limiting**: A Google Translate ingyenes változata korlátozott
2. **Internet kapcsolat**: Szükséges a letöltéshez és fordításhoz
3. **Fordítás pontossága**: Automatikus fordítás, lehetnek hibák

## Fejlesztési lehetőségek

- [ ] További fordító API-k (DeepL, Microsoft)
- [ ] Offline fordító modellek
- [ ] Hanganyag generálás
- [ ] Képasszociációk
- [ ] Gyakorisági adatok
- [ ] Témakörök szerinti csoportosítás