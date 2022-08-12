
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def abbrev_name(name):
    char_1 = name[0].upper()
    char_2 = ''
    for char in range(len(name)):
        if name[char] == ' ':
            char_2 = name[char + 1].upper()

    return "'" + char_1 + "." + char_2 + "'"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    abbrev_name('Philip Moris')