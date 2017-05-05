from add import Add
from subtract import Subtract
from multiple import Multiple
from divide import Divide

operation1 = Add()
operation2 = Subtract(operation1)
operation3 = Divide(operation2)
operation4 = Multiple(operation3)

operation4.handle_request("2 - 3")
