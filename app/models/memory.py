#
#
#

from enum import Enum
from element import Element


class Memory(Element):

    class Type(Enum):
        # Basic type.
        FP = 1,
        EDO = 2,
        SDRAM = 3,
        DDR = 4,
        DDR2 = 5,
        DDR3 = 6,
        DDR4 = 7,
        DDR5 = 8,


    class Speed(Enum):
        # Fast page DRAM (multiply by 10 to get access time in
        # nanoseconds).
        FP_12,
        FP_15,
        FP_20,

        # SDRAM.
        PC_66,
        PC_100,
        PC_133,

        # DDR-SDRAM.
        DDR_200, # aka PC1600
        DDR_266, # aka PC2100
        DDR_300, # aka PC2400,
        DDR_333, # aka PC2700,
        DDR_400, # aka PC3200,

        # DDR2-SDRAM.
        DDR2_400, # aka PC2_3200
        DDR2_533, # aka PC2_4200
        DDR2_667, # aka PC2_5300
        DDR2_800, # aka PC2_6400
        DDR2_1066, # aka PC2_8500

        # DDR3-SDRAM.
        DDR3_800, # aka PC3_6400
        DDR3_1066, # aka PC3_8500
        DDR3_1333, # aka PC3_10600
        DDR3_1600, # aka PC3_12800
        
    
    class FormFactor(Enum):
        # Packaging
        DIP16 = 1,
        SIPP30 = 2,
        SIMM30 = 3,
        SIMM72 = 4,
        DIMM168 = 5,
        DIMM184 = 6,
        DIMM240 = 7,
        DIMM288 = 8,
        SODIMM204 = 9,
        SODIMM260 = 10,


    class Buffering(Enum):
        # Normal (cheap) RAM (UDIMM).
        UNBUFFERED = 0,

        # Registered (RDIMM).
        REGISTERED = 1,

        # Fully-buffered (FB-DIMM).
        FULLY_BUFFERED = 2,

        # Load-reduced (LRDIMM).
        LOAD_REDUCED = 3,


    def __init__(self):
        super(Element, self).__init__()

        # Capacity of this memory element, in bytes
        self.capacity = 0

        # Type of memory.
        self.type = None

        # Speed of memory, in MHz
        self.speed = None

        # Form-factor for this memory (eg. DDR3, etc)
        self.form_factor = ""

        # Error correction.
        self.ecc = False

        # Buffering.
        self.buffering = Buffering.UNBUFFERED
        return


