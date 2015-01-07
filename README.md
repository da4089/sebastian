# - Maintain asset list
# - Depreciation schedule
# - Rack elevations
# - Floor plans
# - Patch schedule
# - Network diagram
# - SDN provisioning
# - OpenStack/AWS provisioning
# - Configuration verification
# - Discovery.  Active vs. passive, etc.


#  - server
#  - NIC (LOM)
#  - HDD
#  - PCIe card
#  - PSU

# Do I need to model a rack server as a derivative, which size in RU?
# And maybe a "rack-mountable" flag?


Next steps
==========

- Get web-app running.
- Define some menu/page structure.
- Create form(s):
  - CRUD.
- Add existing stuff:
  - racks
  - patch panels
  - cable management
  - servers
  - switches
  - shelf
  - PDU
  - UPS
  - cabling for all the above
    - twisted pair
    - coax
    - power
- Design the floor-layout data model.
  - Consider implications on rack layout model.
- Add printing support:
  - Using Python-PDF stuff?
  - Equipment labels.
  - Cable labels.
  - Rack elevations.
  - Floor plans.
- Add CSV export:
  - Asset lists.
  - Depreciation schedule.
  - Patch schedules.



Design Notes
============

Locations
---------
- Maps show geography, and the location of facilities.
  - Can we use Google Maps API?
  - How do we get a more logical view?
- Floorplans show interior geography, and the location of equipment.
- Racks are shown on floorplans, and show equipment in their
  elevations.
- Devices can have sub-components.  It'd be nice to actually have a
  sockets and plugs model to explicitly identify the expansion points
  in a device (CPU sockets, memory sockets, expansion sockets,
  external ports).


Menu Structure
--------------

  Frontpage
  - Search (equipment type, serial #, MAC, IP, location, owner, etc)
    - Basically a full-text search across the database, with results
      like Apple's Spotlight that divides answers into categories?
  - Some basic statistics?
  - Recent activities list?

  New
  - Map
  - Floorplan
  - Rack
  - Device
  - Component
  - Cable

  View
  - Locations
  - Devices (types, etc)
  - Maps
  - Elevations (?)

  Export
  - Asset list
  - Depreciation
  - Patch schedule
  - Backup

