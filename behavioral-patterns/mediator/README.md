# Mediator Pattern 🤝

Welcome to the Mediator section of the Design Patterns repository! This directory contains an explanation of the Mediator design pattern along with a code example in Python.

## What is the Mediator Pattern? 🤔

The Mediator Pattern is a behavioral design pattern that defines an object that encapsulates how a set of objects interact. It promotes loose coupling by keeping objects from referring to each other explicitly and allowing them to communicate through the mediator object. This pattern is useful when the communication between objects becomes complex or when objects need to be decoupled from each other.

### 1. Problem ❌

In a software application, there are often scenarios where multiple objects need to communicate with each other. However, directly coupling these objects together can lead to tight dependencies and make the code difficult to maintain and extend. Additionally, modifying the communication between objects requires changes to multiple classes, violating the single responsibility principle.

### 2. Solution ✅

The Mediator Pattern solves this problem by defining a mediator object that encapsulates the communication between objects. It promotes loose coupling by keeping objects from referring to each other explicitly and instead allowing them to communicate through the mediator. This allows for easier maintenance and extension of the code, as changes to the communication logic can be made in the mediator object without affecting the individual objects.

## When to Use the Mediator Pattern

Consider using the Mediator Pattern in the following situations:

- When multiple objects need to communicate with each other, but direct coupling between them leads to tight dependencies.
- When changes to the communication logic between objects need to be localized and encapsulated.
- When you want to promote loose coupling and enhance the maintainability and extensibility of the code.

## Structure of the Mediator Pattern

The Mediator Pattern typically consists of the following components:

1. **Mediator**: Defines an interface for communicating with colleague objects.
2. **ConcreteMediator**: Implements the Mediator interface and coordinates communication between colleague objects.
3. **Colleague**: Defines an interface for interacting with other colleagues through the mediator.
4. **ConcreteColleague**: Implements the Colleague interface and communicates with other colleagues through the mediator.

## Example Code 🧑‍💻

This repository provides example implementations of the Mediator Pattern in various programming languages, including:

- [Python](./python-example.py)

Feel free to explore the code and experiment with it.
