import re


def color_count_in_round(round_str, color):
    count_str = re.findall(fr'\d+ {color}', round_str)
    if len(count_str) == 1:
        return int(re.findall(r'\d+', count_str[0])[0])
    elif len(count_str) > 1:
        raise RuntimeError("Too many colors in a round: " + round_str)
    else:
        return 0


file_path = 'input'
with open(file_path, 'r') as file:
    max_counts = {"red": 12, "green": 13, "blue": 14}
    valid_game_id_sum = 0
    power_sum = 0
    for game_line in file:
        game_name = game_line[:7]
        game_id = int(re.findall(r'\d+', game_name)[0])
        is_game_valid = True
        min_counts = {"red": 0, "blue": 0, "green": 0}
        for round in game_line[7:].split(";"):
            for color, max_count in max_counts.items():
                count = color_count_in_round(round, color)
                if count > min_counts[color]:
                    min_counts[color] = count
                if count > max_count:
                    is_game_valid = False
        # we now have min counts, find the power
        power = 1
        for i, min_count in min_counts.items():
            power = power * min_count

        power_sum = power_sum + power

        if is_game_valid:
            valid_game_id_sum += game_id

    print("P1: " + str(valid_game_id_sum))
    print("P2: " + str(power_sum))
