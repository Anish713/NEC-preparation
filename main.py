import json
import datetime
import sqlite3
import streamlit as st
from groq import Groq

# from openai import OpenAI

# from dotenv import load_dotenv
# load_dotenv()
DB_PATH = "generated_content.db"

st.set_page_config(
    page_title="Civil Engineering NEC",
    page_icon="👷‍♂️",
    layout="wide",
)

## NEC Syllabus for Civil Engineering
course_structure = {
    "Basic Civil Engineering (ACiE01)": {
        "Engineering materials": {
            "topics": [
                "Properties (physical, chemical, mechanical and thermal)",
                "Types, characteristics, composition, selection, and usage/function of engineering materials",
                "Stones, bricks, tiles, cement, lime, timber, metals/alloys, paints/varnishes, asphalt/bitumen/tar",
            ]
        },
        "Standards (NS & IS) and tests for civil engineering materials": {
            "topics": [
                "Tests of brick (water absorption and compressive tests)",
                "Tests of cement (consistency, setting time, soundness, and compressive strength)",
                "Test of aggregate (bulking of sand)",
                "Test of rebar (tensile test)",
            ]
        },
        "Building technology": {
            "topics": [
                "Building construction technology (brick and stone masonry, carpentry, painting, plastering, concrete roofing, flooring, damp proof course)",
                "Building by laws",
            ]
        },
        "Geometric properties of sections": {
            "topics": [
                "Axes of symmetry",
                "Centre of gravity of different sections (e.g., built-up plane figures, standard steel sections)",
                "Moment of inertia",
                "Radius of gyration",
            ]
        },
        "Surveying and levelling": {
            "topics": [
                "Fundamentals of surveying",
                "Measurements (linear distance, vertical distance, and angle and directions)",
                "Levelling",
                "Topographic survey (principles and applications)",
                "Simple circular curves",
                "Principles and applications of GPS/GIS",
            ]
        },
        "Estimating, costing, and valuation": {
            "topics": [
                "Types of estimate",
                "Methods of estimating",
                "Rate analysis",
                "Specifications (purpose, importance and types)",
                "Valuation",
            ]
        },
    },
    "Soil Mechanics and Foundation Engineering (ACiE02)": {
        "Soil properties and laboratory tests": {
            "topics": [
                "Tests for strength, permeability, compressibility, phase relationships",
                "Determination of index and engineering properties of soils",
                "Soil classification (descriptive, textural, ISI, MIT, USCS)",
                "Boring log interpretation",
                "Sieve analysis and interpretation of results",
                "Determination of Atterberg limits of soils",
            ]
        },
        "Stresses on soil and seepage": {
            "topics": [
                "Effective stress (factors affecting effective stress, capillary rise, and quick sand conditions)",
                "Seepage analysis [Seepage pressure, flow nets and their applications]",
                "Soil compressibility (including various indices)",
                "Compaction (definition, affecting factors)",
            ]
        },
        "Shear strength of soil and stability of slopes": {
            "topics": [
                "Concept of shear strength, principal planes and principal stresses",
                "Mohr-Coulomb theory of shear strength",
                "Calculation of normal and shear stresses at different planes",
                "Relation of principal stress at failure condition",
                "Types of shear tests",
                "Stability of slopes",
            ]
        },
        "Soil exploration, earth pressure and retaining structures": {
            "topics": [
                "Soil exploration (methods, planning, soil sampling and samplers, field tests, site investigation reports)",
                "Earth pressure theories",
                "Stability analysis of retaining walls",
                "Techniques to increase stability of retaining walls",
            ]
        },
        "Fundamentals of foundation": {
            "topics": [
                "Definition",
                "Types (Shallow and Deep)",
                "Functions",
                "Factors affecting foundation",
                "Site investigation of foundation",
                "Concept of spread and mat foundation",
            ]
        },
        "Bearing capacity and foundation settlements": {
            "topics": [
                "Bearing capacity (types, effects of various factors)",
                "Modes of foundation failure",
                "Terzaghi’s general bearing capacity theory",
                "Ultimate bearing capacity of cohesion-less and cohesive soils",
                "Consolidation (concept, types and tests)",
                "Settlement (types, nature, effects and calculations)",
            ]
        },
    },
    "Basic Water Resources Engineering (ACiE03)": {
        "Fluids and their properties": {
            "topics": [
                "Types of fluids",
                "Fluid properties (mass density, specific weight, specific gravity, specific volume, viscosity, compressibility, capillarity, surface tension, cavitation, vapour pressure)",
            ]
        },
        "Hydrostatics": {
            "topics": [
                "Pressure and head",
                "Pascal’s law",
                "Pressure-depth relationship",
                "Manometers",
                "Pressure force and centre of pressure on submerged bodies (plane and curved surfaces, practical applications)",
                "Pressure diagrams",
                "Buoyancy",
                "Stability of floating/submerged bodies",
            ]
        },
        "Hydro-kinematics and hydro-dynamics": {
            "topics": [
                "Classification of fluid flow",
                "Conservation of mass (continuity equation) and momentum equations and their applications",
                "Bernoulli’s equation and its application",
                "Flow measurement",
            ]
        },
        "Pipe flow": {
            "topics": [
                "Types of flow",
                "Governing equations",
                "Major and minor head losses",
                "HGL and TEL lines",
                "Design",
                "Pipe network problems",
                "Unsteady flow in pipes and relief devices",
            ]
        },
        "Open channel flow": {
            "topics": [
                "Geometrical properties",
                "Various types of flows",
                "Energy and momentum principles (Specific Energy and Specific Force)",
                "Types of gradually varied flow profiles",
                "Hydraulic jump (types, theory for horizontal and rectangular)",
                "Flow in mobile boundary channel (design principles/approaches; inception motion condition; Shield diagram)",
            ]
        },
        "Hydrology": {
            "topics": [
                "Hydrologic cycle and water balance components",
                "Flow measurement and rating curves",
                "Hydrographs analysis and synthetic unit hydrographs",
                "Rainfall-runoff analysis",
                "Flood hydrology (flood frequency analysis and design flood)",
                "Groundwater hydrology",
            ]
        },
    },
    "Structural Mechanics (ACiE04)": {
        "Shear forces and bending moments": {
            "topics": [
                "Axial forces, shear forces, and bending moments",
                "Loads and load superposition",
                "Relationship and diagram Interpretation (AF, SF, BM)",
            ]
        },
        "Stress and strain analysis": {
            "topics": [
                "Normal and shear stresses",
                "Principal stresses and principal planes",
                "Maximum shear stress and corresponding plane",
                "Stress-strain curves",
                "Torsion",
            ]
        },
        "Theory of flexure and columns": {
            "topics": [
                "Co-planar and pure bending",
                "Elastic curve",
                "Angle of rotation",
                "Radius of curvature and flexural stiffness",
                "Deflection",
                "Bending stress",
                "Euler’s formula for long column",
            ]
        },
        "Determinate structures-1": {
            "topics": [
                "Degree of determinacy",
                "Energy Methods",
                "Virtual Work Method",
                "Deflection of beams and portal frame",
            ]
        },
        "Determinate structures-2": {
            "topics": [
                "Influence Lines for Simple Structures with point loads and UDL",
                "Analysis of two-hinged arches",
            ]
        },
        "Indeterminate structures": {
            "topics": [
                "Flexibility Method",
                "Two-Hinged Parabolic Arches",
                "Slope Deflection Method",
                "Moment Distribution Method",
                "Stiffness Method",
                "Influence Lines for Continuous Beams",
                "Elementary Plastic Analysis",
            ]
        },
    },
    "Design of Structures (ACiE05)": {
        "Loads and load combinations": {
            "topics": [
                "Dead Load",
                "Imposed Load",
                "Wind Load",
                "Snow Load",
                "Earthquake Load",
            ]
        },
        "Concrete technology": {
            "topics": [
                "Concrete technology (materials, properties, mix design, testing, quality control, and codes (IS and NS))"
            ]
        },
        "RCC structures-1": {
            "topics": [
                "Working stress and limit state methods",
                "Design of beams and slabs",
                "Analysis of RC beams and slabs in bending, shear, deflection, bond, and end anchorage",
                "RCC",
                "NS & IS codes",
            ]
        },
        "RCC structures-2": {
            "topics": [
                "Design of columns and isolated/combined footings",
                "Pre-stressed concrete",
                "NS & IS codes",
            ]
        },
        "Steel structures": {
            "topics": [
                "Standard and built-up sections",
                "Design of bolted and welded connections",
                "Design of simple elements such as ties, struts, axially loaded columns, and column bases",
                "NS and IS codes",
            ]
        },
        "Timber and masonry structures": {
            "topics": [
                "Design principles of timber beams and columns",
                "Design of masonry structures (Mandatory rules of thumb, Nepal Building Code (NBC), properties)",
                "Failure modes of masonry structure",
                "Mud mortar, lime mortar, and cement mortar and its properties",
            ]
        },
    },
    "Water Supply, Sanitation and Environment (ACiE06)": {
        "Water sources, water quality and water demand": {
            "topics": [
                "Sources of water (surface and groundwater) and their selection",
                "Impurities in water (suspended, colloidal, dissolved)",
                "Hardness and alkalinity",
                "Living organisms in water",
                "Water-related diseases and prevention measures",
                "Drinking water quality standards",
                "Water demand estimation",
            ]
        },
        "Intake and distribution systems": {
            "topics": [
                "Types of intakes",
                "Factors affecting the selection of location of intake",
                "Types and purposes of pipe materials, joints, valves and fittings",
                "Break pressure tanks",
                "Service reservoirs and their capacity determination",
                "Design of branch and looped water distribution systems",
            ]
        },
        "Water treatment process and technologies": {
            "topics": [
                "Various treatment processes and their purposes",
                "Screening",
                "Plain sedimentation",
                "Sedimentation with coagulation",
                "Flocculation",
                "Filtration",
                "Disinfection",
                "Softening",
                "Miscellaneous treatments (aeration, removal of iron and manganese, removal of color/odour/taste)",
            ]
        },
        "Design and construction of sewers": {
            "topics": [
                "Estimation of quantity of wastewater",
                "Sewerage system and types",
                "Design criteria of sewers",
                "Shapes of sewers",
                "Sewer materials",
                "Design of sewers for separate and combined systems",
                "Construction of sewers and sewer appurtenances",
            ]
        },
        "Treatment and disposal of wastewater": {
            "topics": [
                "Characteristics and examination of sewage",
                "Decomposition of wastewater",
                "BOD and COD",
                "Primary treatment processes and design of grit chamber",
                "Secondary or biological treatment process",
                "Sewage filtration",
                "Activated sludge process",
                "Oxidation ponds",
                "Wastewater disposal by dilution (oxygen sag curve; Streeter Phelp’s equation)",
                "Wastewater disposal by land treatment",
                "Sludge and solid waste disposal methods",
                "Latrine and septic tank",
            ]
        },
        "Concept of environmental assessment": {
            "topics": [
                "BES",
                "IEE",
                "EIA",
                "Government’s act, rules/regulations/procedures for BES/IEE/EIA",
                "Types of disaster and its mitigation",
            ]
        },
    },
    "Irrigation and Drainage (ACiE07)": {
        "Water demand estimation": {
            "topics": [
                "Crop water and irrigation water requirements",
                "Water availability for irrigation",
                "Command areas",
                "Irrigation intensity",
                "Duty, delta and their relationship",
                "Water losses and irrigation efficiencies",
                "Effective rainfall",
                "Soil-moisture-irrigation relationship",
                "Depth and frequency of irrigation",
                "Design discharge for canals",
            ]
        },
        "Design of canals": {
            "topics": [
                "Canal types, network and alignment",
                "Tractive force approach of canal design",
                "Design of stable canals",
                "Alluvial canals (Kennedy’s and Lacey’s theory)",
                "Lined canals",
            ]
        },
        "Diversion headworks": {
            "topics": [
                "Components of headwork",
                "Seepage theories and their applications (Bligh’s, Lane’s, Khosla’s)",
                "Design of silt control structures (excluder, ejector and settling basins)",
                "Design of weir/barrage (crest, length and thickness of impervious floor)",
                "Design of energy dissipaters",
            ]
        },
        "River training works": {
            "topics": [
                "River stages and need of river training",
                "Design of river training works (guide bund and launching aprons, levees and spurs)",
                "Watershed management",
            ]
        },
        "Regulating and cross-drainage structures": {
            "topics": [
                "Functions of various types of regulators",
                "Design of regulators and escapes (crest, length and thickness of impervious floor)",
                "Design of pipe outlet (free and submerged)",
                "Design of vertical drop (crest, length, and thickness of impervious floor)",
                "Design of cross-drainage structures",
            ]
        },
        "Water logging and drainage": {
            "topics": [
                "Causes, effects and preventive measures",
                "Design of surface and sub-surface drainage systems",
            ]
        },
    },
    "Hydropower (ACiE08)": {
        "Planning of hydropower projects": {
            "topics": [
                "Power potential (gross, technical, economic) of Nepal and the world",
                "Stages of hydropower development",
                "Hydropower development in Nepal (history, policy, acts & regulation)",
            ]
        },
        "Power and energy potential study": {
            "topics": [
                "Power and energy potentials",
                "Methods of fixing installed capacity of a plant",
                "Types of hydropower plants on various basis",
                "Components of different types of hydropower projects",
                "Reservoirs and their regulation",
            ]
        },
        "Headworks of storage plants": {
            "topics": [
                "Components of a typical storage plant",
                "Dams (types, functions, selection, design, failure modes and remedies)",
                "Stability analysis of gravity dam",
                "Seepage control and foundation treatment in dams",
                "Design of intake, spillway and energy dissipaters",
                "Gates (types and locations)",
            ]
        },
        "Headworks of run-of-river (ROR) plants": {
            "topics": [
                "Components of a typical ROR plant",
                "Design of intake",
                "Methods of bed and suspended load handling",
                "Design of settling basin (practice and concentration approach)",
                "Estimation of sediment volume in settling basin",
                "Flushing of deposited sediment",
                "Estimation of flushing frequency for sediments",
            ]
        },
        "Water conveyance structures": {
            "topics": [
                "Hydraulic tunnels, x-sections, and hydraulic design (velocity and sizing)",
                "Tunnel lining",
                "Design of forebay and surge tanks",
                "Design of penstocks and pressure shaft",
                "Hydraulic transients (water hammer)",
            ]
        },
        "Hydro-electric machines and powerhouse": {
            "topics": [
                "Hydro-mechanical equipment and their functions",
                "Types of turbines and performance characteristics",
                "Selection of turbine and their specific speed",
                "Preliminary design of Francis and Pelton turbines",
                "Scroll case and draft tubes",
                "Generators (types, rating)",
                "Governors",
                "Pumps and their performance characteristics",
                "Powerhouse (types, general arrangements, dimensions)",
            ]
        },
    },
    "Transportation (ACiE09)": {
        "Highway planning and survey": {
            "topics": [
                "Modes of transport",
                "History of road development in Nepal",
                "Classification of roads",
                "Road survey",
                "Highway alignment and controlling factors",
                "Evaluating alternate alignments",
                "Road Standards of Nepal",
            ]
        },
        "Geometric design of highway": {
            "topics": [
                "Basic design control and criteria",
                "Elements of highway cross-section",
                "Highway curves",
                "Super elevation",
                "Average and ruling gradients",
                "Stopping sight distance",
                "Design considerations for horizontal and vertical alignments",
                "Extra widening and set back distance",
                "Design of road drainage structures",
                "Design considerations for hill roads",
            ]
        },
        "Highway materials": {
            "topics": [
                "Types of aggregates and tests on their gradation, strength, durability",
                "Binding materials and their tests",
                "Design of asphalt mixes",
                "Evaluation of subgrade soil",
            ]
        },
        "Traffic engineering and safety": {
            "topics": [
                "Impact of human and vehicular characteristics on traffic planning",
                "Traffic operations and regulations",
                "Traffic control devices",
                "Traffic studies (volume, speed, O&D, traffic capacity, traffic flow characteristics, parking, accident, flow)",
                "Road intersections (types, configurations, design)",
                "Traffic lights",
                "Factors influencing night visibility",
                "Road safety measures",
            ]
        },
        "Road pavement": {
            "topics": [
                "Different types of pavement",
                "Design methods for flexible and rigid pavements (DOR Guidelines)",
                "Loads and other factors controlling pavement design",
                "Stress due to load, temperature",
            ]
        },
        "Road construction & maintenance": {
            "topics": [
                "Activities, techniques, tools, equipment and plants used in road construction",
                "Preparation of road subgrade",
                "Field compaction control and soil stabilization",
                "Construction of asphalt concrete layers",
                "Construction procedure for penetration macadam, bituminous bound macadam and plain cement concrete pavements",
                "Road maintenance, repair and rehabilitation",
            ]
        },
    },
    "Project Planning, Design and Implementation (AALL10)": {
        "Engineering drawings and its concepts": {
            "topics": [
                "Fundamentals of standard drawing sheets",
                "Dimensions",
                "Scale",
                "Line diagram",
                "Orthographic projection",
                "Isometric projection/view",
                "Pictorial views",
                "Sectional drawing",
            ]
        },
        "Engineering Economics": {
            "topics": [
                "Understanding of project cash flow",
                "Discount rate, interest and time value of money",
                "Basic methodologies for engineering economics analysis (Discounted Payback Period, NPV, IRR & MARR)",
                "Comparison of alternatives",
                "Depreciation system and taxation system in Nepal",
            ]
        },
        "Project planning and scheduling": {
            "topics": [
                "Project classifications",
                "Project life cycle phases",
                "Project planning process",
                "Project scheduling (bar chart, CPM, PERT)",
                "Resources levelling and smoothing",
                "Monitoring/evaluation/controlling",
            ]
        },
        "Project management": {
            "topics": [
                "Information system",
                "Project risk analysis and management",
                "Project financing",
                "Tender and its process",
                "Contract management",
            ]
        },
        "Engineering professional practice": {
            "topics": [
                "Environment and society",
                "Professional ethics",
                "Regulatory environment",
                "Contemporary issues/problems in engineering",
                "Occupational health and safety",
                "Roles/responsibilities of Nepal Engineers Association (NEA)",
            ]
        },
        "Engineering Regulatory Body": {
            "topics": ["Nepal Engineering Council (Acts & Regulations)"]
        },
    },
}


