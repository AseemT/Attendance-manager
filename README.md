# Attendance Manager — Academic Attendance Monitoring & Forecasting System

A comprehensive, zero-dependency Python utility designed to track course attendance, enforce university regulatory compliance thresholds (such as 75% or 80% mandates), and provide predictive mathematical modeling for academic planning.

---

## Key Features

- **Multi-Course Tracking**: Manage multiple subjects with distinct course codes, attended classes, missed lectures, and total conducted sessions.
- **Dynamic Compliance Monitoring**: Real-time percentage calculations accompanied by visual status indicators (`Compliant`, `Critical Warning`, or `Debarred`).
- **Predictive Bunk Calculator**: Calculates the exact number of upcoming consecutive lectures a student can safely miss while remaining at or above the designated attendance threshold.
- **Attendance Recovery Planner**: Determines the exact minimum consecutive lectures a student must attend to restore compliance from a low or failing percentage.
- **Data Persistence**: Automatic serialization to a local `attendance_data.json` file to preserve records between runs.
- **Interactive Console UI**: User-friendly menu-driven interface with comprehensive input validation.

---

## Mathematical Formulation

1. **Current Attendance Percentage ($P$)**:
   $$P = \left(\frac{\text{Attended Classes}}{\text{Total Conducted Classes}}\right) \times 100$$

2. **Safe Bunks Remaining ($B$)** to stay at or above threshold $T$ ($0 < T < 1$):
   $$B = \left\lfloor \frac{\text{Attended} - T \times \text{Total}}{T} \right\rfloor \quad (\text{for } P \ge T \times 100)$$

3. **Classes Required for Recovery ($R$)** if currently below threshold $T$:
   $$R = \left\lceil \frac{T \times \text{Total} - \text{Attended}}{1 - T} \right\rceil \quad (\text{for } P < T \times 100)$$

---

## Repository Structure

```text
Attendance-manager/
├── attendance_manager.py     # Core application source code
├── statement.md              # Formal project problem statement & mathematical specifications
├── README.md                 # Project documentation and execution instructions
└── attendance_data.json      # Persistent local storage (auto-generated)
