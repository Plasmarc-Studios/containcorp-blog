import typing


class RoadmapEntry:
  def __init__(self, name: str, description: str, complete: bool = False, currentWorking: bool = False, beta: bool = False):
    self.name = name;
    self.description = description
    self.complete = complete
    self.currentWorking = currentWorking
    self.beta =beta


entries = [
    RoadmapEntry("Pre-Alpha", "The basic vision for the game and its systems, barebones and unfinished, but there.", True),
    RoadmapEntry("Early Access Release", "The game is ready for early access!", False, True),
    RoadmapEntry("Laying Foundations", "Fixing technical debt, bugs, tightening systems and game design, and adding basic mod support"),
    RoadmapEntry("Product Logistics", "Researching, Developing & creating products from anomalies, and various factory like elements"),
    RoadmapEntry("Category C Riots & Misconduct", "Introduces the potential for insubordination, riots, and misbehaviour among Interns working in the facility."),
    RoadmapEntry("Firefighting", "Introducing various methods to fight fires in case of emergencies."),
    RoadmapEntry("Ventilation and HVAC", "Complete the gas system with functioning ventilation, air quality, and temperature control mechanics."),
    RoadmapEntry("Waste Management", "Managing Facility Waste and keeping things clean"),
    RoadmapEntry("Anomalous Cuisine", "Customising facility cuisine and making meals from anomalies"),
    RoadmapEntry("General Containment Measures", "More general tools and structures to keep anomalies contained, and improved recontainment mechanics"),
    RoadmapEntry("Departments", "Introduce various specialized staff like HR managers or admin staff that grant perks or handle miscellaneous things, and the ability to organise staff into departments."),
    RoadmapEntry("Facility Directors", "Introduces a cast of facility directors to choose from, each with various perks and drawbacks"),
    RoadmapEntry("Mountains & Caves Expansion", "Enhance map generation with more interesting terrain features, and other generation features like aquifers."),
    RoadmapEntry("CCTV System", "Implement a fog-of-war system where CCTV is used to monitor restricted or hidden areas of the facility."),
    RoadmapEntry("Ancient Anomalies", "Discover strange anomalies deep within caves that pose unique challenges and opportunities."),
    RoadmapEntry("Biomes", "Diverse environmental that affect gameplay, resources, and the behavior of anomalies."),
    RoadmapEntry("World Planet", "A fully simulated planet and tying save files to the world map."),
    RoadmapEntry("Weather Expansion", "Dynamic weather systems, disasters and weather control systems"),
    RoadmapEntry("Field Exploration", "Send out teams to locate and capture dangerous anomalies found in the wilderness."),
    RoadmapEntry("Energy Expansion", "Introduce new energy sources like wind turbines and nuclear reactors to power your facility."),
    RoadmapEntry("Science Expansion", "Expand science operations with more research objects and advanced experimentation systems."),
    RoadmapEntry("Remote Sites", "Create self-sufficient bases in remote geographical areas of the World."),
    RoadmapEntry("NPC Apparel Expansion", "Add temperature-dependent clothing and numerous aesthetic wearable items for characters."),
    RoadmapEntry("Industry", "Produce industrial exports from the earth utilising anomalies in the process."),
    RoadmapEntry("Weapons Expansion", "Expands the arsenal available to security teams to deal with internal and external threats."),
    RoadmapEntry("Sieges and Raid Expansion", "mproves raid mechanics and siege events where hostile forces attack the facility."),
    RoadmapEntry("Deeper Health Modelling", "Body parts have functional roles, affecting character abilities and behavior when injured."),
    RoadmapEntry("Morgues & Disease", "ntroduce morgues and health hazards like infectious diseases that must be managed."),
    RoadmapEntry("Surgery & Infections", "Expand the medical system with detailed surgery and infection mechanics."),
    RoadmapEntry("Synths & Bionics", "Introduces synthetic NPCs and bionic body parts, enhancing or replacing human workers."),
    RoadmapEntry("Drugs & General Health", "Introduces a variety of psychoactive and medicinal drugs. Manage drug usage, addiction, and general health issues within the facility."),
    RoadmapEntry("Psychotherapy", "Assign therapists to help elevate Nugget mood and treat psychological conditions."),
    RoadmapEntry("Ethics & Inspections", "Deal with ethical dilemmas and facility inspections that impact reputation and morale."),
      RoadmapEntry("Faction Relations", "Manage relations with external factions, from alliances to hostilities."),
      RoadmapEntry("Animals & Husbandry", "Introduce animals with various functions, from pets to test subjects; and world-centric events like herd migrations."),
      RoadmapEntry("Cults & Belief", "Introduces secret cults and belief systems that can naturally form within your facility."),
      RoadmapEntry("Relationships", "Nuggets can form personal relationships, impacting teamwork and facility dynamics."),
      RoadmapEntry("Deep Characterization", "Enhance Nuggets with complex traits and personalities that influence their actions."),
      RoadmapEntry("Training Skills", "Allow Nuggets to improve their skills over time through dedicated training programs."),
      RoadmapEntry("Rooms & Recreation Expansion", "Add new room types and recreational activities to keep NPCs happy and productive."),
      RoadmapEntry("Game Ending", "Introduces a proper beat the game and provide players with an overarching goal"),
      RoadmapEntry("Regional Directors", "Introduces a cast of supervisors, providing secondary goals to beat in playthroughs"),
      RoadmapEntry("Quality of Life", "Amending any issues accumulated over alpha and adding any highly requested quality of life features.", beta=True),
      RoadmapEntry("Story Tracking Tools", "Tools for tracking events and finding interesting stories amongst the sea of chaos.", beta=True),
      RoadmapEntry("Mod Support QOL Improvements", "Any miscellaneous quality of life improvements required for mod support", beta=True),
      RoadmapEntry("End of the World Scenarios", "Introduce catastrophic events that challenge the facility's survival, pushing players to their limits, and adding an alternative game end goal.", beta=True),
      RoadmapEntry("Professional Localisation", "Finialise community localisations with professional work, and target all supported languages", beta=True),
      RoadmapEntry("1.0 Release", "The game has reached the ultimate vision.", beta=True),
  ]


