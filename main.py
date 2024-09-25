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
    page_title="EEE NEC Preparation",
    page_icon="⚡",
    layout="wide",
)

# NEC syllabus for Electrical and Electronic Engineering (AEEE)
course_structure = {
    "Fundamentals of Electrical Components and Circuits (AEEE01)": {
        "Basic concept": {
            "topics": [
                "Ohm´s Law, electric voltage, current, power and energy, conducting and insulating materials",
                "Series and parallel electric circuits, start-delta and delta-star conversion",
                "Kirchhoff’s law, linear and non-linear circuits",
                "Bilateral and unilateral circuits, active and passive circuits",
            ]
        },
        "Network theorems": {
            "topics": [
                "Concept of superposition theorem, Thevenin's theorem, Norton’s theorem",
                "Maximum power transfer theorem, R-L, R-C, R-L-C circuits",
                "Resonance in AC series and parallel circuits, active and reactive power",
            ]
        },
        "Alternating current fundamentals": {
            "topics": [
                "Principle of generation of alternating voltages and currents",
                "Equations and waveforms of AC, average, peak and rms values",
                "Three phase system",
            ]
        },
        "Electric recruit response (transient analysis)": {
            "topics": [
                "Steady state and transient analysis of R-L, R-C, R-L-C circuits"
            ]
        },
        "Analysis of one port and two port networks": {
            "topics": [
                "Transfer functions, poles and zeros of networks",
                "Relationship between poles/zeros locations and system response",
                "One port passive circuits, impedance and admittance functions",
                "Two-port parameters of networks, definitions of two-port networks",
                "Short circuit admittance parameters, open circuit impedance parameters, transmission parameters, hybrid parameters, inter-relationship between parameters of two-port network",
            ]
        },
        "Synthesis of one port and two port networks": {
            "topics": [
                "Hurwitz polynomials and properties, positive real functions",
                "Foster and Cauer forms, synthesis of RL, RC and LC networks",
                "Synthesis of resistively terminated active and passive two ports, ladder networks",
            ]
        },
    },
    "Fundamentals of Electronic Devices and Circuits (AEEE02)": {
        "Semiconductor diodes and transistors": {
            "topics": [
                "Overview of electronic devices: Semiconductor diode, PN junction characteristics",
                "Ideal and practical diode; I-V characteristics; Forward and reverse bias",
                "Diode configurations: Series, parallel and hybrid, large signal and small signal model",
                "Half wave and full wave rectifiers, various types of diodes",
                "Bipolar Junction Transistor (BJT): PNP and NPN transistors, modes of operation, BJT biasing",
            ]
        },
        "JFET and MOSFET": {
            "topics": [
                "Field Effect Transistor (FET) and Junction Field Effect Transistor (JFET) construction",
                "Basic operation and characteristics of JFET",
                "Metal Oxide Semiconductor Field Effect Transistor (MOSFET): structure and operation",
                "Types of MOSFET, current-voltage characteristics, MOSFET as amplifier and switch",
                "Working principle of CMOS, applications of MOSFET and CMOS",
            ]
        },
        "Amplifiers and signal generators": {
            "topics": [
                "Definition of amplification and gain, types of amplifiers",
                "Design procedure of low frequency amplifiers using BJT and MOSFET",
                "Power amplifiers: Class A, Class B, Class AB amplifiers",
                "Basic principles of oscillators: Positive feedback, condition for oscillation",
                "Waveform generators: Square wave, triangular wave, and sawtooth wave generators",
            ]
        },
        "Operational amplifier characterization": {
            "topics": [
                "Overview of differential amplifier, basic parameters of ideal Op-Amp",
                "Ideal and practical characteristics of Op-Amp",
                "Derivation of gain for inverting and non-inverting amplifiers with feedback",
                "Concept of voltage follower and negative ground",
                "Op-Amp applications: Integration, differentiation, addition, clipping and comparator circuits",
            ]
        },
        "Nonlinear circuits and active filters": {
            "topics": [
                "Logarithmic and exponential amplifiers, logarithmic multiplier",
                "Phase locked loop, voltage to frequency and frequency to voltage conversion",
                "Characteristics and advantages of active filters",
                "Active first order filter, high pass and low pass filters",
            ]
        },
        "Logic families and ICs": {
            "topics": [
                "Evolution and characteristics of logic families",
                "Classification of logic families",
                "Simple circuits for logic gates: DTL, RTL, TTL",
            ]
        },
    },
    "Digital Logic and Microprocessor (AEEE03)": {
        "Digital logic": {
            "topics": [
                "Number systems, logic levels, logic gates",
                "Boolean algebra, Sum-of-Products method, Product-of-Sums method",
                "Truth table to Karnaugh map",
            ]
        },
        "Combinational and arithmetic circuits": {
            "topics": [
                "Multiplexers and demultiplexers",
                "Decoder and encoder",
                "Binary addition and binary subtraction",
                "Operations on unsigned and signed binary numbers",
            ]
        },
        "Sequential logic circuit": {
            "topics": [
                "RS flip-flops, gated flip-flops, edge triggered flip-flops, master-slave flip-flops",
                "Types of registers and applications of shift registers",
                "Asynchronous counters and synchronous counters",
            ]
        },
        "Microprocessor": {
            "topics": [
                "Internal architecture and features of microprocessors",
                "Assembly language programming",
            ]
        },
        "Interfacing (Microprocessor system)": {
            "topics": [
                "Memory device classification and hierarchy",
                "Interfacing I/O and memory parallel interface",
                "Introduction to programmable peripheral interface (PPI)",
                "Serial interface: Synchronous and asynchronous transmission",
                "Serial interface standards: RS232, RS423, RS422, USB, introduction to USART, Direct Memory Access (DMA) and DMA controllers",
            ]
        },
        "Computer organization": {
            "topics": [
                "Control and central processing unit",
                "Control memory, addressing sequencing",
                "Computer configuration and microinstruction format",
                "Design of control unit, CPU structure and function",
                "Arithmetic and logic unit, instruction formats, addressing modes, data transfer and manipulation, RISC and CISC pipelining and parallel processing",
            ]
        },
    },
    "Computer Programming (AEEE04)": {
        "Introduction to programming": {
            "topics": [
                "Tokens, operators, formatted/unformatted input/output",
                "Structured and object-oriented programming, algorithms and flowcharts",
                "Data types, variables, declaration, constants (string, numeric, character constant)",
                "Arithmetic operators, assignment operators, logical and comparison operations",
                "Input and output statements",
            ]
        },
        "Control statements": {
            "topics": [
                "If statement, if-else statement, switch statement",
                "Loop statements: for loop, while loop, do-while loop",
                "Breaking control statements",
            ]
        },
        "Functions": {
            "topics": [
                "Defining functions and use of functions",
                "Function prototypes, passing arguments to functions",
                "Recursive functions",
            ]
        },
        "Pointers and data file": {
            "topics": [
                "Pointer declaration and pointer arithmetic",
                "Operations on pointers, pointer and array (one-dimensional array)",
                "Dynamic memory allocation",
            ]
        },
        "Array and structures": {
            "topics": [
                "Defining and processing an array",
                "Passing array to functions, multidimensional arrays",
                "Declaration and initialization of structures, array of structures",
                "Pointer to structures",
            ]
        },
        "Features of object-oriented programming": {
            "topics": [
                "Inline functions, function overloading",
                "Class and objects, member functions, private member functions",
                "Initializing an object, static data members, static member functions",
                "Operator overloading, inheritance, polymorphism",
            ]
        },
    },
    "Measurement, Instrumentation and Control (AEEE05)": {
        "Measurement and error": {
            "topics": [
                "Static and dynamic errors",
                "Maxwell bridges, Schering bridge, Wien bridge",
            ]
        },
        "Transducers, sensors and signal conditioning": {
            "topics": [
                "Definitions and classifications of transducers",
                "Transducer selection factors",
                "Types of transducers: resistive, capacitive, inductive, linear variable differential transformer",
                "Various sensors: position, proximity, motion, pressure, level, flow, strain gauges, load cells",
                "Signal conditioning techniques: linearization, filtering, impedance and power matching; DAC and ADC performance parameters",
            ]
        },
        "Electrical measurements and instruments": {
            "topics": [
                "Essential requirements of instruments: deflection, controlling and damping systems",
                "Types and working principles of PMMC instruments, voltmeters, ammeters, ohmmeters, clamp-meters",
                "Working principles of multi-meters, wattmeters, energy meters, time of day meters",
                "Power factor meters, frequency meters, phase meters, instrument transformers, megger, tachometer",
            ]
        },
        "System modeling": {
            "topics": [
                "Control systems: definition and classification",
                "Open loop and closed loop systems",
                "Modeling mechanical systems and electrical circuits",
                "Transfer functions, modeling of liquid level systems and thermal systems",
                "Modeling of sensors, encoders, generators, and electromechanical systems",
            ]
        },
        "Block diagram representation": {
            "topics": [
                "Rules for block diagram reduction and examples",
                "Definitions of signal flow graph and rules for construction",
                "Conversion between block diagram and signal flow graph",
                "Response of first order and second order systems to test signals",
            ]
        },
        "Stability analysis": {
            "topics": [
                "Definitions of stability and stable systems",
                "Routh-Hurwitz criterion, root locus plot introduction and construction rules",
                "Frequency response analysis: Bode plots and stability criteria",
                "Polar plots, Nyquist’s stability criterion, stability margins",
            ]
        },
    },
    "Electrical Machines (AEEE06)": {
        "Transformers fundamentals": {
            "topics": [
                "Importance and applications of transformers",
                "Types and construction of transformers",
                "Theory and operation of single-phase transformers, EMF equation",
                "Voltage regulation, losses and efficiency, equivalent circuit parameters",
                "Transformer tests and three-phase transformers",
            ]
        },
        "DC generators": {
            "topics": [
                "Generator principles and construction",
                "Types of generators and winding",
                "Losses and efficiency, no-load and load characteristics",
                "Armature reaction and commutation",
                "Parallel operation of generators and induced voltage equations",
            ]
        },
        "DC motors": {
            "topics": [
                "Motor principles and types",
                "Construction and output characteristics of different motors",
                "Speed control, starting and applications",
                "Losses and efficiency; introduction to brushless DC motors",
                "Testing of DC machines, reversing and braking",
            ]
        },
        "Induction motors": {
            "topics": [
                "Principle of operation of induction motors",
                "Squirrel cage and wound rotor construction",
                "Equivalent circuit, synchronous speed, and slip",
                "Torque-speed characteristics and losses",
                "Single-phase induction motors: torque-speed characteristics and applications",
            ]
        },
        "Synchronous generators": {
            "topics": [
                "Introduction and construction of synchronous generators",
                "Winding diagram and power/torque relations",
                "Speed and frequency, EMF equation",
                "Voltage regulation and equivalent circuit",
                "Generator synchronization and permanent magnet synchronous generator applications",
            ]
        },
        "Synchronous motors": {
            "topics": [
                "Principle of operation of synchronous motors",
                "Torque-angle characteristics and method of starting",
                "Counter voltage (CEMF) and armature reaction voltage",
                "Excitation methods and power factor improvement",
                "Speed control",
            ]
        },
    },
    "Signals, Systems and Frequency Domain Analysis (AEEE07)": {
        "Fundamentals of signal and systems": {
            "topics": [
                "Signal classification: continuous time and discrete time signals",
                "Periodic and aperiodic signals, energy and power signals",
                "Even and odd signals, orthogonal signals",
                "Causal, anti-causal and non-causal signals, transformation of signals",
                "Unit impulse, unit step and unit ramp, convolution integral, convolution sum",
            ]
        },
        "Laplace transforms": {
            "topics": [
                "Definition and properties of Laplace transforms",
                "Laplace transform of common forcing functions and inverse transforms",
                "Partial fraction expansion and Heaviside’s expansion theorem",
                "Applications of Laplace transform in solving differential equations",
                "Transfer function and frequency response",
            ]
        },
        "Fourier series and transforms": {
            "topics": [
                "CT Fourier series and Fourier integral representation",
                "Forward and inverse Fourier transforms and properties",
                "Parseval's theorem, discrete time Fourier series representation",
                "Properties of discrete time Fourier transform (DTFT)",
                "Forward and inverse DTFT representation",
            ]
        },
        "Z transform and digital systems": {
            "topics": [
                "Sampling and the sampling theorem, aliasing",
                "Conversion to discrete time signals and reconstruction",
                "Definition and properties of the z-transform",
                "Inverse z-transform and system response",
                "Transfer function H(z) and stability tests of discrete time systems",
            ]
        },
        "Application of frequency domain analysis": {
            "topics": [
                "Stability analysis and spectral analysis",
                "Spectrum sensing and correlation",
                "System design",
            ]
        },
        "Filters": {
            "topics": [
                "Filters and applications: ideal and digital filters",
                "Active and passive filters, frequency responses",
                "Butterworth and Chebyshev filters",
                "Introduction to digital filters and basic types of filtering",
                "Transfer function and frequency response of FIR and IIR filters",
            ]
        },
    },
    "Communication Systems (AEEE08)": {
        "Basic elements of communication systems": {
            "topics": [
                "Block diagram of analog and digital communication systems",
                "Analog vs Digital Communication systems",
                "Baseband and band pass systems",
                "Signal and noise in communication systems",
                "Statistical description of noise and types of noise",
            ]
        },
        "Analog modulation and demodulation": {
            "topics": [
                "Amplitude Modulation (AM) and DSB-SC modulation",
                "Demodulators: square law and synchronous demodulation",
                "Carrier recovery techniques",
                "SSB-SC modulation and demodulation",
                "Frequency Modulation (FM) and Phase Modulation (PM)",
            ]
        },
        "Digital communication and modulation": {
            "topics": [
                "Types of Digital Modulation Techniques: BASK, BFSK, BPSK",
                "M-ary Techniques and QPSK",
                "Quadrature Amplitude Modulation (QAM)",
                "Error probability in PSK systems",
                "Shannon Hartley Channel Capacity theorem and multiplexing",
            ]
        },
        "Pulse modulation and coding": {
            "topics": [
                "Pulse Amplitude Modulation (PAM) and bandwidth requirement",
                "Pulse Code Modulation (PCM): encoders, decoders, quantization",
                "Quantization error and Companders",
                "Differential PCM and Delta Modulation (DM)",
                "Adaptive DM and continuously variable DM",
            ]
        },
        "Error control coding techniques": {
            "topics": [
                "Introduction to channel coding and Hamming distance",
                "Parity and parity coding, block codes",
                "Linear block code and systematic linear block coding",
                "Cyclic code and introduction to convolution coding",
                "Code trees, trellis, state diagram, and decoding methods",
            ]
        },
        "Data communication": {
            "topics": [
                "Overview of data communication networks",
                "Parallel and serial communication",
                "Bandwidth utilization and multiplexing",
                "Frequency Division Multiplexing (FDM) and Time Division Multiplexing (TDM)",
                "TCP/IP and OSI Model with layered architecture",
            ]
        },
    },
    "Power Systems and Devices (AEEE09)": {
        "Power plant": {
            "topics": [
                "Electrical Power System: Basic structure of power system",
                "Generation of Electrical Power: Thermal, Hydro, Nuclear",
                "Solar Photovoltaic System, Wind Energy Conversion Systems",
                "Tidal power plant, Geothermal power plants, Fuel Cells",
                "Energy Storage Systems",
            ]
        },
        "Transmission and distribution of electrical power": {
            "topics": [
                "Electric supply system and various systems of power transmission",
                "Economic choice of conductor size and transmission voltage",
                "Mechanical design of overhead lines: conductor materials, line supports",
                "Insulators, corona, right of way, distribution systems",
                "Classification of distribution systems and load curves",
            ]
        },
        "Protection and control of electrical power system": {
            "topics": [
                "Principles of power system protection",
                "Fuse operation, Miniature Circuit Breaker and its operation",
                "Power circuit breaker operation and types",
                "Relays and their types, protection schemes for generators and transformers",
                "Supervisory Control and Data Acquisition System (SCADA), Smart Grid",
            ]
        },
        "Residential and industrial electrification": {
            "topics": [
                "Service mains and types of distribution systems in buildings",
                "Types of electrical wiring and electrical layout drawing",
                "Load estimation and distribution board plan for a residential building",
                "Types of industrial load and power supply requirements",
                "Electrical energy conservation in buildings and industries",
            ]
        },
        "Power electronics": {
            "topics": [
                "Thyristor, Silicon Controller Rectifier, Diac, Triac",
                "Uninterrupted Power Supply (UPS), Switched Mode Power Supply",
                "DC-DC converter and inverter",
            ]
        },
        "Power system analysis": {
            "topics": ["Fault Analysis, Load flow analysis, Power system stability"]
        },
    },
    "Project Planning, Design and Implementation (AALL10)": {
        "Engineering drawings and its concepts": {
            "topics": [
                "Fundamentals of standard drawing sheets",
                "Dimensions, scale, and line diagram",
                "Orthographic projection, isometric projection/view",
                "Pictorial views and sectional drawing",
            ]
        },
        "Engineering Economics": {
            "topics": [
                "Understanding project cash flow",
                "Discount rate, interest, and time value of money",
                "Methodologies for engineering economics analysis (Discounted Payback Period, NPV, IRR & MARR)",
                "Comparison of alternatives",
                "Depreciation and taxation system in Nepal",
            ]
        },
        "Project planning and scheduling": {
            "topics": [
                "Project classifications and life cycle phases",
                "Project planning process",
                "Project scheduling (bar chart, CPM, PERT)",
                "Resources levelling and smoothing",
                "Monitoring, evaluation, and controlling",
            ]
        },
        "Project management": {
            "topics": [
                "Information system",
                "Project risk analysis and management",
                "Project financing and tender process",
                "Contract management",
            ]
        },
        "Engineering professional practice": {
            "topics": [
                "Environment and society",
                "Professional ethics and regulatory environment",
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
                "content": """As an engineering tutor of Electrical And Electronics Engineering, your task is to provide detailed explanations of requested engineering topics. Your goal is to cover all crucial aspects of the topic, incorporating relevant examples to enhance understanding. Aim to address important, tricky or confusing points that might be asked in multiple-choice questions for knowledge assessment. Remember that you are tutoring an engineering background student, so cover everything in detail and don't miss anything.

Your responses should be clear and detailed, offering thorough explanations that enhance the reader's understanding of the topic. Additionally, be prepared to provide JSON responses when explicitly requested by the user, ensuring that any single backward slashes in the JSON are replaced with two backslashes to ensure correct display when extracted and rendered in the UI using streamlit. Otherwise, when responding besides JSON, respond as it is.

Please ensure that your explanations are informative and well-structured, allowing for a detailed grasp of the engineering topics.""",
            },
            {"role": "user", "content": query},
        ],
        model=model_name or "llama-3.1-70b-versatile",
        # model=model_name or "Llama-3.1-8b-Instant",
        temperature=temperature,
        top_p=1,
        max_tokens=7500,
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
    st.title("NEC Study: ELECTRICAL AND ELECTRONICS ENGINEERING")

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
        "mixtral-8x7b-32768",
        "Llama-3.1-8b-Instant",
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
                f"""Based on the following lesson content from Engineering study materials, generate exactly 15 multiple-choice questions (MCQs) along with their respective answers for the topic {selected_topic} from lesson {selected_lesson}. Make sure that only one option is correct while other options are wrong but seems quite similar to the actual option. This is to prepare engineering completed students for top level MCQ assessments to be taken by Engineering council. Each question from MCQ carries either 1 or 2 marks. For 2 marks question, there may be numerical type MCQ or coding related MCQ only if the lesson topic is related to such. Strictly use the given JSON Format below as your response format.
                
                # Lesson Content: {retrieve_content(selected_topic, selected_lesson)}
                
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

    # st.error("Maximum retry attempts reached with Groq models. Switching...")

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
    #     st.error("Maximum retry attempts reached with Github models.")
    # st.error("Maximum retry attempts reached with all models.")
    st.error("Failed to generate assessment after several attempts.")
    st.error("Please retry generating again...")
    return None


def generate_feedback(question, student_answer, actual_answer):
    # Construct the prompt to generate feedback
    prompt = f"""
    Based on the following:
    - Question: {question}
    - Student's Answer: {student_answer}
    - Correct Answer: {actual_answer}
    
    Provide proper feedback offering why student's answer is incorrect and brief explanation of the right answer.
    """
    # First, try using Groq models
    try:
        # print(f"Generating feedback using Groq models.")
        return generate_dynamic_content_groq(
            query=prompt, model_name="Llama-3.1-8b-Instant", temperature=0.5
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
                "content": "You are a helpful tutor for electrical and electronics engineering student from Nepal. Skip Introductions and give brief and correct answer or solution to the query of student to help them have clear concepts on their asked question. They ask questions mostly for understanding multiple choice type of questions. Answer accrodingly.",
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
