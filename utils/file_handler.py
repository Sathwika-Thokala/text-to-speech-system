def read_text_file(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text

    except FileNotFoundError:
        print("File not found!")
        return ""
