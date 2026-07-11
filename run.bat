@echo off
echo AI Dictionary Collector
echo ======================
echo.
echo Válassz egy opciót:
echo 1. Teljes futtatás (ajánlott)
echo 2. Gyors teszt (50 szó)
echo 3. Csak letöltés (fordítás nélkül)
echo 4. Csak fordítás (letöltés nélkül)
echo 5. Kilépés
echo.

set /p choice="Választás (1-5): "

if "%choice%"=="1" (
    echo Teljes futtatás indítása...
    python main.py
    pause
) else if "%choice%"=="2" (
    echo Gyors teszt indítása...
    python quick_test.py
    pause
) else if "%choice%"=="3" (
    echo Csak letöltés indítása...
    python -c "
from main import DictionaryCollector
collector = DictionaryCollector()
words = collector.download_dictionary()
print(f'Letöltve: {len(words)} szó')
import json
import os
os.makedirs('data', exist_ok=True)
with open('data/words_only.json', 'w') as f:
    json.dump(list(words)[:1000], f, indent=2)
print('Mentve: data/words_only.json')
"
    pause
) else if "%choice%"=="4" (
    echo Csak fordítás indítása...
    python -c "
from main import DictionaryCollector
collector = DictionaryCollector()
# Teszt szavak
test_words = ['hello', 'world', 'python', 'programming', 'ai']
for word in test_words:
    trans = collector.translate_word(word)
    print(f'{word} -> {trans}')
"
    pause
) else (
    echo Kilépés...
    timeout /t 2
)