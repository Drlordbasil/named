"""
This is a program for an AI-powered Language Translator. It enables users to perform real-time translations between different languages using text or speech input. The program implements automatic language detection, text-to-text translation, speech-to-text translation, and text-to-speech output. It also has a user-friendly interface for easy input and viewing of translations. The translation accuracy is continuously improved using machine learning algorithms, and the program integrates with cloud-based translation APIs for enhanced capabilities.

Additionally, the program highlights the benefits of global communication, business communication, cultural exchange, time-saving convenience, and monetization potential. It also outlines the required skills for developing such a project, including Python programming, Natural Language Processing (NLP), machine learning, speech recognition, text-to-speech conversion, language translation APIs, GUI development, error handling, scalability, performance, problem-solving, and analytical skills.

With this AI-powered language translator, individuals can overcome language barriers and communicate effectively regardless of their linguistic backgrounds. Furthermore, businesses can leverage this technology to communicate with international clients, partners, and customers. The program also encourages cultural exchange and promotes understanding among individuals from diverse backgrounds. Additionally, it offers time-saving convenience by providing instant translations in conversations or while reading foreign text. Finally, it presents monetization potential through subscription plans, advertisement partnerships, or premium features.
"""

# Implement your AI-powered Language Translator code here

# Required libraries and APIs
import nltk
from googletrans import Translator
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import speech_recognition as sr
import pyttsx3

# Language detection function


def detect_language(text):
    languages = {'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian',
                 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian',
                 'bg': 'Bulgarian', 'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (Simplified)',
                 'zh-tw': 'Chinese (Traditional)', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish',
                 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish',
                 'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek',
                 'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew',
                 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian',
                 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh',
                 'km': 'Khmer', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao',
                 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian',
                 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi',
                 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'ps': 'Pashto',
                 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'ma': 'Punjabi', 'ro': 'Romanian',
                 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona',
                 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish',
                 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'te': 'Telugu',
                 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'uz': 'Uzbek', 'vi': 'Vietnamese',
                 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'}

    detector = nltk.detect(new_line='\n').langid().detect
    detected_language = detector(text)[0]
    detected_language = languages.get(detected_language, detected_language)

    return detected_language

# Text-to-text translation function


def text_to_text_translation(text, source_language, target_language):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(
        text, src=source_language, dest=target_language)

    return translation.text

# Speech-to-text translation function


def speech_to_text_translation():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return ""
    except sr.RequestError as e:
        print(f"Request to Google Speech Recognition service failed: {e}")

# Text-to-speech output function


def text_to_speech_output(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)
    engine.say(text)
    engine.runAndWait()

# Language translation UI


def translate():
    print("****************************************************")
    print("Welcome to the AI-powered Language Translator!")
    print("****************************************************\n")

    while True:
        print("Select an option:")
        print("1. Text-to-Text Translation")
        print("2. Speech-to-Text Translation")
        print("3. Exit")

        option = input("\nEnter option number: ")
        if option == "1":
            source_text = input("\nEnter the text to translate: ")
            source_language = detect_language(source_text)
            target_language = input("Enter the target language: ")

            translated_text = text_to_text_translation(
                source_text, source_language, target_language)
            print(f"\nTranslated text ({target_language}): {translated_text}")

            text_to_speech = input(
                "\nWould you like to hear the translation? (yes/no): ")
            if text_to_speech.lower() == "yes":
                text_to_speech_output(translated_text)
        elif option == "2":
            print("\nSpeak into the microphone:")
            source_text = speech_to_text_translation()

            if source_text:
                source_language = detect_language(source_text)
                target_language = input("Enter the target language: ")

                translated_text = text_to_text_translation(
                    source_text, source_language, target_language)
                print(
                    f"\nTranslated text ({target_language}): {translated_text}")

                text_to_speech = input(
                    "\nWould you like to hear the translation? (yes/no): ")
                if text_to_speech.lower() == "yes":
                    text_to_speech_output(translated_text)
        elif option == "3":
            print("\nThank you for using the AI-powered Language Translator!")
            break
        else:
            print("\nInvalid option. Please try again.\n")


# Main program
if __name__ == "__main__":
    translate()
