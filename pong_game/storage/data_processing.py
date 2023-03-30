class DataProcessing:

    # WINS -------------------------------------------------------------------------------------------------------------
    @staticmethod
    def save_data(data, filename):
        file = open(filename, "a")
        file.write(data + "\n")
        file.close()

    @staticmethod
    def load_data(filename):
        with open(filename, "r") as file:
            win_list = [x.rstrip() for x in file]

        return win_list
