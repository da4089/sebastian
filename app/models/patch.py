#

from element import Element


class PatchJack(Element):
    def __init__(self):
        super(PatchJack, self).__init__()

        # External connector type.
        self.external_connector = 0

        # Internal connector type.
        self.internal_connector = 0
        return

        
class PatchPanel(Element):
    def __init__(self):
        super(PatchPanel, self).__init__()

        # Number of jacks.
        self.count = 0

        # Jack collection.
        self.jacks = []
        return


class RackPatchPanel(PatchPanel):
    def __init__(self):
        super(RackPatchPanel, self).__init__()

        # Size in rack units.
        self.size = 1

        # Rack mountable flag.
        self.rack_mount = True
        return


class WallJackPanel(PatchPanel):
    def __init__(self):
        super(WallJackPanel, self).__init__()
        return
