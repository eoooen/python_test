import sys

handler_world = None
handler_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if handler_world == word:
        handler_count += count
    else:
        if handler_world:
            print('%s\t%s' % (handler_world, handler_count))
        handler_world = word
        handler_count = count
if handler_world == word:
    print('%s\t%s' % (handler_world, handler_count))



