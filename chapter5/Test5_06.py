def counter(representation):
    if representation[1] == '+':
        return float(representation[0]) + float(representation[2])
    elif representation[1] == '-':
        return float(representation[0]) - float(representation[2])
    elif representation[1] == '*':
        return float(representation[0]) * float(representation[2])
    elif representation[1] == '/':
        return float(representation[0]) / float(representation[2])
    elif representation[1] == '%':
        return float(representation[0]) % float(representation[2])
    elif representation[1] == '**':
        return float(representation[0]) ** float(representation[2])
    else:
        return 'error'

print counter("1+4")