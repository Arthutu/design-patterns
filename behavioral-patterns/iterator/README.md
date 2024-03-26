# Iterator Pattern 🔄

Welcome to the Iterator section of the Design Patterns repository! This directory contains an explanation of the Iterator design pattern along with a code example in Python.

## What is the Iterator Pattern? 🤔

The Iterator Pattern is a behavioral design pattern that provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. It separates the traversal of a collection from the collection itself, allowing for different traversal methods to be implemented independently of the collection. This pattern is useful when you want to iterate over the elements of a collection without exposing its internal structure.

### 1. Problem ❌

In a software application, there are often scenarios where you need to iterate over the elements of a collection or aggregate object. However, directly accessing the elements of the collection can lead to tightly coupled code and violate the encapsulation principle. Additionally, different clients may require different traversal methods or algorithms, making it difficult to reuse the code.

### 2. Solution ✅

The Iterator Pattern solves this problem by providing a separate object, called an iterator, that encapsulates the traversal of a collection. It defines a common interface for iterating over the elements of a collection, allowing clients to access the elements sequentially without knowing the specifics of the collection's implementation. This allows for flexible traversal methods to be implemented independently of the collection, promoting code reuse and maintainability.

## When to Use the Iterator Pattern

Consider using the Iterator Pattern in the following situations:

- When you want to access the elements of a collection sequentially without exposing its internal structure.
- When you need to provide a common interface for iterating over different types of collections.
- When you want to decouple the traversal of a collection from the collection itself, allowing for different traversal methods to be implemented independently.

## Structure of the Iterator Pattern

The Iterator Pattern typically consists of the following components:

1. **Iterator**: Defines an interface for accessing and traversing the elements of a collection.
2. **ConcreteIterator**: Implements the Iterator interface and keeps track of the current position in the traversal of the collection.
3. **Aggregate**: Defines an interface for creating an iterator object.
4. **ConcreteAggregate**: Implements the Aggregate interface and provides an iterator object for traversing its elements.

## Example Code 🧑‍💻

This repository provides example implementations of the Iterator Pattern in various programming languages, including:

- [Python](./python-example.py)

Feel free to explore the code and experiment with it.
