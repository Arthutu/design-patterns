# Command Pattern ⚔️

Welcome to the Command section of the Design Patterns repository! This directory contains an explanation of the Command design pattern along with a code example in Python.

## What is the Command Pattern? 🤔

The Command Pattern is a behavioral design pattern that encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations. It allows for the decoupling of senders and receivers of requests, supporting undoable operations, and supporting operations that can be delayed or queued. This pattern is useful when you want to parameterize objects with operations, queue requests, or support undoable operations.

### 1. Problem ❌

In a software application, there are often scenarios where you need to parameterize objects with operations or encapsulate requests as objects. However, directly coupling the sender of a request to its receiver can lead to inflexible designs and make it difficult to support operations such as undo or redo. Additionally, managing the lifecycle of command objects and coordinating their execution can be challenging.

### 2. Solution ✅

The Command Pattern solves this problem by encapsulating a request as an object, allowing for the parameterization of clients with queues, requests, and operations. It defines a common interface for all command objects, allowing clients to invoke commands without knowing the specifics of their implementation. This allows for flexible composition of commands, queueing of requests, and support for undoable operations.

## When to Use the Command Pattern

Consider using the Command Pattern in the following situations:

- When you want to parameterize objects with operations or encapsulate requests as objects.
- When you need to support undoable operations or operations that can be delayed or queued.
- When you want to decouple senders and receivers of requests and support flexible composition of commands.

## Structure of the Command Pattern

The Command Pattern typically consists of the following components:

1. **Command**: Defines an interface for executing a request.
2. **ConcreteCommand**: Implements the Command interface and encapsulates a request as an object.
3. **Invoker**: Asks the command to carry out the request.
4. **Receiver**: Knows how to perform the operations associated with carrying out a request.

## Example Code 🧑‍💻

This repository provides example implementations of the Command Pattern in various programming languages, including:

- [Python](./python-example.py)

Feel free to explore the code and experiment with it.
