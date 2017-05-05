from operation import Operation


class Add(Operation):
    def handle_request(self, text):
        chars = text.split()

        if chars[1] == '+':
            print(int(chars[0]) + int(chars[2]))
            return int(chars[0]) + int(chars[2])
        elif self._successor is not None:
            return self._successor.handle_request(text)
