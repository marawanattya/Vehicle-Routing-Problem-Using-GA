# Vehicle-Routing-Problem-Using-GA
Solving Vehicle Routing Problem using Genetic Algorithms.

---

# **Team members**

    Marawan Attya               320210295                            Section 5
    Abdallah Ashraf             320210338                            Section 5
    Mohamed Sherif              320210277                            Section 5
    Ezzeldin Mahmoud            320210319                            Section 5


# **Vehicle Routing Problem Optimization Using Genetic Algorithm**

---

## **Abstract**

The Vehicle Routing Problem (VRP) is a complex combinatorial optimization problem critical in logistics and supply chain management. This project implements a Genetic Algorithm (GA) to optimize delivery routes, minimizing the total distance traveled while adhering to vehicle capacity constraints. Results show a significant reduction in travel distance over multiple generations, demonstrating the algorithm's efficacy in solving VRPs.

---

## **1. Introduction**

### **1.1 Background**
The VRP involves determining the most efficient routes for a fleet of vehicles to deliver goods from a central depot to various customers. It is a cornerstone of efficient logistics and has applications in transportation, delivery services, and inventory management. 

### **1.2 Problem Statement**
Given:
- A central depot and multiple customer locations.
- A fleet of vehicles with defined capacity limits.
- Goods demand at each customer location.

The goal is to:
1. Minimize the total travel distance.
2. Satisfy all customer demands without exceeding vehicle capacities.

### **1.3 Importance**
Optimizing VRP reduces operational costs, improves service efficiency, and minimizes environmental impact.

---

## **2. Methodology**

### **2.1 Problem Representation**
- **Depot**: Single starting and ending point, represented as coordinates `[0, 0]`.
- **Deliveries**: Customer locations represented as coordinate pairs.
- **Demands**: Integer values indicating the goods required by each customer.
- **Vehicle Capacity**: Fixed at 15 units.
- **Number of Vehicles**: 10 vehicles available for delivery.

### **2.2 Genetic Algorithm Overview**
1. **Chromosome Representation**:
   - Each solution (chromosome) is a set of routes, where each route is a sequence of customer indices assigned to a vehicle.

2. **Fitness Function**:
   - **Objective**: Minimize total travel distance.
   - **Penalty**: Add a large penalty (`1e6`) if a route exceeds the vehicle's capacity.

3. **Selection**:
   - Tournament selection chooses the best candidate from a randomly sampled subset of solutions.

4. **Crossover**:
   - **Method**: Modified Order Crossover (OX).
   - Combines routes from two parents while preserving order and avoiding duplicates.

5. **Mutation**:
   - Randomly swaps two customers in a route with a predefined mutation rate (`0.2`).

6. **Survivor Selection**:
   - Elite solutions (top 10%) are retained in the next generation.

---

## **3. Implementation**

### **3.1 Algorithm Workflow**
1. **Initialization**:
   - Generate an initial population of random feasible routes.
2. **Evaluation**:
   - Compute the fitness of each chromosome.
3. **Reproduction**:
   - Select parents using tournament selection.
   - Generate offspring through crossover and mutation.
4. **Replacement**:
   - Combine elite individuals and offspring to form the new population.
5. **Iteration**:
   - Repeat for a fixed number of generations or until convergence.

### **3.2 Data Preprocessing**
- Input data loaded from a JSON file.
- Coordinates and demands validated to ensure feasibility.

### **3.3 Parameters**
| **Parameter**          | **Value**       |
|-------------------------|-----------------|
| Population Size         | 200             |
| Generations             | 20              |
| Mutation Rate           | 0.2             |
| Crossover Rate          | 0.8             |
| Tournament Size         | 5               |
| Vehicle Capacity        | 15 units        |

---

## **4. Results**

### **4.1 Performance Metrics**
- **Initial Solution**:
  - Total Distance: 5980.80
- **Optimized Solution**:
  - Total Distance: 5875.59
- **Improvement**:
  - Distance Reduced: ~105.21 units (~1.76%).

### **4.2 Optimized Routes**
Routes are provided for all vehicles, showcasing efficient delivery paths while adhering to constraints.

### **4.3 Visualization**
(Include route maps showing the depot, customer locations, and vehicle paths for clarity.)

---

## **5. Discussion**

### **5.1 Challenges**
- **Route Feasibility**:
  Ensuring solutions respect capacity constraints during initialization and mutation.
- **Computational Cost**:
  Evaluating fitness for large populations and complex data took significant computation time.
- **Parameter Sensitivity**:
  The algorithm's performance depended on carefully tuned parameters, particularly mutation and crossover rates.

### **5.2 Potential Enhancements**
1. **Adaptive Genetic Operators**:
   - Dynamically adjust mutation and crossover rates to improve convergence.
2. **Hybrid Algorithms**:
   - Combine GA with local search techniques like Simulated Annealing or Tabu Search.
3. **Scalability**:
   - Parallelize computations to handle larger datasets efficiently.

---

## **6. Conclusion**

This project successfully applied a Genetic Algorithm to optimize a VRP with capacity constraints. The algorithm demonstrated significant improvements in total travel distance over 20 generations. Future work could explore hybrid approaches and scalability enhancements to address real-world challenges in logistics optimization.

---


# **7. Reference**
1. Ochelska-Mierzejewska, J., Poniszewska-Marańda, A., & Marańda, W. (2021). Selected Genetic Algorithms for Vehicle Routing Problem Solving. Electronics, 10(24), 3147. https://doi.org/10.3390/electronics10243147

