#

from enum import Enum
from element import Element


class ExpansionCard(Element):
    """Could be PCIe or proprietary format."""

    class Connector(Enum):
        """Physical connector for card to motherboard or chassis."""

        ISA,
        EISA,
        VLB,
        PCI,
        PCI_X,
        PCIe_x1,
        PCIe_x4,
        PCIe_x8,
        PCIe_x16,
        HTX,

    class Speed(Enum):
        """Main bus connection speed, if applicable."""

        PCI_33,
        PCI_66,
        PCI_X_100,
        PCI_X_133,

        PCIe_1,
        PCIe_2,
        PCIe_3,

        
    def __init__(self):
        """Constructor."""
        Element.__init__(self)

        # Connector.
        self.connector = None

        # Speed.
        self.speed = None

        # Fractional Length (half, third, etc).
        self.length = 1.0

        # Fractional Height (half, etc).
        self.height = 1.0

        # Slot width (single, double, etc).
        self.width = 1
        return


