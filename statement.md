# Attendance Manager — Academic Attendance Monitoring & Forecasting System

## 1. Project Overview & Scope
**Attendance Manager** is a dedicated Python-based application designed to monitor academic course attendance, enforce university regulatory compliance thresholds (such as 75% or 80% mandates), and generate predictive attendance analytics for undergraduate students. The application provides analytical simulation tools enabling users to evaluate future lecture absences and schedule necessary recovery periods without falling into academic default or debarment.

The scope of this project encompasses:
- Multi-course management tracking attended lectures, absent sessions, and total conducted classes.
- Continuous threshold compliance monitoring with real-time percentage computation and graded risk alerts (Compliant / Critical / Debarred).
- Bunk Forecasting: Mathematically calculating the maximum consecutive classes a student can miss while maintaining aggregate compliance at or above the designated threshold.
- Attendance Recovery Optimization: Projecting the exact minimum consecutive lectures a student must attend to restore compliance if their current record is in default.
- CLI User Interface: Structured console interface supporting course addition, record updates, batch inspection, and what-if simulation scenarios.
- Persistent Storage: File-based state serialization (JSON/CSV) to preserve records reliably across execution sessions.

---

## 2. Problem Statement
Institutional attendance policies strictly mandate that students maintain a predefined percentage of physical attendance to remain eligible for term-end examinations. In practice, students manually estimate their attendance, which frequently results in calculation errors, unexpected debarment notices, and poor planning.

Key challenges addressed by Attendance Manager include:
1. Identifying whether upcoming scheduled leaves will cause a violation of minimum compliance thresholds.
2. Accurately determining the number of consecutive classes required to recover from an attendance shortage.
3. Managing multi-subject workloads with varying weekly credit distributions and schedules.

The principal objective of Attendance Manager is to eliminate guesswork through deterministic mathematical models, giving students full transparency over their academic standing and helping them plan attendance strategically.

---

## 3. Mathematical Models & Core Logic
- **Current Attendance Percentage ($P$)**:
  $$P = \left(\frac{\text{Attended Classes}}{\text{Total Conducted Classes}}\right) \times 100$$

- **Safe Missable Classes ($B$)** to remain at or above threshold $T$ ($0 < T < 1$):
  $$B = \left\lfloor \frac{\text{Attended} - T \times \text{Total}}{T} \right\rfloor \quad (\text{for } P \ge T \times 100)$$

- **Classes Required for Recovery ($R$)** if currently below threshold $T$:
  $$R = \left\lceil \frac{T \times \text{Total} - \text{Attended}}{1 - T} \right\rceil \quad (\text{for } P < T \times 100)$$

---

## 4. Academic Metadata
- **Project Title**: Attendance Manager
- **Course**: Problem Solving and Python Programming
- **Institution**: VIT Bhopal University
- **Student Name**: Aseem Tiwari
- **Faculty In-Charge**: Dr. Harihar Sitaraman
- **Academic Year**: 2026–2027
