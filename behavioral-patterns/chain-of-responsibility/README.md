# Chain of Responsibility Pattern ⛓️

Welcome to the Chain of Responsibility section of the Design Patterns repository! This directory contains an explanation of the Chain of Responsibility design pattern along with a code example in Python.

## What is the Chain of Responsibility Pattern? 🤔

The Chain of Responsibility Pattern is a behavioral design pattern that allows multiple objects to handle a request without the sender needing to know which object will handle it. It forms a chain of handlers, where each handler either handles the request or passes it to the next handler in the chain. This pattern is useful when you want to decouple senders and receivers of requests and provide flexibility in handling requests.

### 1. Problem ❌

In a software application, there are often scenarios where you need to handle a request through a series of handlers or processors. However, hard-coding the sequence of handlers or processors into the client code can lead to inflexible and tightly coupled designs. Additionally, modifying the sequence of handlers or processors requires changes to the client code, violating the [open/closed principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle).

### 2. Solution ✅

The Chain of Responsibility Pattern solves this problem by decoupling senders and receivers of requests and forming a chain of handlers. Each handler in the chain has the ability to handle the request or pass it to the next handler in the chain. This allows for flexible composition of handlers and dynamic handling of requests without modifying the client code.

## When to Use the Chain of Responsibility Pattern

Consider using the Chain of Responsibility Pattern in the following situations:

- When you want to decouple senders and receivers of requests and provide flexibility in handling requests.
- When you need to handle a request through a series of handlers or processors without hard-coding the sequence into the client code.
- When you want to avoid coupling the sender of a request to its receiver, allowing multiple objects to handle the request independently.

## Structure of the Chain of Responsibility Pattern

The Chain of Responsibility Pattern typically consists of the following components:

1. **Handler**: Defines an interface for handling requests and optionally implements a successor link.
2. **ConcreteHandler**: Implements the Handler interface and handles requests it is responsible for. It may also pass requests to its successor.
3. **Client**: Initiates requests to the first handler in the chain.

## Example Code 🧑‍💻

This repository provides example implementations of the Chain of Responsibility Pattern in various programming languages, including:

- [Python](./python-example.py)

Feel free to explore the code and experiment with it.
