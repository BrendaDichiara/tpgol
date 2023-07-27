def generate_pdm_v6(N, M, output_file):
    # Base content of the .pdm file
    BASE_CONTENT = """
Coupled
    {{
    Type = Root
    Name = prueba_{N}x{M}
    Ports = 0; 0
    Description = 
    Graphic
        {{
        Position = 0; 0
        Dimension = 600; 600
        Direction = Right
        Color = 15
        Icon = 
        Window = 4000; 4000; 4000; 4000
        }}
    Parameters
        {{
        }}
    System
        {{
    """.format(N=N, M=M)

    # Base templates for different sections of the .pdm file
    MEDIATOR_TEMPLATE = """
            \t\t Atomic
            {{
            Name = Mediator0
            Ports = {num_ports} ; 1
            Path = gol/mediator.h
            Description = Atomic DEVS model
            Graphic
                {{
                Position = -31125 ; -14970
                Dimension = 300 ; 6405
                Direction = Right
                Color = 4
                Icon = None
                }}
            Parameters
                {{
                filename = Str; initial ; str
                }}
            }}
    """

    SENDER_TEMPLATE = """
        \t\t Atomic
            {{
            Name = Sender{sender_id}
            Ports = 1 ; 1
            Path = gol/cell.h
            Description = Atomic DEVS model
            Graphic
                {{
                Position = -32400 ; {position}
                Dimension = 300 ; 300
                Direction = Right
                Color = 15
                Icon = None
                }}
            Parameters
                {{
                CID = Str; {sender_id} ; int
                }}
            }}
    """

    # Start with the base content and open the 'System' section
    new_content = BASE_CONTENT.strip() + "\n\t\t"

    # Add the MEDIATOR
    new_content += MEDIATOR_TEMPLATE.format(num_ports=N*M).strip() + "\n\t\t"
    # Add each SENDER
    for i in range(N*M):
            new_content += SENDER_TEMPLATE.format(sender_id=i, position=-14700 + 700*i).strip() + "\n\t\t"
        
    # Close the 'System' section and the rest of the file
    new_content += "        }\n    }\n"

    # Write the new .pdm file
    with open(output_file, "w") as file:
        file.write(new_content)

