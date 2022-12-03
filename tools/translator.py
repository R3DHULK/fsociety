from translate import Translator
print('''
    Translator
 ========================================== 
      ''')
translator= Translator(from_lang=input(" [?] From Language You Want To Translate : "),to_lang=input(" [?] To Which Language You Want To Translate : "))
translation = translator.translate(input(" 🔴🔴 Enter The Text : "))
print (" Translation is : " + translation)
input("Enter To Exit")
