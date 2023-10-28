class InvalidInputException(Exception):
    def __init__(self, input_provided: str, input_expected: str):
        super().__init__(
            f"InvalidInput Provided: provided {input_provided}, but expected {input_expected}"
        )
