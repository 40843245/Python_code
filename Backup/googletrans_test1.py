from googletrans import Translator
translator = Translator()
x=translator.translate('안녕하세요.')
print(x)
print(type(x))
print(dir(x))
x1=x.__dict__()
print(x1['pronunciation'])
#translator.translate('안녕하세요.', dest='ja')