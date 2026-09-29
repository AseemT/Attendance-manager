"""
Student Attendance & Bunk Detector
Fundamentals:
- Math modeling (ceil / floor boundary calculations)
- Dictionary state management & clean tabular alignment
- Exception handling & defensive numeric parsing
- Dynamic conditional advising logic
"""

import math

def calculate_status(attended, total, target_pct=75.0):
    current_pct = 0.0
    if total > 0:
        current_pct = attended / total * 100

    if current_pct >= target_pct:
        safe_bunks = math.floor((100 * attended - target_pct * total) / target_pct)
        status = "SAFE"
        margin = max(0, safe_bunks)
        advice = f"You can safely miss the next {safe_bunks} class(es)."
    else:
        needed = math.ceil((target_pct * total - 100 * attended) / (100 - target_pct))
        status = "SHORTAGE"
        margin = needed
        advice = f"You must attend the next {needed} consecutive class(es) to recover."

    return {
        "status": status,
        "current_pct": current_pct,
        "margin": margin,
        "advice": advice
    }


def get_positive_int(prompt):
    while True:
        try:
            number = int(input(prompt).strip())
            if number >= 0:
                return number
            print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    print("=" * 48)
    print("      STUDENT ATTENDANCE & BUNK PLANNER       ")
    print("=" * 48)

    target = 75.0
    try:
        target_input = input("Enter target percentage threshold (Default: 75%): ").strip()
        if target_input:
            target = float(target_input)
            if not (0 < target < 100):
                target = 75.0
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

    print("\n" + "=" * 80)
    header = "Course".ljust(15)
    header += "Attendance".ljust(14)
    header += "Current %".ljust(12)
    header += "Status".ljust(12)
    header += "Recommendation"
    print(header)
    print("=" * 80)

    for course_name, data in courses.items():
        result = calculate_status(data["attended"], data["total"], target)
        attendance = f"{data['attended']}/{data['total']}"
        percentage = f"{result['current_pct']:.2f}%"
        row = course_name.ljust(15)
        row += attendance.ljust(14)
        row += percentage.ljust(12)
        row += result["status"].ljust(12)
        row += result["advice"]
        print(row)

    print("=" * 80)


if __name__ == "__main__":
    main()