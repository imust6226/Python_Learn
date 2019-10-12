#coding = utf-8

class BuildPerson():

    def __init__(self):
        pass

    def build_person1(self, first_name, last_name):
        """返回一个字典，包含个人的姓名"""
        person = {'first':first_name, 'last': last_name}
        return person

    def build_person2(self, first_name, last_name, age = ''):
        """返回一个字典，包含个人的姓名"""
        person = {'first':first_name.title(), 'last': last_name.title()}
        if age:
            person['age'] = age
        return person
buildperson = BuildPerson()

print(buildperson.build_person2('jimi', 'hendrix'))
print(buildperson.build_person2('jimi', 'hendrix', 21))
print(buildperson.build_person2('jimi', 'hendrix', age = 18))
