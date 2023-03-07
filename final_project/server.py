from flask import Flask, request, jsonify
from translator import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    # Get the request data as JSON
    data = request.get_json()

    # Get the text to translate and the target language from the JSON data
    text = data.get('text')
    target_language = data.get('target_language')

    # Translate the text using the Translator class
    if target_language == 'fr':
        translated_text = translator.translate_en_to_fr(text)
    elif target_language == 'en':
        translated_text = translator.translate_fr_to_en(text)
    else:
        return jsonify({'error': 'Invalid target language'}), 400

    # Return the translated text as JSON
    return jsonify({'text': translated_text}), 200

if __name__ == '__main__':
    app.run(debug=True)
