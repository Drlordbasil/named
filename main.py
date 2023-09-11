Commit Message:
Optimize Python script

1. Remove unused nltk library import
2. Use set instead of list for stopwords
3. Use defaultdict for languages dictionary
4. Move initialization of Translator object outside functions
5. Use f-strings for string formatting
