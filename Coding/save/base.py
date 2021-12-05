#!/usr/bin/env python
import rebound
sim = rebound.Simulation()
sim.units = ('AU', 'yr', 'Msun')
dateStr = "2021-11-08 00:00"
# Add the celestial bodies
sim.add("Sun", date=dateStr)
sim.add("Venus", date=dateStr)
sim.add("Earth", date=dateStr)
sim.add("Mars", date=dateStr)
sim.add("Jupiter", date=dateStr)
sim.add("Saturn", date=dateStr)
sim.add("Uranus", date=dateStr)
sim.add("Neptune", date=dateStr)
# Save to .bin file
sim.save("../data/simulation_base.bin")