def create_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS content
                     (topic TEXT, lesson TEXT, content TEXT, PRIMARY KEY (topic, lesson))"""
        )
        c.execute(
            """CREATE TABLE IF NOT EXISTS problems
                     (topic TEXT, level TEXT, problems TEXT, PRIMARY KEY (topic, level))"""
        )
        c.execute(
            """CREATE TABLE IF NOT EXISTS assessments
                     (topic TEXT, level TEXT, assessment TEXT, PRIMARY KEY (topic, level))"""
        )
        c.execute(
            """CREATE TABLE IF NOT EXISTS user_answers
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, topic TEXT, level TEXT, answers TEXT, score REAL)"""
        )
        conn.commit()


def store_content(topic, lesson, content):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            "INSERT OR REPLACE INTO content (topic, lesson, content) VALUES (?, ?, ?)",
            (topic, lesson, content),
        )
        conn.commit()


def retrieve_content(topic, lesson):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            "SELECT content FROM content WHERE topic = ? AND lesson = ?",
            (topic, lesson),
        )
        row = c.fetchone()
        if row:
            return row[0]
        return None


def store_problems(topic, level, problems):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            "INSERT OR REPLACE INTO problems (topic, level, problems) VALUES (?, ?, ?)",
            (topic, level, problems),
        )
        conn.commit()


def retrieve_problems(topic, level):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            "SELECT problems FROM problems WHERE topic = ? AND level = ?",
            (topic, level),
        )
        row = c.fetchone()
        if row:
            return row[0]
        return None


def store_assessment(topic, level, assessment):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            "INSERT OR REPLACE INTO assessments (topic, level, assessment) VALUES (?, ?, ?)",
            (topic, level, assessment),
        )
        conn.commit()


def store_user_answers(topic, level, answers, score):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            """
            INSERT OR REPLACE INTO user_answers (topic, level, answers, score)
            VALUES (?, ?, ?, ?)
            """,
            (topic, level, json.dumps(answers), score),
        )
        conn.commit()


def retrieve_assessment(topic, level):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute(
            "SELECT assessment FROM assessments WHERE topic = ? AND level = ?",
            (topic, level),
        )
        row = c.fetchone()
        if row:
            return row[0]
        return None


def generate_dynamic_content_groq(query, model_name=None, temperature=0.5):
    client = Groq()
    stream = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """As a civil engineering tutor, your task is to provide detailed explanations of requested engineering topics. Your goal is to cover all crucial aspects of the topic, incorporating relevant examples to enhance understanding. Aim to address alll conceptual, confusing and important points that might be asked in multiple-choice questions for knowledge assessment for given topic in civil engineering. Remember that you are tutoring an engineering background student, so teach concepts in detail and don't miss anything.

