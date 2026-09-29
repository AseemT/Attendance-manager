import math

# Attendance tracker and safe bunk / recovery planner


def calculate_status(attended, total, target_pct=75.0):
    current_pct = 0.0
    if total > 0:
        current_pct = (attended / total) * 100

    if current_pct >= target_pct:
        # Calculate how many classes can be missed before falling below target
        safe_bunks = math.floor((100 * attended - target_pct * total) / target_pct)
        status = "SAFE"
        margin = max(0, safe_bunks)
        advice = f"You can safely miss the next {safe_bunks} class(es)."
    else:
        # Calculate how many consecutive classes are needed to get back to target
        needed = math.ceil((target_pct * total - 100 * attended) / (100 - target_pct))
        status = "SHORTAGE"
        margin = needed
        advice = f"You must attend the next {needed} consecutive class(es) to recover."

    return status, current_pct, margin, advice


# Helper function to get valid non-negative integer input
def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt).strip())
            if val >= 0:
                return val
            print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    print("=" * 48)
    print("      STUDENT ATTENDANCE & BUNK PLANNER       ")
    print("=" * 48)

    target = 75.0
    target_input = input("Enter target percentage threshold (Default: 75%): ").strip()
    if target_input:
        try:
            val = float(target_input)
            if 0 < val < 100:
                target = val
        except ValueError:
            target = 75.0

    courses = {}

    while True:
        course_name = input("\nEnter Course Code / Name (or 'done' to calculate): ").strip().upper()
        if course_name.lower() == "done":
            break
        if not course_name:
            continue

        attended = get_positive_int(f"Classes attended for {course_name}: ")
        total = get_positive_int(f"Total classes conducted for {course_name}: ")

        if attended > total:
            print("Error: Attended classes cannot exceed total classes conducted.")
            continue

        courses[course_name] = {"attended": attended, "total": total}

    if not courses:
        print("\nNo course data entered. Exiting.")
        return

    # Print summary table
    print("\n" + "=" * 80)
    print(f"{'Course':<15}{'Attendance':<14}{'Current %':<12}{'Status':<12}Recommendation")
    print("=" * 80)

    for course_name, data in courses.items():
        status, pct, margin, advice = calculate_status(data["attended"], data["total"], target)
        att_str = f"{data['attended']}/{data['total']}"
        pct_str = f"{pct:.2f}%"
        print(f"{course_name:<15}{att_str:<14}{pct_str:<12}{status:<12}{advice}")

    print("=" * 80)


if __name__ == "__main__":
    main()
    
