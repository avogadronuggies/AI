# Priors
P_B, P_E = 0.001, 0.002
P_notB, P_notE = 1 - P_B, 1 - P_E

# Alarm conditionals
P_A = {
    (True, True): 0.95,
    (True, False): 0.94,
    (False, True): 0.29,
    (False, False): 0.001
}

# Calls given alarm
P_J, P_M = {True: 0.90, False: 0.05}, {True: 0.70, False: 0.01}

def compute_joint(b, e, a, j, m):
    return ((P_B if b else P_notB) *
            (P_E if e else P_notE) *
            (P_A[(b, e)] if a else 1 - P_A[(b, e)]) *
            (P_J[a] if j else 1 - P_J[a]) *
            (P_M[a] if m else 1 - P_M[a]))

def main():
    yes = lambda x: x.strip().lower() == 'yes'
    b = yes(input("Burglary? (yes/no): "))
    e = yes(input("Earthquake? (yes/no): "))
    a = yes(input("Alarm? (yes/no): "))
    j = yes(input("John called? (yes/no): "))
    m = yes(input("Mary called? (yes/no): "))
    print(f"\nJoint probability: {compute_joint(b, e, a, j, m):.8f}")

if __name__ == "__main__":
    main()
