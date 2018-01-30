class addObj():
    def __init__(self, header, content):
        self.__header = header
        self.__content = content

    def get_header(self):
        return self.__header

    def get_content(self):
        return self.__content

    def set_header(self, header):
        self.__header = header

    def set_content(self, content):
        self.__content = content