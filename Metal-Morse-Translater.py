import pygame

pygame.init()
screen = pygame.display.set_mode([150, 140])
clock = pygame.time.Clock()
pygame.display.set_caption("Headbanging Morse Code")
head_up = pygame.image.load("pictures/up-head.png")
head_down = pygame.image.load("pictures/down-head.png")
pygame.mixer.music.load("sounds/Blegg Meddl 3.5.mp3")
original_text = input("Please enter your text: ").upper()
game_active = True
pygame.mixer.init()

MORSE_CODE_DICT = { 'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-', '!': '-.-.--'}

def createmorsecode(text):
    morsecode = ""
    for letter in original_text:
        if letter != " ":
            morsecode += MORSE_CODE_DICT[letter] + " "
        else:
            morsecode += " "
    return list(morsecode)

morse = createmorsecode(original_text)
morse_string = "".join(map(str, createmorsecode(original_text)))

print(original_text)
print(morse_string)

pygame.mixer.music.play(-1)

while game_active:

    if morse[0] == "-":
        screen.blit(head_up, (0, 0))
        morse.pop(0)
    elif morse[0] == ".":
        screen.blit(head_down, (0, 0))
        pygame.display.flip()
        morse.pop(0)
    elif morse[0] == " ":
        screen.blit(head_up, (0, 0))
        morse.pop(0)
    if len(morse) == 0:
        game_active = False

    pygame.display.flip()
    clock.tick(7)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
