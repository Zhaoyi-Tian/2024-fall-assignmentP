num_words = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
    'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
    'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
    'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
    'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000,
    'million': 1000000}
words=input().split()
result=0
current=0
k=1
for word in words:
    if word=='negative':
        k=-1
    elif word in ['thousand', 'million']:
        result+=num_words[word]*current
        current=0
    elif word=='hundred':
        current*=100
    else:
        current+=num_words[word]
result+=current
result*=k
print(result)
