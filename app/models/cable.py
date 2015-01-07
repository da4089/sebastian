#

from element import Element


class Cable(Element):
    def __init__(self):
        super(Cable, self).__init__()

        # Connectors.
        self.connectors = {}

        # Plenum-rated.
        self.plenum = False

        # Colour.
        self.colour = None

        # Length in meters.
        self.length = 0.0
        return


class TwistedPairCable(Cable):
    def __init__(self):
        super(TwistedPairCable, self).__init__()

        # Category rating.
        self.category = "5"

        # Solid or stranded.
        self.solid = False
        return


class TwinaxCable(Cable):
    def __init__(self):
        super(TwinaxCable, self).__init__()

        # Active or passive.
        self.active = False

        # Gauge.
        self.gauge = None
        return


class PowerCable(Cable):
    def __init__(self):
        super(PowerCable, self).__init__()

        # Number of wires in cable.
        self.wire_count = 3

        # Max current rating in amps.
        self.current = 10.0

        # Max voltage rating in volts.
        self.volts = 250
        return
