
import numpy as np

# Step 1: Simulation Time
N = 400000

# Step 2: Bearing Life Distribution (Table A)
life = [1200, 1400, 1600, 1800, 2000]
life_prob = [0.10, 0.25, 0.30, 0.25, 0.10]

# Step 3: Delay Time Distribution (Table B)
delay = [2, 3, 4, 8]
delay_prob = [0.20, 0.30, 0.30, 0.20]

# Step 4: Repair Time
repair_time = {1: 15, 2: 25, 3: 30, 4: 35}


# Step 5: Simulation Function
def simulate(policy):

    rng = np.random.default_rng(42)

    bearings = rng.choice(life, size=4, p=life_prob)

    clock = 0
    total_cost = 0
    total_bearings = 0
    total_events = 0

    while clock < N:

        # Find minimum bearing life
        t = np.min(bearings)

        if clock + t >= N:
            break

        # Machine runs until a bearing fails
        clock = clock + t
        bearings = bearings - t

        # Find failed bearings
        failed = np.where(bearings <= 0)[0]
        k = len(failed)

        # Generate technician delay
        d = rng.choice(delay, p=delay_prob)

        # Present Policy
        if policy == "present":

            changed = k
            r = repair_time[k]

            # Replace only failed bearings
            bearings[failed] = rng.choice(
                life, size=k, p=life_prob
            )

        # Proposed Policy
        else:

            changed = 4
            r = 35

            # Replace all four bearings
            bearings = rng.choice(
                life, size=4, p=life_prob
            )

        # Calculate Cost
        downtime = d + r

        downtime_cost = downtime * 5
        technician_cost = (r / 60) * 30
        bearing_cost = changed * 30

        total_cost = total_cost + downtime_cost
        total_cost = total_cost + technician_cost
        total_cost = total_cost + bearing_cost

        # Update Simulation
        clock = clock + downtime / 60

        total_bearings = total_bearings + changed
        total_events = total_events + 1

    return total_cost, total_events, total_bearings


# Step 6: Simulate Present Policy
present_cost, p_events, p_bearings = simulate("present")

# Step 7: Simulate Proposed Policy
proposed_cost, q_events, q_bearings = simulate("proposed")


# Step 8: Display Results
print("Present Policy")
print("Total Cost =", present_cost)
print("Total Events =", p_events)
print("Bearings Replaced =", p_bearings)

print("\nProposed Policy")
print("Total Cost =", proposed_cost)
print("Total Events =", q_events)
print("Bearings Replaced =", q_bearings)


# Step 9: Choose Better Policy
print("\nComparison")

if present_cost < proposed_cost:
    print("Present Policy is Better")

else:
    print("Proposed Policy is Better")
