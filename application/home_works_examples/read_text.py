from application.config import FILES_INPUT_FILES


def read_text():
    data = FILES_INPUT_FILES
    with open(data) as a:
        reading = a.read()
    return reading


print(read_text())
