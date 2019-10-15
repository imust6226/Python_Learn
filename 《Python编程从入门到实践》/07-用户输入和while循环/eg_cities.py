#coding = utf-8

prompt = "Tell me,I'll repeat it back to you:"
prompt += "\nEneter 'quit' to break:"

active = True
while active:
    msg = input(prompt)
    if msg == 'quit':
        break
    else:
        print(msg + ",Suscessfully!")
