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
