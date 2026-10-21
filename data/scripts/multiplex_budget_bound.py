"""Optimistic upper bounds on per-scanline object re-strobes from the NTSC budget (unsourced recall constants)."""
CLK_PER_CPU = 3
VISIBLE_PX = 160
LINE_CPU = 76
PLAYER_PX = 8
HM_RANGE = 8  # recalled +/-8 px fine motion

coarse_positions = VISIBLE_PX // CLK_PER_CPU
print("coarse RESP positions across 160 px:", coarse_positions, "(resolution", CLK_PER_CPU, "px)")
print("fine range covers gap:", HM_RANGE >= CLK_PER_CPU - 1, "(need", CLK_PER_CPU - 1, "px, have", HM_RANGE, ")")

def bound(cycles_per_copy):
    # each copy occupies max(PLAYER_PX px, cycles_per_copy*3 px) of beam; copies are serial within the visible window
    span = max(PLAYER_PX, cycles_per_copy * CLK_PER_CPU)
    return VISIBLE_PX // span, span

for label, c in (("STA RESPx only (3 cyc)", 3), ("LDA#+STA GRPx (5 cyc)", 5), ("LDA#+STA GRPx+STA RESPx (8 cyc)", 8)):
    n, span = bound(c)
    print(f"{label}: {c} cycles -> {span} px/copy -> <= {n} copies per line")
