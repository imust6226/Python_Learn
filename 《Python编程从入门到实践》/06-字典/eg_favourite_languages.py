#coding = utf-8

favourite_language = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }
print("Sarah's favourite languages is " +
       favourite_language['sarah'].title() + '.')



for name,language in favourite_language.items():
    print("\n" + name.title() + "'s favourite language is " +
          language.title() + ".")

# 遍历所有的键

friends = ['phil', 'sarah']

for name in favourite_language.keys():
    print("\n" + name.title())
    if name in friends:
        print("Hi," + name.title() +
              ",I see your favourite languages is " +
              favourite_language[name].title() + ".")
    if 'erin' not in favourite_language.keys():
        print("Erin, please take your poll!")
    else:
        print(favourite_language['erin'].title())


# 遍历所有的值
print("The following languages have been mentioned:")
for language in favourite_language.values():
    print(language.title())
