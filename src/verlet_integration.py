# verlet_integration.py
import numpy as np
import matplotlib.pyplot as plt


def acceleration(positions):
    """Simple gravitational acceleration towards the negative y-axis as an example."""
    g = -9.81  # Gravity acceleration in m/s^2
    acc = np.zeros_like(positions, dtype=float)  # Ensure positions are float
    acc[:, 1] = g  # Apply gravity only in the y-direction
    return acc

def verlet_integration(positions, velocities, dt, steps):
    """Performs Verlet Integration for a system of particles in a multi-dimensional space."""
    if dt <= 0 or steps <= 0:
        raise ValueError("Time step and number of steps must be positive.")
    
    trajectory = [positions.copy()]
    accelerations = acceleration(positions)
    positions_prev = positions - velocities * dt + 0.5 * accelerations * dt**2
    
    for _ in range(steps):
        accelerations = acceleration(positions)
        positions_new = 2 * positions - positions_prev + accelerations * dt**2
        positions_prev, positions = positions, positions_new
        trajectory.append(positions.copy())
    
    return np.array(trajectory)

if __name__ == "__main__":
    # Example usage
    positions = np.array([[0.0, 0.0], [1.0, 0.0]], dtype=float)  # Ensure float
    velocities = np.array([[5.0, 5.0], [5.0, 5.0]], dtype=float)  # Ensure float
    dt = 0.01  # Time step
    steps = 1000  # Number of steps

    trajectory = verlet_integration(positions, velocities, dt, steps)

    # Print the final positions of the particles
    print("Final positions:\n", trajectory[-1])

    # Optional: Plot the trajectory
    plt.figure(figsize=(8, 6))
    for i in range(trajectory.shape[1]):
        plt.plot(trajectory[:, i, 0], trajectory[:, i, 1], label=f'Particle {i+1}')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Particle Trajectories')
    plt.legend()
    plt.show()

