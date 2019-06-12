from count import count


def brainfuck_to_c(source):
    legal = {">": "p += Y;\n", "<": "p -= Y;\n", ".": "putchar(*p);\n",
             ",": "*p = getchar();\n", "+": "*p += X;\n", "-": "*p -= X;\n",
             "[": "if (*p) do {\n  ", "]": "} while (*p);\n"}
    illegal = ['+-', '<>', '[]', '><']
    translated_c = ""
    for char in source:
        if char not in legal:
            source = source.replace(char, '')
    for i in range(len(source) - 1):
        if source[i:i + 2] in illegal:
            source = source.replace(source[i:i + 2], '')

    if source.count("]") != source.count("["):
        return "Error!"
    nums = count(source)
    for tup in nums:
        if tup[0] in legal:
            translated_c += legal.get(tup[0]).replace('Y', str(tup[1])).replace('X', str(tup[1]))

    return translated_c


