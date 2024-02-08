# **The Verlet Algorithm** 
## **Theoretical Background:** 
-	The [Verlet Integration](https://www.algorithm-archive.org/contents/verlet_integration/verlet_integration.html), also known as the Verlet algorithm, is a numerical method used to solve Newton's equations of motion for systems of particles. 
-	It is  popular in molecular dynamics simulations for its simplicity and excellent energy conservation properties. 
## **Derivation and Mathematical Formulation**
-	The core idea behind the Verlet Integration is to compute the positions of particles at a future time step using only their current positions, the positions at a previous time step, and the net forces currently acting on them (which are used to compute acceleration). 
-	This approach stems from the second-order Taylor expansions of the position of a particle.
-	Consider a particle with position **r(t)** at time **t** and let **Δt** be a small-time increment. 
-	The position of the particle at time **t+Δt** can be expanded as:

![Verlet Integration  algorithm equation](Picture1.png)

-	Similarly, the position of the particle at time **t − Δt** can be expanded as:

![Verlet Integration  algorithm equation](Picture2.png)

-	where **v(t)** is the velocity of the particle at time **t**, and
-	 **a(t)** is its acceleration due to forces acting upon it. 
-	The term **O(Δt^3)** represents the error term in the Taylor series expansion, which becomes negligible as **Δt** becomes small.

-	By adding these two equations, the terms involving **v(t)** cancel out, and the error term is of a higher order, which is typically ignored for small **Δt**, leading to:

![Verlet Integration  algorithm equation](Picture3.png)


where: 
-	**r(t + Δt)** is the position at future time **t + Δt**
-	**r(t)** is the current position at time **t**, 
-   **r(t − Δt)** is the position at the past time **t − Δt**, 
-	**a(t)** is the acceleration at time **t**, and 
-	**Δt** is the time step.

Essentially, this equation estimates the new position **(r( t+ Δt))** based on the current and previous positions **(r(t) and r(t − Δt))**, as well as the current acceleration **(a(t))**, with **Δt** being the time step.  


## **Practical Implementation:** 
**Initialisation:** 
-	At the start, since there's no "previous position" **(r(t − Δt))** available, an initial approximation is necessary. 
-	This is derived using a first-order approximation like **(t − Δt) = r(t)− v(t) Δt+ 1/2 a(t)Δt^2**
**Loop Over Time Steps:** 
-	For each time step in the simulation, calculate the new positions using the central equation of Verlet Integration. 
-	Update the positions of all particles accordingly. 
Force Calculation: 
-	After updating the positions, calculate the new forces (and thus accelerations) acting on each particle due to their new positions.


# **Velocity Verlet Algorithm:**
-	The Velocity Verlet algorithm is an extension of the Verlet algorithm, designed to explicitly calculate both positions and velocities of particles at each time step, offering a good balance between computational efficiency, accuracy, and ease of implementation. 

## **Theoretical Background: **
-	The Velocity Verlet algorithm can be derived from the Taylor series expansion of particle positions and velocities. 
-	Consider a particle with position **r(t)** and velocity **v(t)** at time **t**, subject to an acceleration **a(t)** due to forces acting on it according to Newton's second law. 
-	The position of the particle at a future time **t + Δt** can be expanded using the Taylor series as:

![Verlet Integration  algorithm equation](Picture4.png)

-	Similarly, the velocity v(t + Δt) can be expanded as:

![Verlet Integration  algorithm equation](Picture5.png)

-	The Velocity Verlet algorithm refines this by incorporating the acceleration at **t + Δt** into the velocity update, splitting the velocity update into two half-steps:
1.	First, it partially updates the velocity using the acceleration at the start of the time step:

![Verlet Integration  algorithm equation](Picture6.png)

2.	Then, it updates the position using this partially updated velocity:

![Verlet Integration  algorithm equation](Picture7.png)

3.	After updating the position, the new acceleration **a(t+ Δt)** is calculated based on the forces at the new position.

4.	Finally, it completes the velocity update with

![Verlet Integration  algorithm equation](Picture8.png)







