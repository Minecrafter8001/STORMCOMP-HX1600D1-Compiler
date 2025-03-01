import re

def assemble(assembly_code):
    # Preprocess the assembly code
    lines = [line.strip() for line in assembly_code.split('\n')]
    
    # First pass: Build symbol table
    symbol_table = {}
    current_address = 0
    label_pattern = re.compile(r'\(([^)]+)\)')
    
    for line in lines:
        # Remove comments
        line = line.split('--')[0].strip()
        if not line:
            continue
        
        # Remove leading line numbers if present
        if line[0].isdigit():
            line = re.sub(r'^\d+\s*', '', line).strip()
        
        # Extract labels
        while True:
            match = label_pattern.search(line)
            if not match:
                break
            label = match.group(1).strip()
            if label in symbol_table:
                raise ValueError(f"Duplicate label: {label}")
            symbol_table[label] = current_address
            line = line.replace(match.group(0), '', 1).strip()
        
        if line:
            current_address += 1

    # Second pass: Generate machine code
    air_a = []
    air_b = []
    current_address = 0
    opcode_table = {
        'NOP': (0, None),
        'LD': (1, 'any'),
        'LDA': (2, [1, 2]),
        'LDD': (3, [1, 2]),
        'LDM': (4, [0, 1, 2]),
        'JUN': (7, [0]),
        'JCN': (8, [1, 2, 3, 4, 5, 6]),
        'ADD': (9, [0]),
        'SUB': (10, [0]),
        'MUL': (11, [0]),
        'DIV': (12, [0]),
        'INC': (13, [0, 1, 2]),
        'DEC': (14, [0, 1, 2]),
        'INP': (15, [1, 2]),
        'OUT': (16, 'any'),
        'DLY': (17, 'any'),
        'HLT': (18, [0]),
    }

    for line in lines:
        # Remove comments and whitespace
        line = line.split('--')[0].strip()
        if not line:
            continue
        
        # Remove leading line numbers if present
        if line[0].isdigit():
            line = re.sub(r'^\d+\s*', '', line).strip()
        
        # Remove labels from line
        while label_pattern.search(line):
            line = label_pattern.sub('', line).strip()
        if not line:
            continue

        # Parse instruction
        parts = re.split(r'\s+', line, 1)
        mnemonic = parts[0].upper()
        operand = parts[1].split('--')[0].strip() if len(parts) > 1 else None

        # Get opcode info
        if mnemonic not in opcode_table:
            raise ValueError(f"Invalid mnemonic: {mnemonic}")
        opcode, allowed = opcode_table[mnemonic]

        # Process operand
        operand_value = 0
        if operand:
            if operand.startswith('@'):
                label = operand[1:]
                if label not in symbol_table:
                    raise ValueError(f"Undefined label: {label}")
                operand_value = symbol_table[label] + 1
            else:
                try:
                    operand_value = int(operand)
                except ValueError:
                    raise ValueError(f"Invalid operand: {operand}")

            # Validate operand
            if allowed != 'any':
                if isinstance(allowed, list) and operand_value not in allowed:
                    raise ValueError(f"Invalid operand for {mnemonic}: {operand}")

        air_a.append(opcode)
        air_b.append(operand_value)
        current_address += 1

    return air_a, air_b

# Example usage
if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        assembly_code = f.read()
    
    air_a, air_b = assemble(assembly_code)
    
    with open('output.txt', 'w') as f:
        f.write('AIRA = {' + ', '.join(map(str, air_a)) + '}\n')
        f.write('AIRB = {' + ', '.join(map(str, air_b)) + '}\n')
