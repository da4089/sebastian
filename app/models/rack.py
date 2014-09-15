#

__all__ = ['Rack',
           'RackShelf',
           'BlankingPlate',
           'HorizontalCableManagement']

from element import Element


class Rack(Element):
    def __init__(self):
        super(Element, self).__init__()

        # Height in rack units.
        self.height = 0

        # FIXME: width, 19" vs. other weird-ass telco shit.
        # FIXME: threaded vs. square-hole

        # FIXME: two-post front, two-post middle, two-post rear,
        # four-post, cabinet?

        # FIXME: lockable? (and do we need to store codes, or key id,
        # or whatever?)

        # FIXME: panels (sides, doors)?  Important for weight?

        # FIXME: extraction fans, etc?

        # FIXME: weird-ass combo things with built-in AC, UPS,
        # whatever?
        return


class RackShelf(Element):
    def __init__(self):
        super(Element, self).__init__()

        # Height in rack units
        self.height = 0

        # Fixed or sliding.
        self.fixed = True

        # Depth in millimeters.
        self.depth = 0
        return


class BlankingPlate(Element):
    def __init__(self):
        super(Element, self).__init__()

        # Height in rack units.
        self.height = 0

        # Perforated?
        self.perforated = False
        return

class HorizontalCableManagement(Element):
    def __init__(self):
        super(Element, self).__init__()

        # Height in rack units.
        self.height = 0

        # Depth in millimeters.
        #
        # Distance from front face of vertical rack rails, to furthest
        # forward extent of the rings/shelf/whatever.  ie. Will the
        # damned door close?
        self.depth = None
