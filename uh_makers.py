from graph_tool.all import *
import numpy as np
import cairo


def new_vertex(g, properties):
    v = g.add_vertex()
    for pair in properties:
        property, value = pair
        property[v] = value

    return v


g = Graph(directed=True)
name = g.new_vertex_property("string")
action = g.new_edge_property("string")

color = g.new_vertex_property("vector<double>")
size = g.new_vertex_property("int")

people_color = [color, np.array([0, 98, 155, 255], dtype=np.float32) / 255]
dept_color = [color, np.array([200, 16, 46, 255], dtype=np.float32) / 255]
workshop_color = [color, np.array([0.7 * 255, 0.7 * 103, 0, 255], dtype=np.float32) / 255]
event_color = [color, np.array([0, 134, 108, 255], dtype=np.float32) / 255]
project_color = [color, np.array([255, 103, 0, 255], dtype=np.float32) / 255]
studentorg_color = [color, np.array([100, 8, 23, 255], dtype=np.float32) / 255]
community_color = [color, np.array([152, 41, 160, 255], dtype=np.float32) / 255]

company_color = [color, np.array([216, 155, 0, 255], dtype=np.float32) / 255]

v_codirectors = new_vertex(g, [[name, "Co-Directors"], people_color])

v_event_coordinator = new_vertex(g, [[name, "Officer: Events"], people_color])
v_workshop_coordinator = new_vertex(g, [[name, "Officer: Workshops"], people_color])
v_documentation_officer = new_vertex(g, [[name, "Officer: Documentation"], people_color])
v_resource_chair = new_vertex(g, [[name, "Officer: Resources"], people_color])
v_technology_officer = new_vertex(g, [[name, "Officer: Technology"], people_color])
v_outreach_officer = new_vertex(g, [[name, "Officer: Outreach"], people_color])

v_lead_1 = new_vertex(g, [[name, "P1 Lead"], people_color])
v_lead_2 = new_vertex(g, [[name, "P2 Lead"], people_color])
v_lead_3 = new_vertex(g, [[name, "P3 Lead"], people_color])
v_lead_4 = new_vertex(g, [[name, "P4 Lead"], people_color])

v_project_1 = new_vertex(g, [[name, "Project 1"], project_color])
v_project_2 = new_vertex(g, [[name, "Project 2"], project_color])
v_project_3 = new_vertex(g, [[name, "Project 3"], project_color])
v_project_4 = new_vertex(g, [[name, "Project 4"], project_color])

v_company = new_vertex(g, [[name, "Sponsors"], company_color])

v_ece = new_vertex(g, [[name, "ECE"], dept_color])
v_cs = new_vertex(g, [[name, "CS @ UH"], dept_color])
v_tech = new_vertex(g, [[name, "CoT"], dept_color])

v_swe = new_vertex(g, [[name, "SWE"], studentorg_color])
v_asme = new_vertex(g, [[name, "ASME"], studentorg_color])
v_ieee_engi = new_vertex(g, [[name, "IEEE Engineering"], studentorg_color])
v_ieee_nsm = new_vertex(g, [[name, "IEEE NSM"], studentorg_color])
v_ieee_tech = new_vertex(g, [[name, "IEEE Tech"], studentorg_color])
v_ece_students = new_vertex(g, [[name, "ECE Students"], studentorg_color])
v_ieee_pvamu = new_vertex(g, [[name, "IEEE PV A&M"], studentorg_color])
v_ieee_uhcl = new_vertex(g, [[name, "IEEE UHCL"], studentorg_color])

v_middle_schools = new_vertex(g, [[name, "Middle Schools"], community_color])
v_high_schools = new_vertex(g, [[name, "High Schools"], community_color])
v_community = new_vertex(g, [[name, "Community"], community_color])


v_pi_workshop = new_vertex(g, [[name, "Pi Workshop"], workshop_color])
v_jetbot_workshop = new_vertex(g, [[name, "Jetbot Workshop"], workshop_color])
v_ml_workshop = new_vertex(g, [[name, "ML Workshop"], workshop_color])
v_ros_workshop = new_vertex(g, [[name, "ROS Workshop"], workshop_color])
v_arduino_workshop = new_vertex(g, [[name, "Arduino Workshop"], workshop_color])

v_pi_workshop_lead = new_vertex(g, [[name, "Pi Lead"], people_color])
v_jetbot_workshop_lead = new_vertex(g, [[name, "Jetbot Lead"], people_color])
v_ml_workshop_lead = new_vertex(g, [[name, "ML Lead"], people_color])
v_ros_workshop_lead = new_vertex(g, [[name, "ROS Lead"], people_color])
v_arduino_workshop_lead = new_vertex(g, [[name, "Arduino Lead"], people_color])

v_buildabot_event = new_vertex(g, [[name, "Build-a-Bot"], event_color])
v_makersshowcase_event = new_vertex(g, [[name, "Makers Showcase"], event_color])
v_makersarcade_event = new_vertex(g, [[name, "Makers Arcade"], event_color])
v_ecedha_event = new_vertex(g, [[name, "ECEDHA"], event_color])
v_chilicookoff_event = new_vertex(g, [[name, "Chili Cookoff"], event_color])

