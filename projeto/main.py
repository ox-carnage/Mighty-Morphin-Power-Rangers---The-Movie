import json
import os

def load_config(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def load_input_data(input_file):
    with open(input_file, 'r') as f:
        return f.read()

def process_data(input_data, config):
    output_data = ""
    lines = input_data.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith('($'):
            hex_values = line.split(')')[:-1]
            for j, hex_value in enumerate(hex_values):
                if hex_value == '($FF)($FF':
                    output_data += config['endstring'] + '\n'
                else:
                    output_data += config['db'] + ' ' + hex_value.replace('($', '$') + '\n'
                    if (j+1) % 4 == 0 and i+1 < len(lines):  # Adicionado verificação de limite
                        output_data += config['script_historia'] + '("' + lines[i+1] + '")\n'
                        lines[i+1] = ""  # Remove the text that has been processed
    return output_data

# Exemplo de uso
config_file_path = os.path.join('config', 'config.json')  # Ajuste o caminho do arquivo aqui
input_file_path = 'fase1.txt'  # Substitua por seu arquivo de entrada
config = load_config(config_file_path)
input_data = load_input_data(input_file_path)
print(process_data(input_data, config))
