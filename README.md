<b>Dynamic Character Movement</b>
<br>This program implements and tests the dynamic movement update and three dynamic movement behaviors: Seek, Flee, and Arrive. The Newton-Euler-1 movement update algorithm is used to update the position of the character after each timestep. A trajectory text file (.txt) is generated that tracks the character's movement per timestep. </br>

<br><b>Project Files</b></br>
  - [Dynamic Movement Program](https://github.com/EricDelgado993/Dynamic-Movement/blob/main/Dynamic%20Movement%20Project/Dynamic%20Character%20Movement.py)
  - [Character Movement Plot Data](https://github.com/EricDelgado993/Dynamic-Movement/blob/main/Dynamic%20Movement%20Project/Character%20Movement%20Plot%20Data.txt)

<br><b>Features</b></br>
  - <b>Character Movement Simulation:</b> Simulates character movement in a 2D space based on position, velocity, and acceleration in both the X and Z directions.
  - <b>Steering Behaviors:</b> Supports multiple steering behaviors:
    - <b>Seek:</b> Character moves towards a target.
    - <b>Flee:</b> Character moves away from a target.
    - <b>Arrive:</b> Character slows down and stops at a target.
    - <b>Continue:</b> Character maintains its current motion.
  - <b>Realistic Physics:</b> Implements velocity and acceleration caps (maximum velocity and acceleration) for realistic movement control.
  - <b>Simulation Time Control:</b> Adjustable time step for simulation, allowing precise control over character updates.
  - <b>Trajectory Tracking:</b> Tracks the positions, velocities, and other parameters of all characters at each time step.
  - <b>File Output:</b> Saves trajectory data into a "results.txt" file, recording the simulation over time for further analysis.

<br><b>Plot of Character Movement After 50 Seconds</b></br>
![Character Movement Plot](https://github.com/user-attachments/assets/6280a0c9-e58f-461a-9218-e4118a9054bc)

