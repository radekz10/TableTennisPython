class DataProcessing:

    # WINS -------------------------------------------------------------------------------------------------------------
    @staticmethod
    def save_wins(data, filename):
        file = open(filename, "a")
        file.write(data + "\n")
        file.close()

    @staticmethod
    def load_wins(filename):
        with open(filename, "r") as file:
            win_list = [x.rstrip() for x in file]

        return win_list
