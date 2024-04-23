with open('programming_languages.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

with open('programming_languages_output.txt', 'w', encoding='utf-8') as output_file:
    for line in lines:
        words = line.split()
        language = words[0]
        year = words[1].strip('[]')
        output_file.write(f'{language} {year}\n')