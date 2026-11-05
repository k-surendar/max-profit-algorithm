def max_profit(n):

    max_earnings = 0
    valid_combinations = set()

    # Building details: (name, construction_time, earning_rate)
    buildings = {
        "T": (5, 1500),
        "P": (4, 1000),
        "C": (10, 2000)
    }

    # Enumerate every possible combination
    for t in range(n // buildings["T"][0] + 1):
        for p in range(n // buildings["P"][0] + 1):
            for c in range(n // buildings["C"][0] + 1):

                # Calculate total construction time
                total_time = (
                    t * buildings["T"][0]
                    + p * buildings["P"][0]
                    + c * buildings["C"][0]
                )

                # Ignore combinations exceeding available time
                if total_time > n:
                    continue

                # Create the building combination
                combination = (t, p, c)

                # Build the list for earnings calculation
                construction_list = (
                    [buildings["T"]] * t
                    + [buildings["P"]] * p
                    + [buildings["C"]] * c
                )

                # Sort by earning rate per construction unit
                construction_list.sort(
                    key=lambda x: x[1] / x[0],
                    reverse=True
                )

                # Calculate earnings
                time_used = 0
                earnings = 0

                for build_time, rate in construction_list:
                    time_used += build_time
                    earnings += rate * (n - time_used)

                # Update maximum and preserve all ties
                if earnings > max_earnings:
                    max_earnings = earnings
                    valid_combinations = {combination}

                elif earnings == max_earnings:
                    valid_combinations.add(combination)

    # Display results
    print(f"Max Earnings: {max_earnings}")
    print("\nValid Combinations:")

    for t, p, c in sorted(valid_combinations):
        print(f"T: {t}, P: {p}, C: {c}")


# Main program
n = int(input("Input Time Unit: "))

if n < 0:
    print("Please enter a non-negative time unit.")
else:
    max_profit(n)
