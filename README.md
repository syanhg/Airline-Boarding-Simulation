# Aircraft Boarding Optimization

This repository contains mathematical models and simulations for optimizing aircraft boarding procedures.

## Overview

Aircraft turnaround time is a critical operational metric for airlines. Efficient boarding directly impacts on-time performance, fuel consumption, and customer satisfaction. This project applies mathematical modeling to examine different boarding strategies and identify optimal approaches.

## Aircraft Model

The Boeing 737-800 is used as the model for this simulation with the following specifications:
- **Seating Configuration**: 3-3 (single aisle)
- **Row Range**: 28-48
- **Seat Labels**: A, B, C (left side) and D, E, F (right side)
- **Total Economy Seats**: 114 seats

## Boarding Strategies

This repository models three primary boarding strategies:

### 1. Back-to-Front Boarding
Passengers are boarded in groups from the back of the aircraft to the front, aiming to minimize interference between passengers.

### 2. Outside-In (Window-Middle-Aisle) Boarding
Passengers board based on seat position rather than row:
- Window seats board first
- Middle seats board second
- Aisle seats board last
This strategy minimizes interference between passengers within the same row.

### 3. Hybrid Strategy (Optimized)
A combination of back-to-front and outside-in strategies:
1. Back window seats
2. Middle window seats
3. Front window seats
4. Back middle seats
5. Middle middle seats
6. Front middle seats
7. Back aisle seats
8. Middle aisle seats
9. Front aisle seats

## Simulation Results

The simulations demonstrate that the hybrid and outside-in strategies outperform the traditional back-to-front method:
- Back-to-Front: ~12 minutes
- Outside-In: ~10 minutes
- Hybrid Strategy: ~10 minutes
- Random Boarding (baseline): ~22 minutes

## Repository Structure

- `visualizations/`: Seating charts and boarding strategy visualizations
- `models/`: Python code implementing the mathematical models
- `simulations/`: Simulation scripts and results for each boarding strategy