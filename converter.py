import os

def convert_file(input_path, output_path):
    try:
        with open(input_path, 'r') as f:
            content = f.read()

        converted_content = content.upper()

        with open(output_path, 'w') as f:
            f.write(converted_content)

        return True
    except Exception as e:
        print("Conversion error:", e)
        return False
