Consider this example [JSON defining "Development Roles Responsibility"].

[
    [
        0,
        0,
        "Project Charter",
        [
            "Business proposition",
            "Project scope & budget",
            "Client communication",
            "Sprint Planning meetings"
        ]
    ],
    [
        1,
        0,
        "Technology selection",
        [
            "Select Development Tools",
            "Infrastructure - Frameworks & Tools",
            "Setup Guide",
            "Create \"Hello World\"",
            "Decide on App deployment"
        ]
    ],
    [
        2,
        0,
        "Version control",
        [
            "Setup Github account",
            "Setup Github Pages repository",
            "Decide how to publish your project docs",
            "User Guide for development workflow"
        ]
    ],    
    [
        0,
        1,
        "Setup communications",
        [
            "Configure communication tools",
            "Team communication",
            "Plan daily meetings"
        ]
    ],
    [
        1,
        1,
        "Software Architecture",
        [
            "Apps = Data + Views",
            "Data models",
            "Views and wireframes"
        ]
    ],
    [
        2,
        1,
        "Test-driven development workflow",
        [
            "Build simple app",
            "Build simple test",
            "Document workflow built around tests"
        ]
    ],
]

Here is the example of the [Python table] that matches.

[
    [[
            "Project Charter",
            [
                "Business proposition",
                "Project scope & budget",
                "Client communication",
                "Sprint Planning meetings"
            ]
        ],
        [
            "Technology selection",
            [
                "Select Development Tools",
                "Infrastructure - Frameworks & Tools",
                "Setup Guide",
                "Create \"Hello World\"",
                "Decide on App deployment"
            ]
        ],
        [
            "Version control",
            [
                "Setup Github account",
                "Setup Github Pages repository",
                "Decide how to publish your project docs",
                "User Guide for development workflow"
            ]
        ]],    
    [[
            "Setup communications",
            [
                "Configure communication tools",
                "Team communication",
                "Plan daily meetings"
            ]
        ],
        [
            "Software Architecture",
            [
                "Apps = Data + Views",
                "Data models",
                "Views and wireframes"
            ]
        ],
        [
            "Test-driven development workflow",
            [
                "Build simple app",
                "Build simple test",
                "Document workflow built around tests"
            ]
        ]]
]
Create a Python script to convert from [JSON defining "Development Roles Responsibility"] to the [Python table].

The first item in each list is the row and the second item is the column. 

The third and fourth items define the Deliverable and the Details respectively.


Show the table as HTML in a code block.

