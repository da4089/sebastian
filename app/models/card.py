#

from enum import Enum
from element import Element


class ExpansionCard(Element):
    """Could be PCIe or proprietary format."""

    class Connector(Enum):
        """Physical connector for card to motherboard or chassis."""

        ISA = 1,
        EISA = 2,
        VLB = 3,
        PCI = 4,
        PCI_X = 5,
        PCIe_x1 = 6,
        PCIe_x4 = 7,
        PCIe_x8 = 8,
        PCIe_x16 = 9,
        HTX = 10,

    class Speed(Enum):
        """Main bus connection speed, if applicable."""

        PCI_33 = 1,
        PCI_66 = 2,
        PCI_X_100 = 3,
        PCI_X_133 = 4,

        PCIe_1 = 5,
        PCIe_2 = 6,
        PCIe_3 = 7,

        
    def __init__(self):
        """Constructor."""
        super(ExpansionCard, self).__init__()

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


