class InvalidValueType(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class TooFewOperands(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class VarNotDefined(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class LabelNotDefined(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class InvalidExpression(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs) 