templateS = """---
layout: default
---

<section class="roadmap-nav-bar">
  <div class="flex-row-between">
      <a href="{{ site.url }}{{ site.baseurl }}/">« Home</a>
    <button title="Change theme" id="theme-toggle" onclick="modeSwitcher()">
      <div></div>
    </button>
  </div>
</section>
<style>
    body{
        background: linear-gradient(to top,#63573a 0%, #65a4b6 50%, #110b0b 75%, #00080a 100%) !important;
    }
</style>
<section>
    <h1 style="margin: auto; inset: 0; padding-bottom: 30px;">Development Roadmap</h1>
    <!-- The Timeline -->
    <div class="star"></div>
    <div class="timeline">
"""

templateE = """
    </div>
    
    

<!-- adding an empty line to separate the social profile links -->
  <br></br>
  <br></br>
  <br></br>
</section>



<section>
  <nav class="post-nav"></nav>
</section>

"""
res = ""
entries.reverse()
idx = 0
betaCount = 0
totalBetaCount = 0

for item in entries:
  if item.beta:
    totalBetaCount += 1

for item in entries:
  rl = "right" if idx % 2 == 0 else "left"
  imp = "implemented" if item.complete else ""
  lab = "Implemented" if item.complete else "Upcoming"
  stage = f'Alpha {len(entries)-1-idx}: ' if not item.beta else f'Beta {totalBetaCount-betaCount}: '
  curr = "current" if item.currentWorking else ""
  lab = "We're working on this!" if item.currentWorking else lab

  if (idx == 0):
    stage = ""
  res += """
    \n<div class="container {0} {1}" id="{2}">
            <div class="content">
                <h2 class="title">{3}{4}</h2>
            </div>
            <p class="date">{5}</p>
            <p class="desc">{6}</p>
        </div>
  """.format(rl,imp, curr, stage, item.name, lab, item.description)
  idx += 1
  if item.beta:
    betaCount+=1

final = templateS + res + templateE

file='./docs/roadmap.html' 
with open(file, 'w', encoding="utf8") as filetowrite:
    filetowrite.write(final)