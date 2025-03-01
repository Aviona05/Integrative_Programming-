# Define sets
A = {"a", "b", "c", "d", "f", "g"}
B = {"b", "c", "h", "l", "m", "o"}
C = {"c", "d", "f", "h", "i", "j", "k"}

# (a) Elements in A and B (A ∩ B)
a_intersect_b = A & B
print("(a) Elements in A and B:", a_intersect_b, "Count:", len(a_intersect_b))

# (b) Elements in B that are not in A or C (B - (A ∪ C))
b_not_in_a_c = B - (A | C)
print("(b) Elements in B but not in A or C:", b_not_in_a_c, "Count:", len(b_not_in_a_c))

# (c) Set operations
set_i = C - A  # {h, i, j, k}
print("(c.i) Elements:", set_i)

set_ii = A & C  # {c, d, f}
print("(c.ii) Elements:", set_ii)

set_iii = (A & B) | (B & C)  # {b, c, h}
print("(c.iii) Elements:", set_iii)

set_iv = (A & C) - B  # {d, f}
print("(c.iv) Elements:", set_iv)

set_v = A & B & C  # {c}
print("(c.v) Elements:", set_v)

set_vi = B - (A | C)  # {l, m, o}
print("(c.vi) Elements:", set_vi)