Your responses should be clear and detailed, offering thorough explanations that enhance the reader's understanding of the topic. Additionally, be prepared to provide JSON responses when explicitly requested by the user, ensuring that any single backward slashes in the JSON are replaced with two backslashes to ensure correct display when extracted and rendered in the UI using streamlit. Otherwise, when responding besides JSON, respond as it is.

Please ensure that your explanations are informative and well-structured, allowing for a comprehensive grasp of the engineering topics.""",
            },
            {"role": "user", "content": query},
        ],
        # model=model_name or "Llama-3.1-8b-Instant",
        model=model_name or "llama-3.1-70b-versatile",
        temperature=temperature,
        top_p=1,
        stream=True,
    )

    response_text = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            response_text += content

    return response_text


def generate_dynamic_content_github(query, model_name=None, temperature=0.5):
    pass


def generate_dynamic_content(
    query, model_type="groq", model_name=None, temperature=0.7
):
    if model_type == "groq":
        return generate_dynamic_content_groq(query, model_name, temperature)
    elif model_type == "github":
        return generate_dynamic_content_github(query, model_name, temperature)


def extract_json_from_response(response_text):
    """Extract the first valid JSON object from a given text."""
    brace_count = 0
    json_str = ""
    json_started = False

    for char in response_text:
        if char == "{":
            brace_count += 1
            json_started = True

        if json_started:
            json_str += char

        if char == "}":
            brace_count -= 1

        if json_started and brace_count == 0:
            break

    if brace_count == 0 and json_started:
        try:
            return json.loads(json_str)
        except (ValueError, json.JSONDecodeError) as e:
            # # Print error for debugging
            # print(f"Error decoding JSON: {e}")
            # print(f"Problematic JSON string: {json_str}")
            # st.error(
            #     "There was an error decoding the JSON response. Please generate again."
            # )
            # st.text(f"Error: {e}")
            # st.text(f"JSON string: {json_str}")
            pass
    else:
        # print("JSON brace count mismatch or JSON not started properly.")
        # st.error("JSON brace count mismatch or JSON not started properly.")
        # st.text(f"Response text: {response_text}")
        return None


create_db()


def course_dashboard():
    st.title("NEC Study: CIVIL ENGINEERING (Check Sidebar!!!) ")

    selected_unit = st.sidebar.selectbox(
        "Choose a Unit", ["Select a Unit"] + list(course_structure.keys())
    )

    if selected_unit and selected_unit != "Select a Unit":
        units = course_structure.get(selected_unit, {})
        selected_lesson = st.sidebar.selectbox(
            "Select a Lesson", list(units.keys()) if units else []
        )

        if selected_lesson:
            lessons = units[selected_lesson].get("topics", [])
            selected_topic = st.sidebar.selectbox(
                "Choose a topic", lessons if lessons else []
            )

            if selected_topic:
                st.header(f"{selected_lesson}: {selected_topic}")

                regenerate_content = st.sidebar.button(
                    "Regenerate Content", key="regenerate_content"
                )

                explanation = retrieve_content(selected_unit, selected_topic)
                if regenerate_content or explanation is None:
                    with st.spinner("Generating explanation..."):
                        explanation = generate_dynamic_content(
                            f"Explain topic {selected_topic} of  lesson {selected_lesson} from unit {selected_unit} in detail."
                        )
                        store_content(selected_unit, selected_topic, explanation)
                        st.sidebar.write("New content generated")
                else:
                    st.sidebar.write("Using cached content")

                st.write(explanation, unsafe_allow_html=True)

                st.write("### MCQs")
                assessment_expander_key = f"{selected_unit}_assessment_expander"
                st.session_state.setdefault(assessment_expander_key, False)

                if st.button(f"Get MCQs", key="take_assessment"):
                    st.session_state[assessment_expander_key] = True

                if st.session_state[assessment_expander_key]:
                    with st.spinner("Generating assessment..."):
                        assessment_dashboard(selected_unit, selected_topic)


def generate_assessment_with_retries(selected_topic, selected_lesson):
    max_retries = 1
    temperatures = [0.7, 0.3, 0.9]
    groq_models = [
        "Llama-3.1-70b-Versatile",
        "Llama-3.1-8b-Instant",
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
        "llama3-8b-8192",
    ]
    github_models = ["gpt-4o-mini", "gpt-4o"]

    def try_generate(model_type, model_name, temperature):
        try:
            # st.write(
            #     f"Attempting generation with {model_type} model '{model_name}' at temperature {temperature}"
            # )
            assessment_response = generate_dynamic_content(
                f"""Based on the following lesson content from Engineering study materials, generate exactly 15 multiple-choice questions (MCQs) along with their respective answers for the topic {selected_topic} from lesson {selected_lesson}. Make sure that only one option is correct while other options are wrong but seems quite similar to the actual option. This is to prepare civil engineering completed students for top level MCQ assessments to be taken by Engineering council. Each question from MCQ carries either 1 or 2 marks. For 2 marks question, there may be numerical type question only if the lesson topic is related to such. Strictly use the given JSON Format below as your response format.
                
                # Lesson Content: 
                {retrieve_content(selected_topic, selected_lesson)}
                
                # JSON Format:
                {{
                    "questions": [
                        {{
                            "question": "Question 1",
                            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                            "correct_answer": "Correct option for  Question 1"

                        }},
                        {{
                            "question": "Question 2",
                            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                            "correct_answer": "Correct option for Question 2"
                        }},
                        ...
                    ]
                }}""",
                model_type=model_type,
                model_name=model_name,
                temperature=temperature,
            )

            assessment_json = extract_json_from_response(assessment_response)
            return assessment_json
        except Exception as e:
            st.error(f"Error occurred: {str(e)}. Retrying...")

    model_index = 0
    attempts = 0
    temperature_index = 0
    while model_index < len(groq_models):
        model_name = groq_models[model_index]
        temperature = temperatures[temperature_index]
        assessment_json = try_generate("groq", model_name, temperature)
        if assessment_json:
            return assessment_json
        attempts += 1
        temperature_index += 1
        if temperature_index >= len(temperatures):
            temperature_index = 0
            model_index += 1
        if attempts >= max_retries * len(temperatures) * len(groq_models):
            break

    st.error("Maximum retry attempts reached with Groq models. Switching...")

    model_index = 0
    attempts = 0
    temperature_index = 0
    while model_index < len(github_models):
        model_name = github_models[model_index]
        temperature = temperatures[temperature_index]
        assessment_json = try_generate("github", model_name, temperature)
        if assessment_json:
            return assessment_json
        attempts += 1
        temperature_index += 1
        if temperature_index >= len(temperatures):
            temperature_index = 0
            model_index += 1
        if attempts >= max_retries * len(temperatures) * len(github_models):
            break
        st.error("Maximum retry attempts reached with Github models.")
    st.error("Maximum retry attempts reached with all models.")
    st.error("Failed to generate assessment after several attempts.")
    st.error("Please retry generating again...")
    return None


def generate_feedback(question, student_answer, actual_answer):
    # Construct the prompt to generate feedback
    prompt = f"""
    Provide proper feedback offering why student's answer is incorrect and brief explanation of the right answer based on the following details:
    # Question: 
    {question}
    # Student's Answer: 
    {student_answer}
    # Correct Answer: 
    {actual_answer}
    
    
    """
    # First, try using Groq models
    try:
        # print(f"Generating feedback using Groq models.")
        return generate_dynamic_content_groq(
            query=prompt, model_name="llama-3.1-70b-versatile", temperature=0.7
        )
    except Exception as e_groq:
        # print(f"Error using Groq model: {e_groq}")
        pass


def assessment_dashboard(selected_topic, selected_lesson):
    st.header(f"Assessment: {selected_lesson}")

    # Retrieve assessment from database
    assessment_json = retrieve_assessment(selected_topic, f"{selected_lesson}")

    if assessment_json is None:
        with st.spinner("Generating assessment..."):
            assessment_json = generate_assessment_with_retries(
                selected_topic, selected_lesson
            )
            store_assessment(
                selected_topic,
                f"{selected_lesson}",
                json.dumps(assessment_json),
            )
            st.rerun()

    if isinstance(assessment_json, dict):
        assessment = assessment_json
    elif isinstance(assessment_json, str):
        assessment = json.loads(assessment_json)
    else:
        raise ValueError("Invalid type for assessment_json")

    questions = assessment["questions"]
    answers = []

    if "start_time" not in st.session_state:
        st.session_state["start_time"] = datetime.datetime.now()

    for i, question in enumerate(questions):
        question_key = f"question_{i}_start_time"
        if question_key not in st.session_state:
            st.session_state[question_key] = datetime.datetime.now()

        st.markdown(f":orange[**Question {i+1}:** {question['question']}]")
        options = question["options"]
        answer = st.selectbox(
            f"Select an answer for Q{i+1}", options, key=f"answer_{i+1}"
        )
        answers.append(answer)

    # Submit the assessment
    if st.button("Submit"):
        score = 0
        correct_answers = []
        wrong_answers = []

        for i, question in enumerate(questions):
            if answers[i] == question["correct_answer"]:
                score += 1
                correct_answers.append(i + 1)
            else:
                wrong_answers.append(i + 1)

        total_time = (
            datetime.datetime.now() - st.session_state["start_time"]
        ).total_seconds()

        store_user_answers(
            selected_topic,
            "NEC",
            answers,
            score,
        )

        if score >= 1:
            st.success(f"**You scored {score}/15**", icon="🔥")
            # mycode = "<script>alert('Check your feedback😀 Then, You may move to next lesson. Good Luck! ')</script>"
            # components.html(mycode, height=0, width=0)
            st.info("Check Feedback below for wrong Answers, if any.")
            st.markdown("# Feedback for Wrong Answers:")
            st.write("## :green[**Correctly Answered:**]")
            for i in correct_answers:
                st.write(
                    f"""➡️ You have correctly answered **Question {i}: :green[{questions[i-1]['correct_answer']}]** ✅"""
                )

            st.write("## :red[**Wrongly Answered:**]")
            for i in wrong_answers:
                st.markdown(f":red[**Question {i}:**] {questions[i-1]['question']}")
                st.write(
                    f"""➡️ You answered: :red[{answers[i-1]}] ❌. Correct Answer is :green[**{questions[i-1]['correct_answer']}**] ✔️"""
                )

                feedback = generate_feedback(
                    question=questions[i - 1]["question"],
                    student_answer=answers[i - 1],
                    actual_answer=questions[i - 1]["correct_answer"],
                )
                st.info(f":green[**Feedback:**] {feedback}", icon="🚨")
                st.divider()

        else:
            st.warning(f"You scored {score}/15. REVISE AGAIN!!!", icon="👀")
            st.write(f"You need to score at least 7 to check feedback.")  # Modify above
            st.write(f"Please revise the provided resources and Try again...")

    # option to generate a new quiz
    if st.button("New Quiz"):
        with st.spinner("Generating a new quiz..."):
            assessment_json = generate_assessment_with_retries(
                selected_topic, selected_lesson
            )
            store_assessment(
                selected_topic,
                f"{selected_lesson}",
                json.dumps(assessment_json),
            )
            st.rerun()


def stream_response(query):
    client = Groq()

    stream = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful tutor for civil engineering student from Nepal. Skip Introductions and give brief and correct answer or solution to the query of student to help them have clear concepts on their asked question.",
            },
            {"role": "user", "content": query},
        ],
        # model="llama3-8b-8192",
        model="llama-3.1-70b-versatile",
        temperature=0.7,
        max_tokens=4096,
        top_p=1,
        stop=None,
        stream=True,
    )

    response_text = ""
    for chunk in stream:
        delta_content = chunk.choices[0].delta.content
        if delta_content:  # Check if not None
            response_text += delta_content
            yield response_text


def main():
    # st.sidebar.title("NEC Learning App")

    # Ensure database and tables are created
    create_db()
    course_dashboard()

    with st.sidebar:
        st.sidebar.title("NEC Learning App")
        query_sidebar = st.chat_input("Ask your query", key="sidebar_chat_input")

        if query_sidebar:
            st.session_state.messages_sidebar = [
                {"role": "user", "content": query_sidebar}
            ]

            with st.chat_message("user"):
                st.code(query_sidebar)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                response_text = ""

                for ast_mess in stream_response(query_sidebar):
                    response_text = ast_mess
                    message_placeholder.markdown(response_text)

                st.session_state.messages_sidebar.append(
                    {"role": "assistant", "content": response_text}
                )

    query = st.chat_input("Ask your query", key="main_chat_query")

    if query:
        st.session_state.messages = [{"role": "user", "content": query}]

        with st.chat_message("user"):
            st.code(query)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response_text = ""

            for ast_mess in stream_response(query):
                response_text = ast_mess
                message_placeholder.markdown(response_text)

            st.session_state.messages.append(
                {"role": "assistant", "content": response_text}
            )


if __name__ == "__main__":
    main()
