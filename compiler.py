import re
import sys


def assemble(assembly_lines):
    symbols = {}
    address = 0

    # First pass: collect labels and their addresses
    for line in assembly_lines:
        # Strip comments and whitespace
        line = re.split(r"--", line)[0].strip()
        if not line:
            continue

        # Extract label if present
        label_match = re.search(r"\(\s*(\w+)\s*\)\s*$", line)
        if label_match:
            label = label_match.group(1)
            symbols[label] = address
            line = line[: label_match.start()].strip()

        # Check for line number and process instruction
        parts = line.split()
        if parts:
            # Skip line number if present
            if parts[0].isdigit():
                parts = parts[1:]
            if parts:
                address += 1

    # Second pass: generate instruction and data lists
    instruction_list = []
    data_list = []
    address = 0  # Reset address counter for second pass

    mnemonic_to_opcode = {
        "NOP": 0,
        "LD": 1,
        "LDA": 2,
        "LDD": 3,
        "LDM": 4,
        "JUN": 7,
        "JCN": 8,
        "ADD": 9,
        "SUB": 10,
        "MUL": 11,
        "DIV": 12,
        "INC": 13,
        "DEC": 14,
        "INP": 15,
        "OUT": 16,
        "DLY": 17,
        "HLT": 18,
    }

    for line in assembly_lines:
        # Strip comments and whitespace
        line = re.split(r"--", line)[0].strip()
        if not line:
            continue

        # Remove label from line
        line = re.sub(r"\(\s*\w+\s*\)\s*$", "", line).strip()
        parts = line.split()
        if not parts:
            continue

        # Skip line number if present
        if parts[0].isdigit():
            parts = parts[1:]
        if not parts:
            continue

        mnemonic = parts[0].upper()
        operand = parts[1] if len(parts) > 1 else "0"

        # Get opcode
        opcode = mnemonic_to_opcode.get(mnemonic)
        if opcode is None:
            raise ValueError(f"Unknown mnemonic '{mnemonic}' in line: {line}")

        # Process operand
        data = 0
        if operand.startswith("@"):
            label_name = operand[1:]
            data = symbols.get(label_name)
            if data is None:
                raise ValueError(f"Undefined label '{label_name}' in line: {line}")
        else:
            try:
                data = int(operand)
            except ValueError:
                raise ValueError(f"Invalid operand '{operand}' in line: {line}")

        instruction_list.append(opcode)
        data_list.append(data)
        address += 1

    return instruction_list, data_list



if __name__ == "__main__":
    with open("input.txt", "r") as file:
        assembly_code = file.read()

    # Split the assembly code into lines
    lines = [line.strip() for line in assembly_code.strip().split("\n")]

    try:
        instructions, data = assemble(lines)
        output = f"AIRA = {{{', '.join(map(str, instructions))}}}\nAIRB = {{{', '.join(map(str, data))}}}"
        print("Compiled successfully.")
        with open("output.txt", "w") as file:
            file.write(output)
    except ValueError as e:
        print("Compilation failed:", e)
