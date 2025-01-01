###### [↩️Return to Portfolio](https://github.com/EricDelgado993/Portfolio)
# Dynamic Character Movement

## **Overview**
The **Dynamic Character Movement** program simulates and tests dynamic movement behaviors for characters in a 2D space. Using the Newton-Euler-1 movement update algorithm, the program calculates and updates the position of each character based on their movement behavior after every time step. The simulated trajectories are logged in a `.txt` file in CSV format, making it easy to analyze and visualize the results.

This project is a great example of simulating dynamic systems and implementing steering behaviors for character movement. Perfect for games, simulations, and AI behavior modeling.

---

## 📂 **Project Files**
- [Dynamic Movement Program](https://github.com/EricDelgado993/Dynamic-Movement/blob/main/Dynamic%20Movement%20Project/Dynamic%20Character%20Movement.py) - Implements the movement simulation and behavior algorithms.
- [Character Movement Plot Data](https://github.com/EricDelgado993/Dynamic-Movement/blob/main/Dynamic%20Movement%20Project/Character%20Movement%20Plot%20Data.txt) - Contains trajectory logs for visualization.

---

## **Features**

### **Character Movement Simulation**
- Simulates the movement of characters in a 2D space using position, velocity, and acceleration in both the X and Z axes.

### **Steering Behaviors**
- Supports multiple dynamic movement behaviors:
  - **Seek**: Character moves towards a target.
  - **Flee**: Character moves away from a target.
  - **Arrive**: Character slows down and stops at the target.
  - **Continue**: Character maintains its current motion without external steering.

### **Realistic Physics**
- Implements velocity and acceleration caps to control movement realistically.

### **Simulation Time Control**
- Adjustable time step for simulation, enabling precise updates for each character's movement.

### **Trajectory Tracking**
- Logs the following parameters at every time step:
  - Position (X, Z)
  - Velocity (X, Z)
  - Acceleration (X, Z)
- Tracks the progression of each character over time.

### **File Output**
- Saves simulation results into a `results.txt` file in CSV format for easy data analysis and visualization.

---

## **How It Works**
1. **Define Characters**: Set up characters with initial positions, velocities, and desired steering behaviors.
2. **Simulate Dynamics**: Use the Newton-Euler-1 algorithm to compute position updates based on velocity and acceleration.
3. **Log Data**: Record trajectory data for all characters at each time step.
4. **Analyze Output**: Use the `results.txt` file to visualize or analyze the movement trajectories.

---

## Plot of Character Movement After 50 Seconds
![Character Movement Plot](https://github.com/user-attachments/assets/6280a0c9-e58f-461a-9218-e4118a9054bc)
<br>This plot illustrates the trajectories of characters exhibiting dynamic behaviors (Seek, Flee, Arrive, and Continue) over a 50-second simulation in 2D space.
