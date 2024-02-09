import numpy as np
import matplotlib.pyplot as plt

def acceleration(positions, mass=None, force_func=None):
    """
    Defines the acceleration function for particles.
    """
    if force_func is None:
        # Default gravity acceleration
        g = 9.81  # Gravity acceleration in m/s^2
        acc = np.zeros_like(positions)
        acc[:, 1] = -g  # Apply gravity only in the y-direction
    else:
        # Use provided force function
        acc = force_func(positions, mass)

    if mass is not None and mass.shape != positions.shape:
        raise ValueError("Masses and positions must have the same shape.")

    return acc

def calculate_energy(positions, velocities):
    """
    Calculate the kinetic energy for demonstration purposes.
    """
    kinetic_energy = 0.5 * np.sum(velocities**2)  # Simplified kinetic energy
    return kinetic_energy

def verlet_integration(positions, velocities, dt, steps, return_all=False, time_points=None,
                       early_termination=False, accuracy_threshold=1e-6, max_dt=None):
    """
    Performs Verlet integration for a system of particles with optimizations.
    """
    trajectory = [] if return_all else []
    positions_prev = positions - velocities * dt + 0.5 * acceleration(positions) * dt**2
    if early_termination:
        prev_energy = calculate_energy(positions, velocities)  # Initialize prev_energy here

    for step in range(steps):
        dt_eff = dt
        if max_dt is not None and dt > max_dt:
            n_substeps = int(np.ceil(dt / max_dt))
            dt_eff = dt / n_substeps
            for _ in range(n_substeps):
                positions_prev, positions = positions, 2 * positions - positions_prev + acceleration(positions) * dt_eff**2
                positions_prev = positions.copy()
        else:
            positions_prev, positions = positions, 2 * positions - positions_prev + acceleration(positions) * dt_eff**2
            positions_prev = positions.copy()

        if early_termination:
            new_energy = calculate_energy(positions, velocities)
            if abs((new_energy - prev_energy) / prev_energy) < accuracy_threshold:
                print(f"Early termination at step {step+1}")
                break
            prev_energy = new_energy

        if return_all or (time_points is not None and step in time_points):
            trajectory.append(positions.copy())

    return np.array(trajectory) if return_all else [positions[i] for i in time_points]

if __name__ == "__main__":
    # Initial conditions: two particles
    positions = np.array([[6.0, 4.5], [2.7, 6.1]], dtype=float)
    velocities = np.array([[5.0, 10.0], [5.0, -5.0]], dtype=float)
    dt = 0.01
    steps = 100

    # Always collect the full trajectory
    full_trajectory = verlet_integration(positions, velocities, dt, steps, return_all=True)

    # Define specific time points for demonstration (every 100 steps)
    time_points = list(range(0, steps, 100))
    specific_points_trajectory = full_trajectory[time_points] if time_points else None

    # Plotting section remains largely the same, with adjustments for plotting specific points
    plt.figure(figsize=(10, 6))
    for i in range(full_trajectory.shape[1]):
        plt.plot(full_trajectory[:, i, 0], full_trajectory[:, i, 1], label=f'Particle {i+1}')
        if specific_points_trajectory is not None:
            plt.scatter(specific_points_trajectory[:, i, 0], specific_points_trajectory[:, i, 1], marker='x', color='red')

    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Particle Trajectories with Specific Points')
    plt.legend()
    plt.grid(True)
    plt.show()
