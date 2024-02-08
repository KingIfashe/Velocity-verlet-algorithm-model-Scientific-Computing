Verlet Integration 
Theoretical Background: 
-	Verlet Integration is used for its simplicity and excellent long-term energy conservation.
-	It calculates the position of particles in a system at a future time step using only the current position, the position at the previous time step, and the current acceleration.
-	The Verlet Integration, also known as the Verlet algorithm, is a numerical method used to solve Newton's equations of motion for systems of particles. 
-	It is particularly popular in molecular dynamics simulations for its simplicity and excellent energy conservation properties. 
Derivation and Mathematical Formulation
-	The core idea behind the Verlet Integration is to compute the positions of particles at a future time step using only their current positions, the positions at a previous time step, and the net forces currently acting on them (which are used to compute acceleration). 
-	This approach stems from the second-order Taylor expansions of the position of a particle.
-	Consider a particle with position r ⃗ (t) at time t and let Δt be a small-time increment. 
-	The position of the particle at time t+Δt can be expanded as:
