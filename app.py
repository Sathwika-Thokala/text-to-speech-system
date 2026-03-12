from tts_engine import text_to_speech
from utils.file_handler import read_text_file

def main():

    print("Text to Speech System")
    print("----------------------")

    choice = input("1. Enter Text\n2. Read from File\nChoose option: ")

    if choice == "1":
        text = input("Enter the text to convert into speech: ")

    elif choice == "2":
        file_path = "input_text/sample.txt"
        text = read_text_file(file_path)

    else:
        print("Invalid option")
        return

    output_file = "output_audio/speech.mp3"

    text_to_speech(text, output_file)

    print("Audio generated successfully!")
    print("Saved at:", output_file)


if __name__ == "__main__":
    main()
