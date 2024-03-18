# Decorator Pattern 🪆

Welcome to the Decorator section of the Design Patterns repository! This directory contains an explanation of the Decorator design pattern along with a code example in Python.

## What is the Decorator Pattern? 🤔

The Decorator Pattern is a structural design pattern that allows behavior to be added to individual objects dynamically, without affecting the behavior of other objects from the same class. It provides a flexible alternative to subclassing for extending functionality. This pattern is useful when you need to add or remove responsibilities from objects at runtime.

### 1. Problem ❌

In a software application, there are often situations where you need to add new features or behaviors to objects dynamically. However, traditional inheritance-based approaches, such as subclassing, can lead to a proliferation of subclasses and tight coupling between classes. Additionally, modifying existing classes to accommodate new features can be difficult and error-prone.

### 2. Solution ✅

The Decorator Pattern solves this problem by allowing behavior to be added to individual objects dynamically through composition. It involves creating a set of decorator classes that wrap the original object and provide additional functionality. Decorators can be stacked on top of each other, allowing multiple features to be added or removed independently. This promotes code reuse, flexibility, and maintainability.

## When to Use the Decorator Pattern

Consider using the Decorator Pattern in the following situations:

- When you need to add or remove responsibilities from objects dynamically.
- When you want to avoid a proliferation of subclasses to accommodate new features.
- When you want to extend the behavior of individual objects without affecting other objects from the same class.

## Structure of the Decorator Pattern

The Decorator Pattern typically consists of the following components:

1. **Component**: Defines the interface for objects that can have responsibilities added or removed dynamically.
2. **Concrete Component**: Represents the core object to which responsibilities can be added.
3. **Decorator**: Maintains a reference to a Component object and defines an interface that conforms to the Component's interface.
4. **Concrete Decorator**: Adds additional responsibilities to the Component dynamically.

## Example Code 🧑‍💻

This repository provides example implementations of the Decorator Pattern in various programming languages, including:

- [Python](./python-example.py)

Feel free to explore the code and experiment with it.
