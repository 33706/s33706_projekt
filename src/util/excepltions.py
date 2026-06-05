class SlotEmptyException(Exception):
    def __init__(self, message="The slot is empty!"):
        self.message = message
        super().__init__(self.message)