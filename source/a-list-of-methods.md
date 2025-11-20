# A List of Methods Being Considered

## Under Investigation

## Friction based approaches
### [Additive friction stir deposition (AFSD)](https://discord.com/channels/1028060441273958510/1028767820181422090/1126363310363787335)
Tested, forces too high, handling small wires in segments and discontinuous feeding is very difficult at small scale. 
### Additive friction extrusion deposition (AFED)
Same as in AFSD, but with the added challenge of very fast die wear for small dies (0.4 mm ID). More details from various attempts can be found in these [discord threads](https://discord.com/channels/1028060441273958510/1334721242703331369)
### Additive friction roll bonding
Info can be found in [this discord thread](https://discord.com/channels/1028060441273958510/1254838510683426998)
This is our latest working approach. It works very well, and economically, at low force, and with relatively long tool wear lives. 

## Lasers
### Laser Directed Energy Deposition (DED)
More infor can be found on [Junker's Discord thread](https://discord.com/channels/1028060441273958510/1304109853299572756), Junkers AKA [Metal Matters](https://www.youtube.com/@metalmatters) on youtube, has been a big supporter in the project and has done thorough and high quality work downcosting LPBF and Wire DED for the home shop! 
## Kinetic Energy
Tested, getting high enough particle velocities in a small head with anarrow nozzle is very difficult with practically sized systems and commodity gas pressures. Moreover, the gaussian profile of the deposits complicates layer building. 
### Cold Spray 

### Flame Spray/Detonation Spray
Sam and I tested this pretty extensively with the [Open Pyrojet Project](https://openpyrojet.com/). 
It has a great deal of chemical and toxicological complexity and all of the expenses and complexities of thermal inkjet printing as well as the complexities and dnagers of flame and detonation spray.  It barely works with silver, and gold particles and tends to make deposits that are rich in organics or otherwise heavily oxidized. It may be extensible for some applications. Happy to discuss on request. 

## Acoustic energy
### Ultrasonic Additive Manufacturing
[Junkers Does it again](https://discord.com/channels/1028060441273958510/1200003094369542144) testing ultrasonic welding of aluminum.
### Thermosonic Additive Manufacturing

##electric and chemical potential
### Electrochemical Additive Manufacturing
## Laser Induced Electrochemical Deposition 
Info can be found in [this thread](https://discord.com/channels/1028060441273958510/1429239317909475419) by That One Guy on laser metal deposition that seems to work pretty well. 

### Heat and Impact
## Heated Micro Powerhammer forging
[tested](https://www.youtube.com/watch?v=xnsqmpapSvk). Steel nozzles used as hammers dull quickly, forces and vibration amplitudes a bit too high for easy control. Might still be possible though. One imagines a kind of sewing machine for metal.
## Electric arcs and plasma heating, resistance heating, induction heating
tried all of these. They all have their own pros and cons. 
Kor on the discord has been heading up the [micro arc plasma](https://discord.com/channels/1028060441273958510/1301966385945120828) work
## joule printing
Requires conductive substrates and works poorly with high electrical/thermal conductive materials. Currently requires high current power suppliers and other costly features. [Dominik Meffert](https://hackaday.io/project/169412-wire-3d-printer) has already done an excellent job of this on Hackaday. 
### Micro welding
Info can be found in [this discord thread](https://discord.com/channels/1028060441273958510/1232359803163119667)

## Thermal Energy
### Glowplug (Semisolid metal direct writing)
You can find [more info here](https://dailyrotoforge.blogspot.com/)

### Semisolid Metal Direct Write with Induction heating
[Dival Banerjee](https://www.linkedin.com/in/dival-b-3571b5117/) is doing a great job of exploring this with [Vuecason](https://www.vuecason.com/). There are also many efforts published in literature of induction heating approaches. They seem to work but typically require high frequency induction power suppliers, and struggle with many of the chemical and rheological challenges of the glowplug approach. 

### Semisolid Metal Direct Write the FDM way
Michael Perrone did a great piece of work on this [modified FDM hotend approach](https://hackaday.io/project/179846-semisolid-metal-printing) on hacakday. Good for printing various solder alloys, especially Sn-Zn and anything that melts under ~500 C. 

Bad Obsession motorsports also did a great job of showcasing [a milling machine and semisolid metal drect write approach with a standard FDM hotend](https://www.youtube.com/watch?v=FzrZoVKT8gM). 
## Rejected

## To Be Evaluated

## Combined Approaches of conduction heating, and various forms of mechanical deformation
### Hot Tool Orbital Friction Stiring 
Avery is trying this out to some very cool results! 
### Hot Tool Rotary Vibro Welding
### Hot Tool Linear Vibro Welding