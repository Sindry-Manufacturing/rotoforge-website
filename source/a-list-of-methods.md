# A List of Methods Being Considered

## Under Investigation

## Friction based approaches
### [Additive friction stir deposition (AFSD)](https://discord.com/channels/1028060441273958510/1028767820181422090/1126363310363787335)

![Animated schematic of additive friction stir deposition: a rotating shoulder stirs fed rod or wire into a wide layer](img/methods/afsd.gif)

Tested, forces too high, handling small wires in segments and discontinuous feeding is very difficult at small scale. 
### Additive friction extrusion deposition (AFED)

![Animated schematic of additive friction extrusion deposition: a rotating chamber friction-heats feedstock and extrudes it through a small die](img/methods/afed.gif)

Same as in AFSD, but with the added challenge of very fast die wear for small dies (0.4 mm ID). More details from various attempts can be found in these [discord threads](https://discord.com/channels/1028060441273958510/1334721242703331369)
### Additive friction roll bonding

![Animated schematic of additive friction roll bonding: a spinning wheel drags preheated wire under its rim and rolls it onto the layer below](img/methods/afrb.gif)

Info can be found in [this discord thread](https://discord.com/channels/1028060441273958510/1254838510683426998)
This is our latest working approach. It works very well, and economically, at low force, and with relatively long tool wear lives. 

## Lasers
### Laser Directed Energy Deposition (DED)

![Animated schematic of laser wire DED: a laser melts a pool and wire is fed into it](img/methods/laser-wire-ded.gif)

More infor can be found on [Junker's Discord thread](https://discord.com/channels/1028060441273958510/1304109853299572756), Junkers AKA [Metal Matters](https://www.youtube.com/@metalmatters) on youtube, has been a big supporter in the project and has done thorough and high quality work downcosting LPBF and Wire DED for the home shop! 
## Kinetic Energy
Tested, getting high enough particle velocities in a small head with anarrow nozzle is very difficult with practically sized systems and commodity gas pressures. Moreover, the gaussian profile of the deposits complicates layer building. 
### Cold Spray 

![Animated schematic of cold spray: supersonic gas fires solid particles that flatten on impact](img/methods/cold-spray.gif)

### Flame Spray/Detonation Spray

![Animated schematic of flame spray: inkjet droplets ride a flame jet and splat onto the part](img/methods/flame-spray.gif)

Sam and I tested this pretty extensively with the [Open Pyrojet Project](https://openpyrojet.com/). 
It has a great deal of chemical and toxicological complexity and all of the expenses and complexities of thermal inkjet printing as well as the complexities and dnagers of flame and detonation spray.  It barely works with silver, and gold particles and tends to make deposits that are rich in organics or otherwise heavily oxidized. It may be extensible for some applications. Happy to discuss on request. 

## Acoustic energy
### Ultrasonic Additive Manufacturing

![Animated schematic of ultrasonic additive manufacturing: a vibrating roller scrubs foil onto the stack](img/methods/ultrasonic-am.gif)

[Junkers Does it again](https://discord.com/channels/1028060441273958510/1200003094369542144) testing ultrasonic welding of aluminum.
### Thermosonic Additive Manufacturing

![Animated schematic of thermosonic additive manufacturing: ultrasonic scrubbing plus a heated stage and tool](img/methods/thermosonic-am.gif)

##electric and chemical potential
### Electrochemical Additive Manufacturing

![Animated schematic of electrochemical additive manufacturing: metal ions plate onto the part through an electrolyte meniscus](img/methods/electrochemical-am.gif)

## Laser Induced Electrochemical Deposition 

![Animated schematic of laser-induced electrochemical deposition: a laser heats one spot in a plating bath](img/methods/laser-induced-ecd.gif)

Info can be found in [this thread](https://discord.com/channels/1028060441273958510/1429239317909475419) by That One Guy on laser metal deposition that seems to work pretty well. 

### Heat and Impact
## Heated Micro Powerhammer forging

![Animated schematic of heated micro power-hammer forging: a heated hammer forges the wire flat strike by strike](img/methods/micro-powerhammer.gif)

[tested](https://www.youtube.com/watch?v=xnsqmpapSvk). Steel nozzles used as hammers dull quickly, forces and vibration amplitudes a bit too high for easy control. Might still be possible though. One imagines a kind of sewing machine for metal.
## Electric arcs and plasma heating, resistance heating, induction heating

![Animated schematic of micro arc/plasma deposition: an arc melts the wire and a pool on the part](img/methods/micro-arc-plasma.gif)

tried all of these. They all have their own pros and cons. 
Kor on the discord has been heading up the [micro arc plasma](https://discord.com/channels/1028060441273958510/1301966385945120828) work
## joule printing

![Animated schematic of joule printing: current through the wire-substrate contact heats it while the head presses the wire down](img/methods/joule-printing.gif)

Requires conductive substrates and works poorly with high electrical/thermal conductive materials. Currently requires high current power suppliers and other costly features. [Dominik Meffert](https://hackaday.io/project/169412-wire-3d-printer) has already done an excellent job of this on Hackaday. 
### Micro welding

![Animated schematic of micro welding: a pulsed micro-welder tacks the wire down dot by dot](img/methods/micro-welding.gif)

Info can be found in [this discord thread](https://discord.com/channels/1028060441273958510/1232359803163119667)

## Thermal Energy
### Glowplug (Semisolid metal direct writing)

![Animated schematic of glow-plug semisolid direct write: a glow plug heats wire to a semisolid that is extruded through a nozzle](img/methods/glowplug-semisolid.gif)

You can find [more info here](https://dailyrotoforge.blogspot.com/)

### Semisolid Metal Direct Write with Induction heating

![Animated schematic of induction-heated semisolid direct write: an RF coil heats the barrel and feedstock](img/methods/induction-semisolid.gif)

[Dival Banerjee](https://www.linkedin.com/in/dival-b-3571b5117/) is doing a great job of exploring this with [Vuecason](https://www.vuecason.com/). There are also many efforts published in literature of induction heating approaches. They seem to work but typically require high frequency induction power suppliers, and struggle with many of the chemical and rheological challenges of the glowplug approach. 

### Semisolid Metal Direct Write the FDM way

![Animated schematic of an FDM-style hotend melting low-temperature solder wire](img/methods/fdm-semisolid.gif)

Michael Perrone did a great piece of work on this [modified FDM hotend approach](https://hackaday.io/project/179846-semisolid-metal-printing) on hacakday. Good for printing various solder alloys, especially Sn-Zn and anything that melts under ~500 C. 

Bad Obsession motorsports also did a great job of showcasing [a milling machine and semisolid metal drect write approach with a standard FDM hotend](https://www.youtube.com/watch?v=FzrZoVKT8gM). 
## Rejected

## To Be Evaluated

## Combined Approaches of conduction heating, and various forms of mechanical deformation
### Hot Tool Orbital Friction Stiring 

![Animated schematic of hot-tool orbital friction stirring: a heated foot orbits in a small circle and stirs the wire into the layer below](img/methods/hot-tool-orbital.gif)

Avery is trying this out to some very cool results! 
### Hot Tool Rotary Vibro Welding

![Animated schematic of hot-tool rotary vibro welding: a heated tool twists back and forth at high frequency](img/methods/hot-tool-rotary-vibro.gif)

### Hot Tool Linear Vibro Welding

![Animated schematic of hot-tool linear vibro welding: a heated tool shuttles along the travel direction at high frequency](img/methods/hot-tool-linear-vibro.gif)
