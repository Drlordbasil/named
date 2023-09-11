Here are some optimizations for the Python script:

1. Remove unused libraries: The script imports the nltk library but doesn't use it. You can remove the following line:
    ```python
    import nltk
    ```

2. Use a set instead of a list for stopwords: The script imports the stopwords corpus from the nltk library and converts it to a list. However, using a set for stopwords can provide faster membership checks. Replace the following line:
    ```python
    stopwords_list = list(stopwords.words('english'))
    ```
    with:
    ```python
    stopwords_set = set(stopwords.words('english'))
    ```

3. Use a defaultdict for languages: The script defines a dictionary of languages and their abbreviations. However, there are unnecessary checks for missing values. Use a defaultdict instead to provide a default value for missing keys. Add the following import statement at the top of the script:
    ```python
    from collections import defaultdict
    ```
    Then, replace the `languages` dictionary with the following line:
    ```python
    languages = defaultdict(lambda: '', {'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', ...})
    ```

4. Move the initialization of the `Translator` object outside the translation functions: In the `text_to_text_translation` and `speech_to_text_translation` functions, the `Translator` object is created multiple times. This can be moved outside the functions to improve performance. Add the following line at the top of the script, after the import statements:
    ```python
    translator = Translator(service_urls=['translate.google.com'])
    ```
    Then, remove the object creation line from the `text_to_text_translation` and `speech_to_text_translation` functions.

5. Use f-strings for formatting: In a few places, the script uses string concatenation to format messages. You can use f-strings for more readable and concise formatting. For example, replace this line:
    ```python
    print(f"\nTranslated text ({target_language}): {translated_text}")
    ```
    with:
    ```python
    print(f"\nTranslated text ({target_language}): {translated_text}")
    ```

These optimizations should help improve the code performance and readability.
