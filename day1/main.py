import re

word_to_number = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                  "eight": "8", "nine": "9"}


def replace_number_words_with_digits(line):
    digits_only_line = ""
    for i in range(0, len(line)):
        if line[i].isdigit():
            digits_only_line += line[i]
        else:
            for word in word_to_number.keys():
                # Check if this word is within s
                if (i + len(word)) <= len(line):
                    is_word_present = word == line[i:i + len(word)]
                    if is_word_present:
                        digits_only_line += word_to_number[word]

    return digits_only_line


def calculate_calibration_value(line):
    line = re.sub(r'\D', "", line)
    if len(line) >= 1:
        startDigit = line[0]
        endDigit = line[len(line) - 1]
        return int(startDigit + "" + endDigit)


file_path = 'input'
with (open(file_path, 'r') as file):
    p1_sum = 0
    p2_sum = 0
    for line in file:
        p1_sum += calculate_calibration_value(line.strip())
        p2_sum += calculate_calibration_value(replace_number_words_with_digits(line.strip()))
    print("P1: " + str(p1_sum))
    print("P2: " + str(p2_sum))
