def char_count(s):
    count={}

    for ch in s:
        count[ch]=count.get(ch,0)+1
    print(count)

char_count("hello")