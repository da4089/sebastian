#


from element import Element


class CPU(Element):
    def __init__(self):
        super(Element, self).__init__()

        # Default speed in MHz
        self.speed = 0

        # Maximum speed in MHz
        self.turbo = 0

        # Core count
        self.core_count = 0

        # Thread count
        self.thread_count = 0

        return


