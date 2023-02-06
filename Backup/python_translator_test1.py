from python_translator import Translator

translator = Translator()
#result = translator.translate("Hello world!", "spanish", "english")
result = translator.translate("fuck", "japanese", "english")
print(type(result))
print(result)
print(dir(result))
print(type(result.new_text))
print(result.original_text)