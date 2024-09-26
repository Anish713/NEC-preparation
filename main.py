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
    page_title="Computer Engineering NEC",
    page_icon="🖥️",
    layout="wide",
)

## NEC Syllabus for computer Engineering
course_structure = {
    "Concept of Basic Electrical and Electronics Engineering (AExE01)": {
        "Basic concept": {
            "topics": [
                "Ohm's law",
                "electric voltage current, power and energy, conducting and insulating materials",
                "Series and parallel electric circuits, start-delta and delta-star conversion",
                "Kirchhoff’s law",
                "linear and non-linear circuit, bilateral and unilateral circuits",
                "active and passive circuits",
            ]
        },
        "Network theorems": {
            "topics": [
                "concept of superposition theorem, Thevenin's theorem, Norton’s theorem, maximum power transfer theorem",
                "R-L, R-C, R-L-C circuits, resonance in AC series and parallel circuit",
                "active and reactive power",
            ]
        },
        "Alternating current fundamentals": {
            "topics": [
                "Principle of generation of alternating voltages and currents and their equations and waveforms",
                "average, peak and rms values",
                "Three phase system",
            ]
        },
        "Semiconductor devices": {
            "topics": [
                "Semiconductor diode and its characteristics",
                "BJT Configuration and biasing",
                "small and large signal model",
                "working principle and application of MOSFET and CMOS",
            ]
        },
        "Signal generator": {
            "topics": [
                "Basic Principles of Oscillator",
                "RC, LC and Crystal Oscillators Circuits",
                "Waveform generators",
            ]
        },
        "Amplifiers": {
            "topics": [
                "Classification of Output Stages",
                "Class A Output Stage",
                "Class B Output Stage",
                "Class AB Output Stage, Biasing the Class AB Stage",
                "Power BJTs, Transformer-Coupled Push-Pull Stages",
                "Tuned Amplifiers",
                "op-amps",
            ]
        },
    },
    "Digital Logic and Microprocessor (AExE02)": {
        "Digital logic": {
            "topics": [
                "Number Systems, Logic Levels, Logic Gates",
                "Boolean algebra",
                "Sum-of-Products Method, Product-of-Sums Method",
                "Truth Table to Karnaugh Map",
            ]
        },
        "Combinational and arithmetic circuits": {
            "topics": [
                "Multiplexers, Demultiplexers",
                "Decoder, Encoder",
                "Binary Addition, Binary Subtraction",
                "operation on Unsigned and Signed Binary Numbers",
            ]
        },
        "Sequential logic circuit": {
            "topics": [
                "RS Flip-Flops, Gated Flip-Flops, Edge Triggered Flip-Flops, Master-Slave Flip-Flops",
                "Types of Registers",
                "Applications of Shift Registers",
                "Asynchronous Counters, Synchronous Counters",
            ]
        },
        "Microprocessor": {
            "topics": [
                "Internal Architecture and Features of microprocessor",
                "Assembly Language Programming",
            ]
        },
        "Microprocessor system": {
            "topics": [
                "Memory Device Classification and Hierarchy",
                "Interfacing I/O and Memory Parallel Interface",
                "Introduction to Programmable Peripheral Interface (PPI)",
                "Serial Interface, Synchronous and Asynchronous Transmission",
                "Serial Interface Standards",
                "Introduction to Direct Memory Access (DMA) and DMA Controllers",
            ]
        },
        "Interrupt operations": {
            "topics": ["Interrupt, Interrupt Service Routine, and Interrupt Processing"]
        },
    },
    "Programming Language and Its Applications (ACtE03)": {
        "Introduction to C programming": {
            "topics": [
                "C Tokens, Operators",
                "Formatted/Unformatted Input/output",
                "Control Statements, Looping",
                "User-defined functions, Recursive functions",
                "Array (1-D, 2-D, Multi-dimensional), and String manipulations",
            ]
        },
        "Pointers, structure and data files in C programming": {
            "topics": [
                "Pointer Arithmetic",
                "Pointer and array, passing pointer to function",
                "Structure vs Union, array of structure, passing structure to function",
                "structure and pointer",
                "Input/output operations on files",
                "Sequential and Random Access to File",
            ]
        },
        "C++ language constructs with objects and classes": {
            "topics": [
                "Namespace, Function Overloading, Inline functions, Default Argument",
                "Pass/Return by reference",
                "introduction to Class and object, Access Specifiers",
                "Objects and the Member Access, Defining Member Function",
                "Constructor and its type, Destructor",
                "Dynamic memory allocation for objects and object array",
                "this Pointer, static Data Member and static Function",
                "Constant Member Functions and Constant Objects, Friend Function and Friend Classes",
            ]
        },
        "Features of object-oriented programming": {
            "topics": [
                "Operator overloading (unary, binary), data conversion",
                "Inheritance (single, multiple, multilevel, hybrid, multipath)",
                "constructor/destructor in single/multilevel inheritances",
            ]
        },
        "Pure virtual function and file handling": {
            "topics": [
                "Virtual function, dynamic binding",
                "defining opening and closing a file",
                "Input / Output operations on files",
                "Error handling during input/output operations",
                "Stream Class Hierarchy for Console Input /Output",
                "Unformatted Input /Output, Formatted Input /Output with ios Member functions and Flags",
                "Formatting with Manipulators",
            ]
        },
        "Generic programming and exception handling": {
            "topics": [
                "Function Template, Overloading Function Template",
                "Class Template, Function Definition of Class Template",
                "Standard Template Library (Containers, Algorithms, Iterators)",
                "Exception Handling Constructs (try, catch, throw)",
                "Multiple Exception Handling, Rethrowing Exception",
                "Catching All Exceptions, Exception with Arguments",
                "Exceptions Specification for Function, Handling Uncaught and Unexpected Exceptions",
            ]
        },
    },
    "Computer Organization and Embedded System (ACtE04)": {
        "Control and central processing units": {
            "topics": [
                "Control Memory, addressing sequencing",
                "Computer configuration",
                "Microinstruction Format",
                "Design of control unit",
                "CPU Structure and Function",
                "Arithmetic and logic Unit",
                "Instruction formats, addressing modes",
                "Data transfer and manipulation",
                "RISC and CISC",
                "Pipelining, parallel processing",
            ]
        },
        "Computer arithmetic and memory system": {
            "topics": [
                "Arithmetic and Logical operation",
                "The Memory Hierarchy",
                "Internal and External memory",
                "Cache memory principles",
                "Elements of Cache design - Cache size, Mapping function, Replacement algorithm, write policy, Number of caches",
                "Memory Write Ability and Storage Permanence",
                "Composing Memory",
            ]
        },
        "Input-Output organization and multiprocessor": {
            "topics": [
                "Peripheral devices",
                "I/O modules, Input-output interface",
                "Modes of transfer, Direct Memory access",
                "Characteristics of multiprocessors",
                "Interconnection Structure",
                "Inter-processor Communication and synchronization",
            ]
        },
        "Hardware-Software design issues on embedded system": {
            "topics": [
                "Embedded Systems overview",
                "Classification of Embedded Systems",
                "Custom Single-Purpose Processor Design",
                "Optimizing Custom Single-Purpose Processors",
                "Basic Architecture, Operation and Programmer’s View",
                "Development Environment",
                "Application-Specific Instruction-Set Processors",
            ]
        },
        "Real-Time operating and control system": {
            "topics": [
                "Operating System Basics",
                "Task, Process, and Threads",
                "Multiprocessing and Multitasking",
                "Task Scheduling, Task Synchronization",
                "Device Drivers",
                "Open-loop and Close-Loop control System overview",
                "Control",
            ]
        },
        "Hardware description language and IC technology": {
            "topics": [
                "VHDL Overview",
                "Overflow and data representation using VHDL",
                "Design of combinational and sequential logic using VHDL",
                "Pipelining using VHDL",
            ]
        },
    },
    "Concept of Computer Network and Network Security System (ACtE05)": {
        "Introduction to computer networks and physical layer": {
            "topics": [
                "Networking model",
                "Protocols and Standards",
                "OSI model and TCP/IP model",
                "Networking Devices (Hubs, Bridges, Switches, and Routers)",
                "Transmission media",
            ]
        },
        "Data link layer": {
            "topics": [
                "Services, Error Detection and Corrections",
                "Flow Control, Data Link Protocol",
                "Multiple access protocols",
                "LAN addressing and ARP (Address Resolution Protocol)",
                "Ethernet, IEEE 802.3 (Ethernet), 802.4 (Token Bus), 802.5 (Token Ring)",
                "CSMA/CD",
                "Wireless LANs",
                "PPP (Point to Point Protocol), Wide area protocols",
            ]
        },
        "Network layer": {
            "topics": [
                "Addressing (Internet address, classful address)",
                "Subnetting",
                "Routing Protocols (RIP, OSPF, BGP, Unicast and multicast routing protocols)",
                "Routing algorithms (shortest path algorithm, flooding, distance vector routing, link state routing)",
                "Routing Protocols (ARP, RARP, IP, ICMP)",
                "IPv6 (Packet formats, Extension headers, Transition from IPv4 to IPv6, Multicasting)",
            ]
        },
        "Transport layer": {
            "topics": [
                "The transport service",
                "Transport protocols",
                "Port and Socket",
                "Connection establishment & Connection release",
                "Flow control & buffering",
                "Multiplexing & de-multiplexing",
                "Congestion control algorithm",
            ]
        },
        "Application layer": {
            "topics": [
                "Web (HTTP & HTTPS)",
                "File Transfer (FTP, PuTTY, Win SCP)",
                "Electronic Mail",
                "DNS, P2P Applications",
                "Socket Programming",
                "Application server concept",
                "Concept of traffic analyzer (MRTG, PRTG, SNMP, Packet tracer, Wireshark)",
            ]
        },
        "Network security": {
            "topics": [
                "Types of Computer Security",
                "Types of Security Attacks",
                "Principles of cryptography",
                "RSA Algorithm",
                "Digital Signatures",
                "Securing e-mail (PGP)",
                "Securing TCP connections (SSL)",
                "Network layer security (IPsec, VPN)",
                "Securing wireless LANs (WEP)",
                "Firewalls",
            ]
        },
    },
    "Theory of Computation and Computer Graphics (ACtE06)": {
        "Introduction to finite automata": {
            "topics": [
                "Introduction to Finite Automata and Finite State Machine",
                "Equivalence of DFA and NDFA",
                "Minimization of Finite State Machines",
                "Regular Expressions",
                "Equivalence of Regular Expression and Finite Automata",
                "Pumping lemma for regular language",
            ]
        },
        "Introduction to context free language": {
            "topics": [
                "Introduction to Context Free Grammar (CFG)",
                "Derivative trees (Bottom-up and Top-down approach, Leftmost and Rightmost, Language of a grammar)",
                "Parse tree and its construction",
                "Ambiguous grammar",
                "Chomsky Normal Form (CNF)",
                "Greibach Normal Form (GNF)",
                "Backus-Naur Form (BNF)",
                "Push down automata",
                "Equivalence of context free language and PDA",
                "Pumping lemma for context free language",
                "Properties of context free Language",
            ]
        },
        "Turing machine": {
            "topics": [
                "Introduction to Turing Machines (TM)",
                "Notations of Turing Machine",
                "Acceptance of a string by a Turing Machines",
                "Turing Machine as a Language Recognizer",
                "Turing Machine as a Computing Function",
                "Turing Machine as an enumerator of strings of a language",
                "Turing Machine with Multiple Tracks",
                "Turing Machine with Multiple Tapes",
                "Non-Deterministic Turing Machines",
                "Church-Turing Thesis",
                "Universal Turing Machine for encoding of Turing Machine",
                "Computational Complexity",
                "Time and Space complexity of a Turing Machine",
                "Intractability, Reducibility",
            ]
        },
        "Introduction to computer graphics": {
            "topics": [
                "Overview of Computer Graphics",
                "Graphics Hardware (Display Technology, Architecture of Raster-Scan Displays, Vector Displays, Display Processors, output device and Input Devices)",
                "Graphics Software and Software standards",
            ]
        },
        "Two-dimensional transformation": {
            "topics": [
                "Two-dimensional translation, rotation, scaling, reflection, shear transformation",
                "2D composite transformation",
                "2D viewing pipeline",
                "World to screen viewing transformation and clipping (Cohen Sutherland line clipping, Liang-Barsky Line Clipping)",
            ]
        },
        "Three-dimensional transformation": {
            "topics": [
                "Three-dimensional translation, rotation, scaling, reflection, shear transformation",
                "3D composite transformation",
                "3D viewing pipeline",
                "Projection concepts (Orthographic, parallel, perspective projection)",
            ]
        },
    },
    "Data Structures and Algorithm, Database System and Operating System (ACtE07)": {
        "Introduction to data structure, list, linked lists and trees": {
            "topics": [
                "Data types, data structures and abstract data types",
                "Time and space analysis of algorithms (Big O, Omega and Theta notations)",
                "Linear data structure (Stack and queue implementation)",
                "Stack application: infix to postfix conversion, evaluation of postfix expression",
                "Array implementation of lists",
                "Stack and Queues as list",
                "Static and dynamic list structure",
                "Dynamic implementation of linked list",
                "Types of Linked list: Singly Linked list, Doubly Linked list, Circular Linked list",
                "Basic operations on Linked list: creation, insertion, and deletion of nodes",
                "Doubly linked lists and its applications",
                "Concept of Tree, Operation in Binary tree",
                "Tree search, insertion/deletions in Binary Tree",
                "Tree traversals (pre-order, post-order and in-order)",
                "Height, level and depth of a tree",
                "AVL balanced trees",
            ]
        },
        "Sorting, searching, and graphs": {
            "topics": [
                "Types of sorting: internal and external",
                "Insertion and selection sort",
                "Exchange sort",
                "Merge and Radix sort",
                "Shell sort",
                "Heap sort as a priority queue",
                "Big O notation and Efficiency of sorting",
                "Search technique: Sequential search, Binary search and Tree search",
                "General search tree",
                "Hashing: Hash function and hash tables, Collision resolution technique",
                "Undirected and Directed Graphs",
                "Representation of Graph, Transitive closure of graph",
                "Warshall’s algorithm",
                "Depth First Traversal and Breadth First Traversal of Graph",
                "Topological sorting (Depth first, Breadth first)",
                "Minimum spanning trees (Prim’s, Kruskal’s and Round-Robin algorithms)",
                "Shortest-path algorithm (Greedy algorithm, Dijkstra’s Algorithm)",
            ]
        },
        "Introduction to data models, normalization, and SQL": {
            "topics": [
                "Data Abstraction and Data Independence",
                "Schema and Instances",
                "E-R Model, Strong and Weak Entity Sets",
                "Attributes and Keys, E-R Diagram",
                "Different Normal Forms (1st, 2nd, 3rd, BCNF)",
                "Functional Dependencies",
                "Integrity Constraints and Domain Constraints",
                "Relations (Joined, Derived)",
                "Queries under DDL and DML Commands",
                "Views, Assertions and Triggering",
                "Relational Algebra",
                "Query Cost Estimation",
                "Query Operations, Evaluation of Expressions",
                "Query Optimization and Query Decomposition",
            ]
        },
        "Transaction processing, concurrency control and crash recovery": {
            "topics": [
                "ACID properties",
                "Concurrent Executions",
                "Serializability Concept",
                "Lock based Protocols",
                "Deadlock handling and Prevention",
                "Failure Classification",
                "Recovery and Atomicity",
                "Log-based Recovery",
            ]
        },
        "Introduction to Operating System and process management": {
            "topics": [
                "Evolution of Operating System",
                "Type of Operating System",
                "Operating System Components",
                "Operating System Structure",
                "Operating System Services",
                "Introduction to Process, Process description",
                "Process states, Process control",
                "Threads, Processes and Threads",
                "Types of scheduling",
                "Principles of Concurrency",
                "Critical Region, Race Condition",
                "Mutual Exclusion, Semaphores and Mutex",
                "Message Passing, Monitors",
                "Classical Problems of Synchronization",
            ]
        },
        "Memory management, file systems and system administration": {
            "topics": [
                "Memory address",
                "Swapping and Managing Free Memory Space",
                "Virtual Memory Management, Demand Paging",
                "Performance, and Page Replacement Algorithms",
                "Introduction to File, Directory and File Paths",
                "File System Implementation",
                "Impact of Allocation Policy on Fragmentation",
                "Mapping File Blocks on The Disk Platter",
                "File System Performance",
                "Administration Tasks, User Account Management",
                "Start and Shutdown Procedures",
            ]
        },
    },
    "Software Engineering and Object-Oriented Analysis & Design (ACtE08)": {
        "Software process and requirements": {
            "topics": [
                "Software characteristics",
                "Software quality attributes",
                "Software process model (Agile Model, V-Model, Iterative Model, Prototype Model, Big Bang Model)",
                "Computer-aided software engineering",
                "Functional and non-functional requirements",
                "User requirements",
                "System requirement",
                "Interface specification",
                "The software requirements documents",
                "Requirement’s elicitation and analysis",
                "Requirement’s validation and management",
            ]
        },
        "Software design": {
            "topics": [
                "Design process",
                "Design Concepts",
                "Design Mode",
                "Design Heuristic",
                "Architectural design decisions",
                "System organization",
                "Modular decomposition styles",
                "Control styles",
                "Reference architectures",
                "Multiprocessor architecture",
                "Client-server architectures",
                "Distributed object architectures",
                "Inter-organizational distributed computing",
                "Real-time software design",
                "Component-based software engineering",
            ]
        },
        "Software testing, cost estimation, quality management, and configuration management": {
            "topics": [
                "Unit Testing",
                "Integration testing",
                "System testing",
                "Component testing",
                "Acceptance Testing",
                "Test case design",
                "Test automation",
                "Metrics for testing",
                "Algorithmic cost modeling",
                "Project duration and staffing",
                "Software quality assurance",
                "Formal technical reviews",
                "Formal approaches to SQA",
                "Statistical software quality assurance",
                "A framework for software metrics",
                "Matrices for analysis and design model",
                "ISO standards",
                "CMMI",
                "SQA plan",
                "Configuration management planning",
                "Change management",
                "Version and release management",
                "CASE tools for configuration management",
            ]
        },
        "Object-oriented fundamentals and analysis": {
            "topics": [
                "Defining Models",
                "Requirement Process",
                "Use Cases",
                "Object Oriented Development Cycle",
                "Unified Modeling Language",
                "Building Conceptual Model",
                "Adding Associations and Attributes",
                "Representation of System Behavior",
            ]
        },
        "Object-oriented design": {
            "topics": [
                "Analysis to Design",
                "Describing and Elaborating Use Cases",
                "Collaboration Diagram",
                "Objects and Patterns",
                "Determining Visibility",
                "Class Diagram",
            ]
        },
        "Object-oriented design implementation": {
            "topics": [
                "Programming and Development Process",
                "Mapping Design to Code",
                "Creating Class Definitions from Design Class Diagrams",
                "Creating Methods from Collaboration Diagram",
                "Updating Class Definitions",
                "Classes in Code",
                "Exception and Error Handling",
            ]
        },
    },
    "Artificial Intelligence and Neural Networks (ACtE09)": {
        "Introduction to AI and intelligent agent": {
            "topics": [
                "Concept of Artificial Intelligence",
                "AI Perspectives",
                "History of AI",
                "Applications of AI",
                "Foundations of AI",
                "Introduction of agents",
                "Structure of Intelligent agent",
                "Properties of Intelligent Agents",
                "PEAS description of Agents",
                "Types of Agents (Simple Reflexive, Model Based, Goal Based, Utility Based)",
                "Environment Types (Deterministic, Stochastic, Static, Dynamic, Observable, Semi-observable, Single Agent, Multi Agent)",
            ]
        },
        "Problem solving and searching techniques": {
            "topics": [
                "Definition",
                "Problem as a state space search",
                "Problem formulation",
                "Well-defined problems",
                "Constraint satisfaction problem",
                "Uninformed search techniques (Depth First Search, Breadth First Search, Depth Limited Search, Iterative Deepening Search, Bidirectional Search)",
                "Informed Search (Greedy Best first search, A* search, Hill Climbing, Simulated Annealing)",
                "Game playing",
                "Adversarial search techniques (Mini-max Search, Alpha-Beta Pruning)",
            ]
        },
        "Knowledge representation": {
            "topics": [
                "Knowledge representations and Mappings",
                "Approaches to Knowledge Representation",
                "Issues in Knowledge Representation",
                "Semantic Nets",
                "Frames",
                "Propositional Logic (PL)",
                "Predicate Logic (FOPL)",
                "Bayes' Rule and its use",
                "Bayesian Networks",
                "Reasoning in Belief Networks",
            ]
        },
        "Expert system and natural language processing": {
            "topics": [
                "Expert Systems",
                "Architecture of an expert system",
                "Knowledge acquisition",
                "Declarative knowledge vs Procedural knowledge",
                "Development of Expert Systems",
                "Natural Language Processing Terminology",
                "Natural Language Understanding and Generation",
                "Steps of Natural Language Processing",
                "Applications of NLP",
                "NLP Challenges",
                "Machine Vision Concepts",
                "Machine Vision Stages",
                "Robotics",
            ]
        },
        "Machine learning": {
            "topics": [
                "Introduction to Machine Learning",
                "Concepts of Learning",
                "Supervised, Unsupervised and Reinforcement Learning",
                "Inductive learning (Decision Tree)",
                "Statistical-based Learning (Naive Bayes Model)",
                "Fuzzy learning",
                "Fuzzy Inferences System",
                "Fuzzy Inference Methods",
                "Genetic Algorithm (Genetic Algorithm Operators, Genetic Algorithm Encoding, Selection Algorithms, Fitness function, Genetic Algorithm Parameters)",
            ]
        },
        "Neural networks": {
            "topics": [
                "Biological Neural Networks Vs. Artificial Neural Networks (ANN)",
                "McCulloch-Pitts Neuron",
                "Mathematical Model of ANN",
                "Activation functions",
                "Architectures of Neural Networks",
                "The Perceptron",
                "The Learning Rate",
                "Gradient Descent",
                "The Delta Rule",
                "Hebbian learning",
                "Adaline network",
                "Multilayer Perceptron Neural Networks",
                "Backpropagation Algorithm",
                "Hopfield Neural Network",
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
                "Discount rate",
                "Interest and time value of money",
                "Basic methodologies for engineering economics analysis (Discounted Payback Period, NPV, IRR & MARR)",
                "Comparison of alternatives",
                "Depreciation system",
                "Taxation system in Nepal",
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


def generate_dynamic_content_groq(query, model_name=None, temperature=0.7):
    client = Groq()
    stream = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """As an engineering tutor, your task is to provide detailed explanations of requested engineering topics. Your goal is to cover all crucial aspects of the topic, incorporating relevant examples to enhance understanding. Aim to address important points that might be asked in multiple-choice questions for knowledge assessment. Remember that you are tutoring an engineering background student, so go in detail and don't miss anything. Also, you may utilize latex capabilities to express equations when needed.

Your responses should be clear and detailed, offering thorough explanations that enhance the reader's understanding of the topic. Additionally, be prepared to provide JSON responses when explicitly requested by the user, ensuring that any single backward slashes in the JSON are replaced with two backslashes to ensure correct display when extracted and rendered in the UI using streamlit. Otherwise, when responding besides JSON, respond as it is. Reminder: Don't provided JSON format response unless requested by user.

Please ensure that your explanations are informative and well-structured, allowing for a comprehensive grasp of the engineering topics.""",
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


def generate_dynamic_content_github(query, model_name=None, temperature=0.7):
    pass


def generate_dynamic_content(
    query, model_type="groq", model_name=None, temperature=0.8
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
    st.title("NEC Study Dashboard: COMPUTER ENGINEERING")

    st.markdown(
        """
        <style>
        /* Add borders to the selectbox container */
        .st-emotion-cache-sy3zga div[role="combobox"] {
            border: 2px solid #ddd !important;  /* Add a visible border */
            padding: 5px !important;  /* Add padding inside the box */
            border-radius: 5px;  /* Round the edges slightly */
        }

        /* Add borders and improve visibility for each option */
        .st-emotion-cache-sy3zga div[role="combobox"] > div {
            border-bottom: 1px solid #ccc !important;  /* Border between options */
            padding: 5px !important;  /* Ensure there's space inside each option */
        }

        /* Prevent selected option from overlapping */
        .st-emotion-cache-sy3zga div[role="combobox"] > div {
            white-space: pre-wrap !important;  /* Wrap long text */
            overflow-wrap: break-word !important;  /* Break long words */
            height: auto !important;  /* Adjust height dynamically */
        }

        /* Ensure long text doesn’t overlap other options */
        .st-emotion-cache-sy3zga {
            overflow: visible !important;  /* Prevent clipping */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

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
                        set_scroll_position()

                else:
                    st.sidebar.write("Using cached content")
                    set_scroll_position()

                st.write(explanation, unsafe_allow_html=True)
                set_scroll_position()

                # st.write("### MCQs")
                assessment_expander_key = f"{selected_unit}_assessment_expander"
                st.session_state.setdefault(assessment_expander_key, True)
                set_scroll_position()

                # if st.button(f"Get MCQs", key="take_assessment"):
                #     st.session_state[assessment_expander_key] = True

                if st.session_state[assessment_expander_key]:
                    set_scroll_position()

                    assessment_dashboard(selected_unit, selected_topic)
                    set_scroll_position()


def generate_practice_problems_with_retries(explanation, selected_topic):
    pass


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
                f"""Based on the following lesson content from Engineering study materials, generate exactly 15 multiple-choice questions (MCQs) along with their respective answers for the topic {selected_topic} from lesson {selected_lesson}. Make sure that only one option is correct while other options are wrong but seems quite similar to the actual option. This is to prepare engineering completed students for top level MCQ assessments to be taken by Engineering council. Each question from MCQ carries either 1 or 2 marks. For 2 marks question, there may be numerical type MCQ or coding related MCQ only if the lesson topic is related to such. Provide me a json response. Strictly use the given JSON Format as your response format.
                
                # Lesson Content: {retrieve_content(selected_topic, selected_lesson)}
                
                ## Reminder: Strictly use the given JSON Format below as your response format. Use double backslashes instead of one backslash for if needed to use streamlit expressions inside your JSON response.
                # JSON Format:
                {{
                    "questions": [
                        {{
                            "question": "Question 1 [mark]",
                            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                            "correct_answer": "Correct option for  Question 1"

                        }},
                        {{
                            "question": "Question 2 [mark]",
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
            query=prompt, model_name="llama-3.1-70b-versatile", temperature=0.7
        )
    except Exception as e_groq:
        # print(f"Error using Groq model: {e_groq}")
        pass


def assessment_dashboard(selected_topic, selected_lesson):
    st.header(f"MCQs: {selected_lesson}")

    # Retrieve assessment from database
    assessment_json = retrieve_assessment(selected_topic, f"{selected_lesson}")

    if assessment_json is None:
        with st.spinner("Generating MCQs..."):
            set_scroll_position()

            assessment_json = generate_assessment_with_retries(
                selected_topic, selected_lesson
            )
            store_assessment(
                selected_topic,
                f"{selected_lesson}",
                json.dumps(assessment_json),
            )
            set_scroll_position()

            # st.rerun()
            set_scroll_position()

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
        total_ques = i + 1
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

        pass_threshold = 2
        if score >= pass_threshold:
            st.success(f"**You scored {score}/{total_ques}**", icon="🔥")
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
            st.warning(f"You scored {score}/{total_ques}. REVISE AGAIN!!!", icon="👀")
            st.write(f"You need to score at least {pass_threshold} to check feedback.")
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


def set_scroll_position():
    # JavaScript snippet to maintain scroll position at the top
    st.markdown(
        """
        <script>
        window.onload = function() {
            window.scrollTo(0, 0);  // Scroll to top
        }
        </script>
        """,
        unsafe_allow_html=True,
    )


def stream_response(query):
    client = Groq()

    # Use shared history + the new user query
    stream = client.chat.completions.create(
        messages=st.session_state.shared_messages
        + [{"role": "user", "content": query}],
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
    set_scroll_position()


def main():
    st.sidebar.title("NEC Learning App")

    # Ensure database and tables are created
    create_db()
    course_dashboard()
    # Initialize shared message history if not present
    if "shared_messages" not in st.session_state:
        st.session_state.shared_messages = []

    # Function to limit history to last 3 full conversations
    def trim_conversation():
        messages = st.session_state.shared_messages
        conversation_pairs = [(i, i + 1) for i in range(0, len(messages) - 1, 2)]
        if len(conversation_pairs) > 3:
            st.session_state.shared_messages = messages[
                -6:
            ]  # Last 3 pairs (6 messages)

    # Prevent page from scrolling to bottom automatically
    set_scroll_position()

    # Sidebar Chat Interface
    with st.sidebar:
        st.sidebar.title("NEC Learning App")
        query_sidebar = st.chat_input("Ask your query", key="sidebar_chat_input")

        if query_sidebar:
            # Add user's query to shared history
            st.session_state.shared_messages.append(
                {"role": "user", "content": query_sidebar}
            )

            # Display the user query in sidebar
            with st.chat_message("user"):
                st.code(query_sidebar)

            # Assistant responds to the query
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                response_text = ""

                # Stream the assistant response
                for ast_mess in stream_response(query_sidebar):
                    response_text = ast_mess
                    message_placeholder.markdown(response_text)

                # Add assistant's response to shared history
                st.session_state.shared_messages.append(
                    {"role": "assistant", "content": response_text}
                )

            trim_conversation()
    # # Scroll to Top Text Link
    # st.markdown(
    #     """
    #     <div style="position: fixed; bottom: 20px; right: 20px; z-index: 999;">
    #         <button onclick="window.scrollTo({top: 0, behavior: 'smooth'});" style="padding: 10px 15px; border-radius: 5px; background-color: #007BFF; color: white; border: none; cursor: pointer;">
    #             Scroll to Top
    #         </button>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # Main Chat Interface
    query = st.chat_input("Ask your query", key="main_chat_query")

    if query:
        # Add user's query to shared history
        st.session_state.shared_messages.append({"role": "user", "content": query})

        # Display the user query in main chat
        with st.chat_message("user"):
            st.code(query)

        # Assistant responds to the query
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response_text = ""

            # Stream the assistant response
            for ast_mess in stream_response(query):
                response_text = ast_mess
                message_placeholder.markdown(response_text)

            # Add assistant's response to shared history
            st.session_state.shared_messages.append(
                {"role": "assistant", "content": response_text}
            )

        trim_conversation()
    

if __name__ == "__main__":
    main()
    set_scroll_position()
