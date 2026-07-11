from main import DictionaryCollector
import json

def quick_test():
    """Gyors teszt - csak 50 szóval"""
    print("🚀 Gyors teszt indítása (50 szó)...")
    
    collector = DictionaryCollector()
    
    # Készítsünk egy kis teszt listát
    test_words = [
        "hello", "world", "computer", "programming", "artificial",
        "intelligence", "learning", "data", "science", "algorithm",
        "network", "system", "software", "hardware", "database",
        "security", "privacy", "encryption", "authentication", "authorization",
        "framework", "library", "module", "package", "dependency",
        "interface", "protocol", "standard", "specification", "implementation",
        "deployment", "maintenance", "documentation", "tutorial", "example",
        "exercise", "practice", "training", "education", "knowledge",
        "experience", "expertise", "skill", "ability", "competence",
        "proficiency", "mastery", "excellence", "achievement", "success"
    ]
    
    print(f"Teszt szavak: {len(test_words)}")
    
    # Fordítás
    translations = {}
    for word in test_words:
        translation = collector.translate_word(word)
        translations[word] = translation
        print(f"  {word} → {translation}")
    
    # Mentés
    import os
    os.makedirs("test_data", exist_ok=True)
    
    with open("test_data/test_translations.json", "w", encoding="utf-8") as f:
        json.dump(translations, f, ensure_ascii=False, indent=2)
    
    # Példamondatok generálása
    training_data = []
    for i, (word, translation) in enumerate(translations.items()):
        eng_sentence, hun_sentence = collector.generate_example_sentences(word, translation)
        
        entry = {
            "id": i + 1,
            "english_word": word,
            "hungarian_translation": translation,
            "english_example": eng_sentence,
            "hungarian_example": hun_sentence,
            "word_type": collector.detect_word_type(word),
            "difficulty": collector.calculate_difficulty(word)
        }
        
        training_data.append(entry)
        print(f"\n{word.upper()}:")
        print(f"  Angol: {eng_sentence}")
        print(f"  Magyar: {hun_sentence}")
    
    # Mentés
    with open("test_data/test_training.json", "w", encoding="utf-8") as f:
        json.dump(training_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Teszt kész! {len(training_data)} bejegyzés generálva.")
    print("   Fájlok: test_data/ mappában")

if __name__ == "__main__":
    quick_test()