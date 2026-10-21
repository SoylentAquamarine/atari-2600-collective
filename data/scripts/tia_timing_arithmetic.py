colorburst = 3_579_545
clocks_per_line, blank, visible, lines = 228, 68, 160, 262
cpu = colorburst / 3
cyc_line = clocks_per_line // 3
cyc_frame = cyc_line * lines
print("blank+visible ok:", blank + visible == clocks_per_line)
print("CPU clock MHz: %.4f" % (cpu / 1e6))
print("CPU cycles/line:", cyc_line, "exact:", clocks_per_line % 3 == 0)
print("CPU cycles/frame:", cyc_frame)
print("frame rate Hz: %.3f" % (colorburst / (clocks_per_line * lines)))
print("STA zp (3cyc) per line:", cyc_line // 3, "remainder", cyc_line % 3)
print("visible window CPU cycles: %.2f" % (visible / 3))
