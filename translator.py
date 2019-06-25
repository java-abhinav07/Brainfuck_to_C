import re


def brainfuck_to_c(source):
    # remove redundant code
    sourceregex = re.compile(r'[^+-<>,.\[\]]')  # ^ means negation or not
    source = re.sub(sourceregex, '', source)

    # remove illegal values
    empty = ''
    while source != empty:
        empty = source
        source = re.sub('\+-|-\+|<>|><|\[\]', '', source)

    # number of brackets
    if source.count("]") != source.count("["):
        return "Error!"

    braces = re.sub('[^\[\]]', '', source)
    while braces.count('[]'):
        braces = braces.replace('[]', '')
    if braces:
        return 'Error!'

    # translation
    translated_c = []

    nums = re.findall('\++|-+|>+|<+|[.,\[\]]', source)  # returns a lost of strings
    indent = 0
    for x in nums:
        if x[0] in '+-<>':
            line = ('%sp %s= %s;\n' %
                    ('*' if x[0] in '+-' else '',
                     '+' if x[0] in '+>' else '-',
                     len(x)))
        elif x == '.':
            line = 'putchar(*p);\n'
        elif x == ',':
            line = '*p = getchar();\n'
        elif x == '[':
            line = 'if (*p) do {\n'
        elif x == ']':
            line = '} while (*p);\n'
            indent -= 1
        translated_c.append('  ' * indent + line)
        if x == '[':
            indent += 1

    return ''.join(translated_c)
