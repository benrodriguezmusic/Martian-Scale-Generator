from playtones import play_sawtooth

initial_freq = float(input("Initial Frequency: "))
equiv_ratio = float(input("Equivalence Ratio: "))
gen_ratio = float(input("Generative Ratio: "))
iterations = int(input("Number of Iterations: "))
tones = []

freq_list = [initial_freq]


def append_freq():

    last_freq = freq_list[-1]
    next_freq = last_freq * gen_ratio
    while next_freq > initial_freq * equiv_ratio:
        next_freq = next_freq / equiv_ratio
    if next_freq not in freq_list:
        freq_list.append(round(next_freq, 2))
    scale_list = freq_list.copy()
    scale_list.append(initial_freq * equiv_ratio)
    scale_list.sort()
    rounded_scale = [round(freq, 1) for freq in scale_list]
    return scale_list, rounded_scale


def wellness_check(i):
    scale_list, rounded_scale = append_freq()
    interval_list = []

    for n in range(1, len(scale_list)):
        next_interval = round((scale_list[n] / scale_list[n - 1]), 3)
        if next_interval not in interval_list:
            interval_list.append(next_interval)

    print("")
    print(f"{i + 1})")
    print(f"int: {interval_list}")
    print(f"freqs: {freq_list}")
    print(f"SCALE: {rounded_scale}")
    if len(interval_list) == 2:
        print("'well formed' kinda")
    if i == (iterations - 1):
        return rounded_scale


for i in range(1, iterations):
    tones = wellness_check(i)

while True:
    for t in tones:
        play_sawtooth(t)
    if not input("Press the space bar to play it again, or press any key to finish: ") == " ":
        break
