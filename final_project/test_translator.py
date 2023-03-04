def test_translate_fr_to_en():
    # Initialize translator
    translator = Translator(api_key='BLCXCACU5xg4NVKKvPVlYAQcM_mFk_DzJfLHzRNSoCL1', url='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/572872b6-5ffc-408f-891f-939ec6bb0242', version='2018-05-01')
    
    # Test case 1: Basic translation
    french_text = 'Bonjour comment allez-vous?'
    expected_english_text = 'Hello, how are you?'
    assert translator.translate_fr_to_en(french_text) == expected_english_text
    
    # Test case 2: Translation of a longer sentence
    french_text = 'Le ciel est bleu et les oiseaux chantent.'
    expected_english_text = 'The sky is blue and the birds are singing.'
    assert translator.translate_fr_to_en(french_text) == expected_english_text
    
    # Test case 3: Translation of a single word
    french_text = 'amour'
    expected_english_text = 'love'
    assert translator.translate_fr_to_en(french_text) == expected_english_text

def test_translate_en_to_fr():
    # Initialize translator
    translator = Translator(api_key='BLCXCACU5xg4NVKKvPVlYAQcM_mFk_DzJfLHzRNSoCL1', url='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/572872b6-5ffc-408f-891f-939ec6bb0242', version='2018-05-01')
    
    # Test case 1: Basic translation
    english_text = 'Hello, how are you?'
    expected_french_text = 'Bonjour comment allez-vous?'
    assert translator.translate_en_to_fr(english_text) == expected_french_text
    
    # Test case 2: Translation of a longer sentence
    english_text = 'The quick brown fox jumps over the lazy dog.'
    expected_french_text = 'Le renard brun rapide saute par-dessus le chien paresseux.'
    assert translator.translate_en_to_fr(english_text) == expected_french_text
    
    # Test case 3: Translation of a single word
    english_text = 'love'
    expected_french_text = 'amour'
    assert translator.translate_en_to_fr(english_text) == expected_french_text
