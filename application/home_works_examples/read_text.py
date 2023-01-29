from application.config.paths import FILES_INPUT


def read_text():
    data = FILES_INPUT
    with open(data) as a:
        reading = a.read()
    return reading
