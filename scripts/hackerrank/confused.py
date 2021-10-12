a = ['fb.com', 'tw.com', 'cat.com']

for i in a:
    print(f"i: {i}")
    if 'fb' in i:
        # print(i)
        # pass
        # print(i)
        i = i + 'tw'

    if 'tw' in i:
         pass
    else:
        print(i)

