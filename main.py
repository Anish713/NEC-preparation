import json
import datetime
import sqlite3
import streamlit as st
from groq import Groq

# from openai import OpenAI

# from dotenv import load_dotenv
# load_dotenv()
DB_PATH = "generated_content.db"

## NEC Syllabus for computer Engineering
course_structure = {
    "Concept of Basic Electrical and Electronics Engineering (AExE01)": {
        "Basic Concept": {
            "topics": [
                "Ohm's law + electric voltage + current + power and energy",
                "Conducting and insulating materials",
                "Series and parallel electric circuits + star-delta and delta-star conversion",
                "Kirchhoff’s law + linear and non-linear circuit + bilateral and unilateral circuits",
                "Active and passive circuits",
            ]
        },
        "Network Theorems": {
            "topics": [
                "Superposition theorem + Thevenin's theorem + Norton's theorem",
                "Maximum power transfer theorem",
                "R-L, R-C, R-L-C circuits + resonance in AC series and parallel circuit",
                "Active and reactive power",
            ]
        },
        "Alternating Current Fundamentals": {
            "topics": [
                "Principle of generation of alternating voltages and currents + equations and waveforms",
                "Average, peak and RMS values",
                "Three phase system",
            ]
        },
        "Semiconductor Devices": {
            "topics": [
                "Semiconductor diode + characteristics",
                "BJT configuration and biasing + small and large signal model",
                "Working principle and application of MOSFET and CMOS",
            ]
        },
        "Signal Generator": {
            "topics": [
                "Basic principles of oscillator",
                "RC, LC and crystal oscillators circuits",
                "Waveform generators",
            ]
        },
        "Amplifiers": {
            "topics": [
                "Classification of output stages: Class A, Class B, Class AB",
                "Biasing the Class AB stage",
                "Power BJTs + Transformer-coupled push-pull stages",
                "Tuned amplifiers + op-amps",
            ]
        },
    },
    "Digital Logic and Microprocessor (AExE02)": {
        "Digital Logic": {
            "topics": [
                "Number systems + logic levels + logic gates",
                "Boolean algebra",
                "Sum-of-Products method + Product-of-Sums method",
                "Truth Table to Karnaugh Map",
            ]
        },
        "Combinational and Arithmetic Circuits": {
            "topics": [
                "Multiplexers + Demultiplexers + Decoder + Encoder",
                "Binary addition + Binary subtraction",
                "Operations on unsigned and signed binary numbers",
            ]
        },
        "Sequential Logic Circuit": {
            "topics": [
                "RS Flip-Flops + Gated Flip-Flops + Edge Triggered Flip-Flops + Master-Slave Flip-Flops",
                "Types of registers",
                "Applications of shift registers",
                "Asynchronous counters + Synchronous counters",
            ]
        },
        "Microprocessor": {
            "topics": [
                "Internal architecture and features of microprocessor",
                "Assembly language programming",
            ]
        },
        "Microprocessor System": {
            "topics": [
                "Memory device classification and hierarchy",
                "Interfacing I/O and memory + parallel interface",
                "Introduction to programmable peripheral interface (PPI)",
                "Serial interface + synchronous and asynchronous transmission + serial interface standards",
                "Introduction to Direct Memory Access (DMA) and DMA controllers",
            ]
        },
        "Interrupt Operations": {
            "topics": ["Interrupt + Interrupt Service Routine", "Interrupt processing"]
        },
    },
    "Programming Language and Its Applications (ACtE03)": {
        "Introduction to C Programming": {
            "topics": [
                "C tokens + operators + formatted/unformatted input/output",
                "Control statements + looping",
                "User-defined functions + recursive functions",
                "Array (1-D, 2-D, multi-dimensional) + string manipulations",
            ]
        },
        "Pointers, Structure and Data Files in C Programming": {
            "topics": [
                "Pointer arithmetic + pointer and array + passing pointer to function",
                "Structure vs union + array of structure + passing structure to function + structure and pointer",
                "Input/output operations on files",
                "Sequential and random access to file",
            ]
        },
        "C++ Language Constructs with Objects and Classes": {
            "topics": [
                "Namespace + function overloading + inline functions + default argument",
                "Pass/return by reference + class and object introduction + access specifiers",
                "Objects and member access + defining member function + constructor and its types + destructor",
                "Dynamic memory allocation for objects + object array + this pointer + static data member + static function",
                "Constant member functions + constant objects + friend function + friend classes",
            ]
        },
        "Features of Object-Oriented Programming": {
            "topics": [
                "Operator overloading (unary, binary) + data conversion",
                "Inheritance (single, multiple, multilevel, hybrid, multipath)",
                "Constructor/destructor in single/multilevel inheritance",
            ]
        },
        "Pure Virtual Function and File Handling": {
            "topics": [
                "Virtual function + dynamic binding",
                "Defining, opening, and closing a file + input/output operations on files",
                "Error handling during input/output operations",
                "Stream class hierarchy for console input/output",
                "Unformatted/Formatted input/output with ios member functions + flags + formatting with manipulators",
            ]
        },
        "Generic Programming and Exception Handling": {
            "topics": [
                "Function template + overloading function template + class template",
                "Standard Template Library (containers, algorithms, iterators)",
                "Exception handling constructs (try, catch, throw) + multiple exception handling",
                "Rethrowing exception + catching all exceptions + exception with arguments",
                "Exception specification for function + handling uncaught and unexpected exceptions",
            ]
        },
    },
    "Computer Organization and Embedded System (ACtE04)": {
        "Control and Central Processing Units": {
            "topics": [
                "Control memory + addressing sequencing + computer configuration",
                "Microinstruction format + design of control unit",
                "CPU structure and function + arithmetic and logic unit",
                "Instruction formats + addressing modes + data transfer and manipulation",
                "RISC and CISC pipelining + parallel processing",
            ]
        },
        "Computer Arithmetic and Memory System": {
            "topics": [
                "Arithmetic and logical operations",
                "Memory hierarchy + internal and external memory",
                "Cache memory principles + elements of cache design",
                "Cache size + mapping function + replacement algorithm + write policy",
                "Memory write ability + storage permanence + composing memory",
            ]
        },
        "Input-Output Organization and Multiprocessor": {
            "topics": [
                "Peripheral devices + I/O modules + input-output interface",
                "Modes of transfer + direct memory access",
                "Characteristics of multiprocessors + interconnection structure",
                "Inter-processor communication and synchronization",
            ]
        },
        "Hardware-Software Design Issues on Embedded System": {
            "topics": [
                "Embedded systems overview + classification of embedded systems",
                "Custom single-purpose processor design + optimizing custom single-purpose processors",
                "Basic architecture + operation + programmer's view",
                "Development environment",
                "Application-specific instruction-set processors",
            ]
        },
        "Real-Time Operating and Control System": {
            "topics": [
                "Operating system basics + task + process + threads",
                "Multiprocessing + multitasking",
                "Task scheduling + task synchronization",
                "Device drivers",
                "Open-loop and close-loop control system overview + control",
            ]
        },
        "Hardware Descriptions Language and IC Technology": {
            "topics": [
                "VHDL overview + overflow and data representation using VHDL",
                "Design of combinational and sequential logic using VHDL",
                "Pipelining using VHDL",
            ]
        },
    },
    "Concept of Computer Network and Network Security System (ACtE05)": {
        "Introduction to Computer Networks and Physical Layer": {
            "topics": [
                "Networking model + protocols and standards",
                "OSI model + TCP/IP model",
                "Networking devices (hubs, bridges, switches, routers)",
                "Transmission media",
            ]
        },
        "Data Link Layer": {
            "topics": [
                "Services + error detection and corrections + flow control",
                "Data link protocol + multiple access protocols",
                "LAN addressing + ARP (Address Resolution Protocol)",
                "Ethernet, IEEE 802.3 (Ethernet) + 802.4 (Token Bus) + 802.5 (Token Ring)",
                "CSMA/CD + wireless LANs + PPP (Point to Point Protocol) + wide area protocols",
            ]
        },
        "Network Layer": {
            "topics": [
                "Addressing (Internet address + classful address) + subnetting",
                "Routing protocols (RIP, OSPF, BGP, Unicast, Multicast)",
                "Routing algorithms (shortest path algorithm, flooding, distance vector routing, link state routing)",
                "ARP, RARP, IP, ICMP",
                "IPv6 (Packet formats, extension headers, transition from IPv4 to IPv6, multicasting)",
            ]
        },
        "Transport Layer": {
            "topics": [
                "Transport service + transport protocols",
                "Port and socket + connection establishment and release",
                "Flow control + buffering + multiplexing + de-multiplexing",
                "Congestion control algorithm",
            ]
        },
        "Application Layer": {
            "topics": [
                "Web (HTTP & HTTPS) + file transfer (FTP, PuTTY, Win SCP)",
                "Electronic mail + DNS + P2P applications",
                "Socket programming + application server concept",
                "Traffic analyzer concept (MRTG, PRTG, SNMP, packet tracer, Wireshark)",
            ]
        },
        "Network Security": {
            "topics": [
                "Types of computer security + types of security attacks",
                "Principles of cryptography + RSA algorithm + digital signatures",
                "Securing email (PGP) + securing TCP connections (SSL)",
                "Network layer security (IPsec, VPN) + securing wireless LANs (WEP)",
                "Firewalls",
            ]
        },
    },
    "Theory of Computation and Computer Graphics (ACtE06)": {
        "Introduction to Finite Automata": {
            "topics": [
                "Finite automata + finite state machine",
                "Equivalence of DFA and NDFA",
                "Minimization of finite state machines",
                "Regular expressions + equivalence of regular expressions and finite automata",
                "Pumping lemma for regular language",
            ]
        },
        "Introduction to Context Free Language": {
            "topics": [
                "Context free grammar (CFG) + derivative trees (bottom-up + top-down approach)",
                "Parse tree + construction + ambiguous grammar",
                "Chomsky Normal Form (CNF) + Greibach Normal Form (GNF) + Backus-Naur Form (BNF)",
                "Push down automata + equivalence of context free language and PDA",
                "Pumping lemma for context free language + properties of context free language",
            ]
        },
        "Turing Machine": {
            "topics": [
                "Introduction to Turing machines (TM) + notations of Turing machine",
                "Turing machine as a language recognizer + computing function",
                "Turing machine with multiple tracks + tapes + non-deterministic Turing machines",
                "Universal Turing machine + Church-Turing thesis",
                "Computational complexity + time and space complexity + intractability + reducibility",
            ]
        },
        "Introduction to Computer Graphics": {
            "topics": [
                "Overview of computer graphics",
                "Graphics hardware (display technology, architecture of raster-scan + vector displays)",
                "Display processors + output and input devices",
                "Graphics software + software standards",
            ]
        },
        "Two-Dimensional Transformation": {
            "topics": [
                "2D translation + rotation + scaling + reflection + shear transformation",
                "2D composite transformation",
                "2D viewing pipeline",
                "World to screen viewing transformation + clipping (Cohen Sutherland, Liang-Barsky)",
            ]
        },
        "Three-Dimensional Transformation": {
            "topics": [
                "3D translation + rotation + scaling + reflection + shear transformation",
                "3D composite transformation",
                "3D viewing pipeline",
                "Projection concepts (orthographic + parallel + perspective projection)",
            ]
        },
    },
    "Data Structures and Algorithm, Database System and Operating System (ACtE07)": {
        "Introduction to Data Structure, List, Linked Lists and Trees": {
            "topics": [
                "Data types, data structures, abstract data types + time and space analysis (Big O, Omega, Theta notations)",
                "Linear data structure (stack + queue implementation), stack application: infix to postfix conversion + evaluation of postfix expression",
                "Array implementation of lists + static and dynamic list structure",
                "Dynamic implementation of linked list (singly linked list, doubly linked list, circular linked list), basic operations on linked list",
                "Concept of tree + binary tree operations (search, insertion, deletion), tree traversals (pre-order, post-order, in-order), AVL balanced trees",
            ]
        },
        "Sorting, Searching, and Graphs": {
            "topics": [
                "Types of sorting (internal + external), insertion sort, selection sort, merge sort, radix sort, shell sort, heap sort",
                "Efficiency of sorting (Big O notation)",
                "Search techniques (sequential search, binary search, tree search), general search tree",
                "Hashing (hash function + hash tables, collision resolution technique)",
                "Graphs (undirected + directed), depth-first traversal, breadth-first traversal, minimum spanning trees, shortest-path algorithms (Dijkstra, greedy algorithm)",
            ]
        },
        "Introduction to Data Models, Normalization, and SQL": {
            "topics": [
                "Data abstraction + independence, schema + instances, ER model, attributes + keys",
                "Normal forms (1st, 2nd, 3rd, BCNF), functional dependencies, integrity + domain constraints",
                "DDL + DML commands, relational algebra, query optimization, query decomposition",
                "Query cost estimation + evaluation of expressions",
            ]
        },
        "Transaction Processing, Concurrency Control and Crash Recovery": {
            "topics": [
                "ACID properties + concurrent executions, serializability concept",
                "Lock-based protocols + deadlock handling + prevention",
                "Failure classification + recovery and atomicity",
                "Log-based recovery",
            ]
        },
        "Introduction to Operating System and Process Management": {
            "topics": [
                "Evolution + types of operating systems, OS components, structure + services",
                "Introduction to process, process states, control, threads, scheduling types",
                "Principles of concurrency, critical region, race condition, mutual exclusion, semaphores, mutex, message passing, monitors",
                "Classical problems of synchronization",
            ]
        },
        "Memory Management, File Systems and System Administration": {
            "topics": [
                "Memory address + swapping, free memory space management, virtual memory management, demand paging",
                "Page replacement algorithms",
                "File system implementation, mapping file blocks on disk platter, fragmentation impact",
                "User account management + system administration tasks",
            ]
        },
    },
    "Software Engineering and Object-Oriented Analysis & Design (ACtE08)": {
        "Software Process and Requirements": {
            "topics": [
                "Software characteristics + quality attributes, software process models (Agile, V-Model, Iterative, Prototype, Big Bang)",
                "Computer-aided software engineering, functional + non-functional requirements",
                "User + system requirements, interface specification, software requirements documents",
                "Requirements elicitation + analysis, validation + management",
            ]
        },
        "Software Design": {
            "topics": [
                "Design process + concepts, design modes + heuristics, architectural design decisions",
                "System organization + modular decomposition styles, control styles",
                "Reference architectures + multiprocessor architecture",
                "Client-server + distributed object architectures, inter-organizational distributed computing",
                "Real-time software design + component-based software engineering",
            ]
        },
        "Software Testing, Cost Estimation, Quality Management, and Configuration Management": {
            "topics": [
                "Unit, integration, system, component + acceptance testing, test case design + automation",
                "Metrics for testing + algorithmic cost modeling",
                "Project duration + staffing, software quality assurance + formal technical reviews",
                "Statistical software quality assurance + a framework for software metrics",
                "Configuration management planning + change management, version + release management, CASE tools",
            ]
        },
        "Object-Oriented Fundamentals and Analysis": {
            "topics": [
                "Defining models + requirement process, use cases + object-oriented development cycle",
                "Unified Modeling Language, building conceptual model + adding associations and attributes",
                "Representation of system behavior",
            ]
        },
        "Object-Oriented Design": {
            "topics": [
                "Analysis to design, describing + elaborating use cases",
                "Collaboration diagrams, objects + patterns, determining visibility",
                "Class diagrams",
            ]
        },
        "Object-Oriented Design Implementation": {
            "topics": [
                "Programming + development process, mapping design to code",
                "Creating class definitions from design class diagrams",
                "Creating methods from collaboration diagrams, updating class definitions",
                "Classes in code + exception and error handling",
            ]
        },
    },
    "Artificial Intelligence and Neural Networks (ACtE09)": {
        "Introduction to AI and Intelligent Agents": {
            "topics": [
                "Concept of Artificial Intelligence + AI perspectives, history of AI, applications of AI, foundations of AI",
                "Introduction to agents, structure of intelligent agents, properties of intelligent agents",
                "PEAS description of agents, types of agents (simple reflexive, model based, goal based, utility based)",
                "Environment types (deterministic, stochastic, static, dynamic, observable, semi-observable, single agent, multi-agent)",
            ]
        },
        "Problem Solving and Searching Techniques": {
            "topics": [
                "Definition + problem as state space search, problem formulation, well-defined problems, constraint satisfaction problem",
                "Uninformed search techniques (depth first search, breadth first search, depth limited search, iterative deepening search, bidirectional search)",
                "Informed search techniques (greedy best first search, A* search, hill climbing, simulated annealing)",
                "Game playing + adversarial search techniques, mini-max search, alpha-beta pruning",
            ]
        },
        "Knowledge Representation": {
            "topics": [
                "Knowledge representations + mappings, approaches to knowledge representation, issues in knowledge representation",
                "Semantic nets, frames, propositional logic (syntax, semantics, formal logic-connectives, tautology, validity, well-formed formula, inference using resolution)",
                "Predicate logic (FOPL, syntax, semantics, quantification, rules of inference, unification, resolution refutation system)",
                "Bayes' rule + its use, Bayesian networks + reasoning in belief networks",
            ]
        },
        "Expert Systems and Natural Language Processing": {
            "topics": [
                "Expert systems, architecture of an expert system, knowledge acquisition",
                "Declarative knowledge vs procedural knowledge, development of expert systems",
                "Natural language processing terminology, natural language understanding + generation",
                "Steps of natural language processing, applications of NLP, NLP challenges",
                "Machine vision concepts + stages, robotics",
            ]
        },
        "Machine Learning": {
            "topics": [
                "Introduction to machine learning, concepts of learning",
                "Supervised, unsupervised, and reinforcement learning, inductive learning (decision tree)",
                "Statistical-based learning (Naive Bayes model), fuzzy learning + inference system",
                "Genetic algorithm (operators, encoding, selection algorithms, fitness function, parameters)",
            ]
        },
        "Neural Networks": {
            "topics": [
                "Biological neural networks vs artificial neural networks (ANN)",
                "McCulloch-Pitts neuron, mathematical model of ANN, activation functions",
                "Architectures of neural networks, perceptron, learning rate",
                "Gradient descent, delta rule, Hebbian learning, Adaline network",
                "Multilayer perceptron neural networks, backpropagation algorithm, Hopfield neural network",
            ]
        },
    },
    "Project Planning, Design and Implementation (AALL10)": {
        "Engineering Drawings and Its Concepts": {
            "topics": [
                "Fundamentals of standard drawing sheets",
                "Dimensions, scale, line diagram",
                "Orthographic projection, isometric projection/view",
                "Pictorial views, sectional drawing",
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
        "Project Planning and Scheduling": {
            "topics": [
                "Project classifications",
                "Project life cycle phases",
                "Project planning process",
                "Project scheduling (bar chart, CPM, PERT)",
                "Resources leveling and smoothing",
                "Monitoring, evaluation, and controlling",
            ]
        },
        "Project Management": {
            "topics": [
                "Information system",
                "Project risk analysis and management",
                "Project financing, tender and its process",
                "Contract management",
            ]
        },
        "Engineering Professional Practice": {
            "topics": [
                "Environment and society",
                "Professional ethics",
                "Regulatory environment",
                "Contemporary issues/problems in engineering",
                "Occupational health and safety",
                "Roles and responsibilities of Nepal Engineers Association (NEA)",
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
                "content": "As a Engineering tutor, your role is to provide detailed explanations of requested topics without the need for greetings. Your explanations should be detailed and thorough, incorporating examples where necessary to enhance understanding. Ensure that your responses are comprehensive and clear, aiming to thoroughly explain the given topic. Provide JSON response only when asked to respond with JSON. Additionally, when providing a JSON response, remember to use two backward slashes in place of any single backward slashes present in the JSON to ensure correct display when rendered in the UI using streamlit. Avoid dollar symbol in your response till possible.",
            },
            {"role": "user", "content": query},
        ],
        model=model_name or "Llama-3.1-8b-Instant",
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
            st.error(
                "There was an error decoding the JSON response. Please generate again."
            )
            st.text(f"Error: {e}")
            st.text(f"JSON string: {json_str}")
    else:
        # print("JSON brace count mismatch or JSON not started properly.")
        st.error("JSON brace count mismatch or JSON not started properly.")
        st.text(f"Response text: {response_text}")
        return None


create_db()


def course_dashboard():
    st.title("NEC Study Dashboard")

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
                st.write("### Practice Problems")

                problems_json = retrieve_problems(selected_unit, f"{selected_topic}")
                if regenerate_content or problems_json is None:
                    with st.spinner("Generating practice problems..."):
                        problems_json = generate_practice_problems_with_retries(
                            explanation, selected_unit
                        )
                        if problems_json:
                            store_problems(
                                selected_unit,
                                f"{selected_topic}",
                                json.dumps(problems_json),
                            )
                            st.sidebar.write("New problems generated")
                else:
                    st.sidebar.write("Using cached practice problems")

                if problems_json:
                    problems = (
                        json.loads(problems_json)
                        if isinstance(problems_json, str)
                        else problems_json
                    )
                    expander_state_key = f"{selected_unit}_{selected_topic}_expander"

                    with st.expander(
                        "Show Practice Problems",
                        expanded=st.session_state.get(expander_state_key, False),
                    ):
                        st.session_state[expander_state_key] = st.session_state.get(
                            expander_state_key, False
                        )
                        for i, problem in enumerate(problems.get("questions", [])):
                            st.markdown(
                                f":orange[**Question {i+1}:** {problem['question']}]",
                                unsafe_allow_html=True,
                            )
                            if st.button(
                                f"Show Answer to Q{i+1}", key=f"show_answer_{i+1}"
                            ):
                                with st.spinner(f"Showing answer to Question {i+1}..."):
                                    st.markdown(f"**Answer:** {problem['solution']}")

                else:
                    st.write(
                        "Practice sets not available! Please try generating again."
                    )

                if st.button("New Practice Sets", key="new_practice_sets"):
                    with st.spinner("Generating new practice problems..."):
                        explanation = retrieve_content(selected_unit, selected_topic)
                        problems_json = generate_practice_problems_with_retries(
                            explanation, selected_unit
                        )
                        if problems_json:
                            store_problems(
                                selected_unit,
                                f"{selected_topic}",
                                json.dumps(problems_json),
                            )
                            st.empty()
                            st.rerun()

                st.write("### MCQs")
                assessment_expander_key = f"{selected_unit}_assessment_expander"
                st.session_state.setdefault(assessment_expander_key, False)

                if st.button(f"Get MCQs", key="take_assessment"):
                    st.session_state[assessment_expander_key] = True

                if st.session_state[assessment_expander_key]:
                    with st.spinner("Generating assessment..."):
                        assessment_dashboard(selected_unit, selected_topic)


def generate_practice_problems_with_retries(explanation, selected_topic):
    max_retries = 1
    temperatures = [0.7, 0.3, 0.9]
    groq_models = [
        "Llama-3.1-8b-Instant",
        "llama3-8b-8192",
        "Llama-3.1-70b-Versatile",
        "gemma2-9b-it",
        "mixtral-8x7b-32768",
    ]
    github_models = ["gpt-4o-mini", "gpt-4o"]

    def try_generate(model_type, model_name, temperature):
        try:
            # st.write(
            #     f"Attempting generation with {model_type} model '{model_name}' at temperature {temperature}"
            # )
            problems_response = generate_dynamic_content(
                f"""Based on the following lesson content, generate 2 simple, 2 intermediate, and 2 complex questions along with their respective answers for the topic {selected_topic}. Strictly use the given JSON Format below as your response format.
                
                # Lesson Content: {explanation}
                
                # JSON Format:
                {{
                    "questions": [
                        {{
                            "difficulty": "simple",
                            "question": "Simple question 1",
                            "solution": "solution 1"
                        }},
                        {{
                            "difficulty": "simple",
                            "question": "Simple question 2",
                            "solution": "solution 2"
                        }},
                        {{
                            "difficulty": "intermediate",
                            "question": "Intermediate question 1",
                            "solution": "solution 1"
                        }},
                        {{
                            "difficulty": "intermediate",
                            "question": "Intermediate question 2",
                            "solution": "solution 2"
                        }},
                        {{
                            "difficulty": "complex",
                            "question": "Complex question 1",
                            "solution": "solution 1"
                        }},
                        {{
                            "difficulty": "complex",
                            "question": "Complex question 2",
                            "solution": "solution 2"
                        }}
                    ]
                }}""",
                model_type=model_type,
                model_name=model_name,
                temperature=temperature,
            )

            problems_json = extract_json_from_response(problems_response)
            return problems_json
        except Exception as e:
            st.error(f"Error occurred: {str(e)}. Retrying...")

    model_index = 0
    attempts = 0
    temperature_index = 0
    while model_index < len(groq_models):
        model_name = groq_models[model_index]
        temperature = temperatures[temperature_index]
        problems_json = try_generate("groq", model_name, temperature)
        if problems_json:
            return problems_json
        attempts += 1
        temperature_index += 1
        if temperature_index >= len(temperatures):
            temperature_index = 0
            model_index += 1
        if attempts >= max_retries * len(temperatures) * len(groq_models):
            break

    st.error(
        "Maximum retry attempts reached with Groq models. Switching to GitHub models."
    )

    model_index = 0
    attempts = 0
    temperature_index = 0
    while model_index < len(github_models):
        model_name = github_models[model_index]
        temperature = temperatures[temperature_index]
        problems_json = try_generate("github", model_name, temperature)
        if problems_json:
            return problems_json
        attempts += 1
        temperature_index += 1
        if temperature_index >= len(temperatures):
            temperature_index = 0
            model_index += 1
        if attempts >= max_retries * len(temperatures) * len(github_models):
            break

    st.error("Maximum retry attempts reached with all models.")

    st.error("Failed to generate practice problems after several attempts.")
    return None


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
            st.success(f"**You scored {score}/10**", icon="🔥")
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
            st.write(f"You scored {score}/10")
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


def main():
    st.sidebar.title("NEC Learning App")

    # Ensure database and tables are created
    create_db()
    course_dashboard()


if __name__ == "__main__":
    main()
