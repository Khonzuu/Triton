import os

dot_freq_range = (109, 113)
dash_freq_range = (87, 90)
star_freq_range = (97, 100)

cipher = {
    'A': '---', 'B': '--.', 'C': '--*', 'D': '-.-', 'E': '-..', 'F': '-.*',
    'G': '-*-', 'H': '-*.', 'I': '-**', 'J': '.--', 'K': '.-.', 'L': '.-*',
    'M': '..-', 'N': '...', 'O': '..*', 'P': '.*-', 'Q': '.*.', 'R': '.**',
    'S': '*--', 'T': '*-.', 'U': '*-*', 'V': '*.-', 'W': '*..', 'X': '*.*',
    'Y': '**-', 'Z': '**.', '/': '***'
}

def read_pitch_file(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    return [float(line.strip().split()[1]) for line in lines]

def get_symbol_from_freq(freq):
    if dot_freq_range[0] <= freq <= dot_freq_range[1]:
        return '.'
    elif dash_freq_range[0] <= freq <= dash_freq_range[1]:
        return '-'
    elif star_freq_range[0] <= freq <= star_freq_range[1]:
        return '*'
    return None

def analyze_pitch_data(pitch_data):
    symbols = []
    count = 0
    prev_symbol = None

    for i, freq in enumerate(pitch_data):
        symbol = get_symbol_from_freq(freq)
        
        if symbol is None:
            continue

        if prev_symbol is None:
            prev_symbol = symbol
            count = 1
        elif prev_symbol == symbol:
            count += 1
        else:
            symbols.extend([prev_symbol] * (count // 5))
            prev_symbol = symbol
            count = 1

        if i == len(pitch_data) - 1:
            symbols.extend([prev_symbol] * (count // 5))

    return symbols



def output_groups(symbols, group_size=3):
    grouped_symbols = [symbols[i:i+group_size] for i in range(0, len(symbols), group_size)]
    return grouped_symbols

def translate_using_cipher(grouped_symbols, cipher):
    translated_text = []
    for group in grouped_symbols:
        group_str = ''.join(group)
        for key, value in cipher.items():
            if group_str == value:
                translated_text.append(key)
                break
    return ''.join(translated_text)

def main():
    input_file = os.path.join('coded', 'output.txt')
    pitch_data = read_pitch_file(input_file)
    symbols = analyze_pitch_data(pitch_data)
    
    print("Symbols:", ''.join(symbols))

    grouped_symbols = output_groups(symbols)
    for group in grouped_symbols:
        print(''.join(group))

    translated_text = translate_using_cipher(grouped_symbols, cipher)
    print("Translated text:", translated_text)

    output_folder = 'Dcoded'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, 'decoded.txt')
    with open(output_file, 'w') as f:
        f.write(translated_text)

if __name__ == '__main__':
    main()

  
