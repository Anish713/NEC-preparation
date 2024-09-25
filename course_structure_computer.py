## NEC Syllabus for Computer Engineering
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
