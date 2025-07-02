# from abtin
def generate_arch(circuit, type="compact_layout"):
    gates, ops = wisq.dascot.extract_gates_from_file(circuit)
    qubits = len(wisq.dascot.extract_qubits_from_gates(gates))
    arch = wisq.architecture.compact_layout(qubits, magic_states="all_sides")
    arch["magic_state_qubits"] = arch.pop("magic_states")
    arch["graph"] = []
    for i in range(arch["width"] * arch["height"]):
        for j in range(arch["width"] * arch["height"]):
            if abs(i - j) == 1 or abs(i - j) == arch["width"]:
                arch["graph"].append([i, j])
    json.dump(
        arch,
        open("arch.json", "w"),
        indent=4,
    )
