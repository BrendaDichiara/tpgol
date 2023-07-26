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
        Window = 5000; 5000; 5000; 5000
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
                Position = -15780 ; -8850
                Dimension = 675 ; 1350
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
                Position = -17880 ; {position}
                Dimension = 675 ; 720
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
            new_content += SENDER_TEMPLATE.format(sender_id=i, position=-9510 + 1425*i).strip() + "\n\t\t"
        
    # Close the 'System' section and the rest of the file
    new_content += "        }\n    }\n"

    # Write the new .pdm file
    with open(output_file, "w") as file:
        file.write(new_content)

# Set the size of the board
N = 10
M = 10

# Output file path
output_file = "prueba_{0}x{1}.pdm".format(N, M)

# Generate the .pdm file
generate_pdm_v6(N, M, output_file)

