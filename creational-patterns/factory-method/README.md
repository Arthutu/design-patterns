# Factory Method 🏭

Welcome to the Factory Method section of the Design Patterns repository! This directory contains an explanation of the Factory Method design pattern along with code examples in python.

## What is the Factory Method? 🤔

The Factory Method is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. It encapsulates object creation logic into a separate method, thereby promoting loose coupling and ensuring the [open/closed principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle).

In essence, the Factory Method defines an interface for creating an object but allows subclasses to alter the type of object that will be created.

### 1. Problem ❌

Imagine a software application that needs to load different types of documents, such as text documents, spreadsheets, and presentations. Each document type requires a specific parser to read its contents. Without the Factory Method, the application might have complex conditional statements to determine the type of document to load and which parser to use.

### 2. Solution ✅

The Factory Method solves this problem by providing a framework for creating objects without specifying their exact class. Instead of directly instantiating document parsers in the application code, the application defines a factory method for creating parsers. Each document type subclass overrides this factory method to instantiate the appropriate parser for that type.

## When to Use the Factory Method? 💡

Consider using the Factory Method in the following situations:

- When a class cannot anticipate the class of objects it needs to create.
- When a class wants its subclasses to specify the objects it creates.
- When a class needs to delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate.

## Structure of the Factory Method 🗂️

The Factory Method typically consists of the following components:

1. **Product**: Defines the interface of objects the factory method creates.
2. **Concrete Product**: Implements the Product interface.
3. **Creator**: Declares the factory method, which returns an object of type Product. This may also define a default implementation of the factory method that returns a default Concrete Product.
4. **Concrete Creator**: Overrides the factory method to return an instance of a specific Concrete Product.

## Example Code 🧑‍💻

This repository provides example implementations of the Factory Method in [python](./python-example.py). Feel free to explore the code and experiment with it.
