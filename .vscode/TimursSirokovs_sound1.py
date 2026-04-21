from winsound import Beep

notes = {
    'C': 261,
    'D': 293,
    'E': 329,
    'F': 349,
    'G': 392,
    'A': 440,
    'B': 493,
    'C2': 523,
    ' ': 37
}

melodie = 'EEFG GFED CCDE EDD'

for note in melodie:
    if note in notes:
        Beep(notes[note], 400)