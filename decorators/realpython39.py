from functools import wraps


def normal(func):
    return func


def shout(func):
    @wraps(func)
    def shout_decorator(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return shout_decorator


def whisper(func):
    @wraps(func)
    def whisper_decorator(*args, **kwargs):
        return func(*args, **kwargs).lower()

    return whisper_decorator


def main():

    DECORATORS = {"normal": normal, "shout": shout, "whisper": whisper}

    voice = input(f"Choose your voice ({', '.join(DECORATORS)}): ")

    @DECORATORS[voice]
    def get_story():
        return """
            Alice was beginning to get very tired of sitting by her sister on the
            bank, and of having nothing to do: once or twice she had peeped into
            the book her sister was reading, but it had no pictures or
            conversations in it, "and what is the use of a book," thought Alice
            "without pictures or conversations?"
            """

    print(get_story())


if __name__ == "__main__":

    main()