# Introduction to the project
![Rotoforge up close](https://github.com/Sindry-Manufacturing/rotoforge/raw/4d83dadd1b250bc74a4e3fa7a5a5383b4bb77142/docs/img/Screenshot%202025-11-15%20133716.png)

[discord server](https://discord.gg/tprMSEd4wA)

[youtube channel](https://www.youtube.com/@rotoforge2024)

[blog](https://dailyrotoforge.blogspot.com/)

[Rotoforge github](https://github.com/Sindry-Manufacturing/rotoforge). 

## What is Rotoforge?
Rotoforge is a [free and open source](https://en.wikipedia.org/wiki/Free_and_open-source_software) [hardware](https://en.wikipedia.org/wiki/Open-source_hardware)/software 3d printer for printing metal, plastic and ceramic heterogenously on the home desktop safely and affordably with performance similar to FDM. It uses friction welding to locally heat, form and bond metal/plastic/ceramic wire/rod/sheet/powder into 3D objects.

## Where we are right now
![Al 1100 Test Print](https://github.com/Sindry-Manufacturing/rotoforge/blob/main/docs/img/firstcleanal1100deposit.jpg?raw=true)

We are repeatably printing aluminum [1100](https://en.wikipedia.org/wiki/1100_aluminium_alloy), and [5054](https://en.wikipedia.org/wiki/Aluminium%E2%80%93magnesium_alloys), bars, walls, and tensile / flexural test specimens from 0.5mm OD wire using the [latest version of the hardware](https://github.com/Sindry-Manufacturing/rotoforge/blob/a09c34a0b46779132ed0c06f043717a615cee749/src/parts/CAD) and a [basic python g-code generator](https://github.com/Sindry-Manufacturing/rotoforge/blob/a09c34a0b46779132ed0c06f043717a615cee749/src/afrb_playground_gui(2).py).  We are implementing temperature, torque and force monitoring to better characterize the process and help us design smaller, cheaper, faster, and more accurate printers based on the process. 

## Where we want to be
The [total BOM cost](https://github.com/Sindry-Manufacturing/rotoforge/blob/a09c34a0b46779132ed0c06f043717a615cee749/docs/billsofmaterials/Rotoforge%20BOM%2011152025%20-%20Amazon%20BOM-2.pdf) at time of writing, including the ender 3 and all custom parts is ~$791.43. This leaves room for another 3-5X reduction with group buys, better sourcing, and design for manufacturing. less than $500 is the target BOM. 

In the next 3-6 months we want to be reliably printing strong aluminum objects with complexity approaching a benchy with line widths of less than 2.5 mm. Currently Avery(on the discord) is designing and building a 4th axis to allow smooth curves. 

Besides downcosting, building a community of developers, building a large printable material library(all aluminums, copper and copper alloys, steels, ceramics, cermets), expanding the range of achievable material properties as printed, developing a complete closed loop control system, digital twinning, are all high on the list. 


## Licensing information (operating principles)
The project is currently licensed under the terms of the [AGPL-3.0](https://github.com/Sindry-Manufacturing/rotoforge/blob/a09c34a0b46779132ed0c06f043717a615cee749/LICENSE) and the [CERN open hardware license](https://github.com/Sindry-Manufacturing/rotoforge/blob/a09c34a0b46779132ed0c06f043717a615cee749/cern_ohl_s_v2.txt).

## Why do this? 
1. Because manufacturing freedom for the individual *is* individual creative freedom
2. Plastic trinkets only get you so far
3. A truly self replicating machine and its proported benefits must be able to produce itself *entirely* from raw materials and energy, wherever it might happen to be. Probably, in places that do not include convenient metal foundry and electronics fabrication infrastructure. 
4. Insert your reason here. ;)

## Where and how to get involved
We have a [discord server](https://discord.gg/tprMSEd4wA) where we discuss our latest efforts and share and discuss other projects from the wider community and a [youtube channel](https://www.youtube.com/@rotoforge2024) where we post experimental logs, build guides, and project videos for Rotoforge, as well as a [blog](https://dailyrotoforge.blogspot.com/) where we write longer technical updates periodically. The latest project files, BOM, code and CAD designs/drawings are found on the [Rotoforge github](https://github.com/Sindry-Manufacturing/rotoforge). 

Join the discord, introduce yourself in introductions, and help us out by watching our content, sharing it, donating time/money if you can/want and if you are feeling up to the task, building your own Rotoforge!