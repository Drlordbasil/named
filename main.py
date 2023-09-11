from googletrans import Translator
from collections import defaultdict
Commit: Remove unused nltk library import

```diff
- import nltk
```

Commit: Use set instead of list for stopwords

```diff
# Initialize stopwords as a set instead of a list
- stopwords = ['a', 'an', 'the', 'and']
+ stopwords = {'a', 'an', 'the', 'and'}
```

Commit: Use defaultdict for languages dictionary

```diff

# Initialize languages as a defaultdict
- languages = {}
+ languages = defaultdict(list)
```

Commit: Move initialization of Translator object outside functions

```diff

# Initialize translator object outside functions
- def translate(text, lang):
+ translator = Translator()

-     translator = Translator()
translation = translator.translate(text, dest=lang)

return translation.text
```

Commit: Use f-strings for string formatting

```diff
# Use f-strings for string formatting
- print("Translated text: " + translation_text)
+ print(f"Translated text: {translation_text}")
```

All optimizations have been committed.
