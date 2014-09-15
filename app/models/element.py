#

class Element(object):

    def __init__(self):
        # Primary key.
        self.id = 0

        # Owner's name for this instance of an element, eg. hostname.
        self.name = ""

        # Owner's asset identifier for this element.
        self.asset_id = ""
        
        # Manufacturer's serial number for this element.
        self.serial = ""

        # Manufacturer's name for this model of device.
        self.model = ""

        # If true, this element is built-in to its container.
        self.built_in = False

        # Source of this element.
        self.vendor = ""

        # Purchase price for this element, if separately purchased.
        self.price = 0.0

        # Purchase currency for this element.
        self.currency = ""

        # Date of purchase.
        self.purchase_date = 0

        # Depreciation lifetime (months).
        self.lifetime = 0

        # Power consumption, at full load, in watts.
        self.power = 0

        # Heat production, at full load, in watts.
        self.heat = 0

        # Weight, in kilograms.
        self.weight = 0

        # Owning group, department, person.
        self.owner = ""

        # Owner's contact details.
        self.contact = ""

        # Collection of sub-component instances physically contained
        # within in this element.
        self.sub_components = []

        return
