# velocity_verlet.py
import numpy as np
import matplotlib.pyplot as plt

from verlet_integration import acceleration  # Importing the acceleration function

def velocity_verlet(positions, velocities, dt, steps):
    """Performs Velocity Verlet Integration using the imported acceleration function."""
    if dt <= 0 or steps <= 0:
        raise ValueError("Time step and number of steps must be positive.")
    
    trajectory = [positions.copy()]
    accelerations = acceleration(positions)
    
    for _ in range(steps):
        positions += velocities * dt + 0.5 * accelerations * dt**2
        new_accelerations = acceleration(positions)
        velocities += 0.5 * (accelerations + new_accelerations) * dt
        accelerations = new_accelerations
        trajectory.append(positions.copy())
    
    return np.array(trajectory)

if __name__ == "__main__":
    # Initial conditions
    positions = np.array([[0.0, 10.0], [0.0, 20.0]])  # Initial positions of two particles
    velocities = np.array([[5.0, 0.0], [-5.0, 0.0]])  # Initial velocities
    dt = 0.01  # Time step in seconds
    steps = 100  # Number of steps to simulate

    # Run the simulation
    trajectory = velocity_verlet(positions, velocities, dt, steps)

    # Print the final positions
    print("Final positions:\n", trajectory[-1])

    # Plot the trajectory
    plt.figure(figsize=(8, 6))
    for i in range(trajectory.shape[1]):
        plt.plot(trajectory[:, i, 0], trajectory[:, i, 1], label=f'Particle {i+1}')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Particle Trajectories')
    plt.legend()
    plt.show()

