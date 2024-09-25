## NEC Syllabus for Computer Engineering
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
