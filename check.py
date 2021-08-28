import os

texts = []

for folder in os.listdir('data/'):
    texts = []
    try:
        for file in os.listdir('data/'+folder):
            if file[-3:] == 'txt':
                with open(f'data/{folder}/{file}', 'r') as f:
                    data = f.read()
                    print(data)
                quality = input("(q/Enter)")
                if quality == '':
                    texts.append(data)
        print(texts)
    except:
        pass