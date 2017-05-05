from operation import Operation


class Divide(Operation):
    def handle_request(self, text):
        chars = text.split()

        if chars[1] == '/':
            print(int(chars[0]) / int(chars[2]))
            return int(chars[0]) / int(chars[2])
        elif self._successor is not None:
            return self._successor.handle_request(text)
        else:
            print("Not supported operation")
            return None