g.add_edge(v_pi_workshop_lead, v_pi_workshop)
g.add_edge(v_jetbot_workshop_lead, v_jetbot_workshop)
g.add_edge(v_ml_workshop_lead, v_ml_workshop)
g.add_edge(v_ros_workshop_lead, v_ros_workshop)
g.add_edge(v_arduino_workshop_lead, v_arduino_workshop)

g.add_edge(v_workshop_coordinator, v_pi_workshop_lead)
g.add_edge(v_workshop_coordinator, v_jetbot_workshop_lead)
g.add_edge(v_workshop_coordinator, v_ml_workshop_lead)
g.add_edge(v_workshop_coordinator, v_ros_workshop_lead)
g.add_edge(v_workshop_coordinator, v_arduino_workshop_lead)

g.add_edge(v_workshop_coordinator, v_ece_students)

g.add_edge(v_event_coordinator, v_buildabot_event)
g.add_edge(v_event_coordinator, v_makersshowcase_event)
g.add_edge(v_event_coordinator, v_makersarcade_event)
g.add_edge(v_event_coordinator, v_ecedha_event)
action[g.add_edge(v_makersarcade_event, v_chilicookoff_event)] = "Supports"

g.add_edge(v_ieee_engi, v_chilicookoff_event)

g.add_edge(v_codirectors, v_event_coordinator)
g.add_edge(v_codirectors, v_workshop_coordinator)
g.add_edge(v_codirectors, v_documentation_officer)
g.add_edge(v_codirectors, v_resource_chair)
g.add_edge(v_codirectors, v_technology_officer)
g.add_edge(v_codirectors, v_outreach_officer)
g.add_edge(v_codirectors, v_ieee_engi)
g.add_edge(v_codirectors, v_ece)
g.add_edge(v_codirectors, v_buildabot_event)
g.add_edge(v_codirectors, v_makersshowcase_event)
g.add_edge(v_codirectors, v_makersarcade_event)
g.add_edge(v_codirectors, v_ecedha_event)

g.add_edge(v_ece, v_ecedha_event)
g.add_edge(v_ieee_engi, v_ece)
g.add_edge(v_ece, v_ece_students)
g.add_edge(v_ieee_engi, v_ece_students)
g.add_edge(v_ieee_engi, v_ieee_pvamu)
g.add_edge(v_ieee_engi, v_middle_schools)
g.add_edge(v_ieee_engi, v_high_schools)
g.add_edge(v_ieee_engi, v_community)

g.add_edge(v_outreach_officer, v_cs)
g.add_edge(v_outreach_officer, v_tech)
g.add_edge(v_outreach_officer, v_swe)
g.add_edge(v_outreach_officer, v_asme)
g.add_edge(v_outreach_officer, v_ieee_nsm)
g.add_edge(v_outreach_officer, v_ieee_tech)
g.add_edge(v_outreach_officer, v_ece_students)
g.add_edge(v_outreach_officer, v_ieee_uhcl)
g.add_edge(v_outreach_officer, v_ieee_pvamu)
g.add_edge(v_outreach_officer, v_ieee_engi)

g.add_edge(v_ieee_nsm, v_cs)
g.add_edge(v_ieee_tech, v_tech)

g.add_edge(v_resource_chair, v_lead_1)
g.add_edge(v_resource_chair, v_lead_2)
g.add_edge(v_resource_chair, v_lead_3)
g.add_edge(v_resource_chair, v_lead_4)
g.add_edge(v_resource_chair, v_ece)

g.add_edge(v_codirectors, v_lead_1)
g.add_edge(v_codirectors, v_lead_2)
g.add_edge(v_codirectors, v_lead_3)
g.add_edge(v_codirectors, v_lead_4)

g.add_edge(v_lead_1, v_project_1)
g.add_edge(v_lead_2, v_project_2)
g.add_edge(v_lead_3, v_project_3)
g.add_edge(v_lead_4, v_project_4)

g.add_edge(v_codirectors, v_company)

action[g.add_edge(v_pi_workshop, v_project_1)] = "Supports"
action[g.add_edge(v_arduino_workshop, v_project_2)] = "Supports"
action[g.add_edge(v_ml_workshop, v_project_3)] = "Supports"
action[g.add_edge(v_ros_workshop, v_project_3)] = "Supports"
action[g.add_edge(v_jetbot_workshop, v_project_3)] = "Supports"
action[g.add_edge(v_pi_workshop, v_project_4)] = "Supports"
action[g.add_edge(v_arduino_workshop, v_project_4)] = "Supports"

g.add_edge(v_technology_officer, v_workshop_coordinator)

for v in g.vertices():
    sz = int(50 * np.log(v.in_degree() + v.out_degree() + 2))
    print(name[v])
    print(sz)
    size[v] = sz

graph_draw(g, vertex_size=size,
           vertex_text=name,
           vertex_text_position=-2,
           vertex_text_color="white",
           edge_text=action,
           edge_marker_size=40,
           edge_font_size=30,
           edge_text_color="white",
           edge_color=np.array([0/2.5, 98/2.5, 155/2.5, 255], dtype=np.float32) / 255,
           bg_color=(0, 0, 0, 1),
           vertex_font_size=30,
           vertex_font_weight=cairo.FONT_WEIGHT_BOLD,
           vertex_fill_color=color,
           output_size=(3840, 2160),
           output="ieee-uh-makers.png")
