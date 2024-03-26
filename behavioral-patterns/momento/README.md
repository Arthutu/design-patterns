# Memento Pattern 🕰️

Welcome to the Memento section of the Design Patterns repository! This directory contains an explanation of the Memento design pattern along with a code example in Python.

## What is the Memento Pattern? 🤔

The Memento Pattern is a behavioral design pattern that allows the capture and externalization of an object's internal state so that the object can be restored to this state later. It encapsulates the internal state of an object into a memento object, which can be stored, passed around, or used to restore the object's state. This pattern is useful when you need to implement undo functionality, save and restore object states, or provide snapshots of an object's state.

### 1. Problem ❌

In a software application, there are often scenarios where you need to save and restore the state of an object. However, directly exposing the internal state of an object or tightly coupling the object with the mechanism for saving and restoring its state can lead to violations of encapsulation and code complexity. Additionally, managing the history of an object's state and implementing undo functionality can be challenging.

### 2. Solution ✅

The Memento Pattern solves this problem by providing a way to capture and externalize an object's internal state without exposing its implementation details. It defines three key components: the Originator, which creates and restores the state from a memento object; the Memento, which encapsulates the internal state of the originator; and the Caretaker, which manages the history of memento objects. This allows for flexible management of object states, implementation of undo functionality, and support for snapshots of an object's state.

## When to Use the Memento Pattern

Consider using the Memento Pattern in the following situations:

- When you need to capture and externalize an object's internal state without exposing its implementation details.
- When you want to implement undo functionality or provide snapshots of an object's state.
- When you need to save and restore object states in a flexible and decoupled manner.

## Structure of the Memento Pattern

The Memento Pattern typically consists of the following components:

1. **Originator**: Creates and restores the state from a memento object.
2. **Memento**: Encapsulates the internal state of the originator.
3. **Caretaker**: Manages the history of memento objects.

## Example Code 🧑‍💻

This repository provides example implementations of the Memento Pattern in various programming languages, including:

- [Python](./python-example.py)

Feel free to explore the code and experiment with it.
