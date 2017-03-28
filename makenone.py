class makenone:
    def __init__(self, *args):
        for each in args:
            print(str(each) + " is None.")
        raise Exception("All your arguments is None.")
