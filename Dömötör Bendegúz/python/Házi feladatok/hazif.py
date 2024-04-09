with open("./Hazi/nyelvek.txt", "r") as input_file:
    lines = input_file.readlines()

with open("nyelvek_es_ev.txt", "w") as output_file:
    for line in lines:
        fields = line.strip().split(";")
        language = fields[1].strip()
        year = fields[0].strip()
        output_file.write(f"{language} {year}\n")