# Flyweight Pattern ✈️

Welcome to the Flyweight section of the Design Patterns repository! This directory contains an explanation of the Flyweight design pattern along with a code example in Python.

## What is the Flyweight Pattern? 🤔

The Flyweight Pattern is a structural design pattern that aims to minimize memory usage or computational expenses by sharing as much as possible with similar objects. It achieves this by storing common states externally and passing them to the objects instead of storing them internally. This pattern is useful when you need to create a large number of similar objects and memory consumption or performance is a concern.

### 1. Problem ❌

In a software application, there are often scenarios where you need to create a large number of objects that share common state or properties. However, creating and maintaining separate instances for each object can lead to high memory usage and decreased performance, especially when dealing with large datasets or frequent object creation.

### 2. Solution ✅

The Flyweight Pattern solves this problem by separating **intrinsic (shared)** and **extrinsic (unique)** states of objects. It stores intrinsic states externally and passes them to the objects when needed, allowing multiple objects to share the same state. This reduces memory consumption and improves performance by eliminating redundant storage of common state information.

## When to Use the Flyweight Pattern

Consider using the Flyweight Pattern in the following situations:

- When you need to create a large number of objects that share common state or properties.
- When memory consumption or performance is a concern, especially in resource-constrained environments.
- When you want to minimize memory usage by storing common state externally and passing it to objects.

## Structure of the Flyweight Pattern

The Flyweight Pattern typically consists of the following components:

1. **Concrete Flyweight**: Stores intrinsic state (shared) that can be shared across multiple objects. Can receive and act on extrinsic states.
2. **Flyweight Factory**: Manages flyweight objects and ensures that flyweights are shared and reused properly.
3. **Client**: Maintains references to flyweights and provides extrinsic states when necessary.

## Example Code 🧑‍💻

This repository provides example implementations of the Flyweight Pattern in various programming languages, including:

- [Python](./python-example.py)

Feel free to explore the code and experiment with it.
