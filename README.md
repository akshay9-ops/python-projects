# Python Projects Portfolio

A collection of Python projects I've built while learning — spanning scripting, OOP, and Turtle graphics. Each project lives in its own folder with its own entry point.

## Projects

| Project | Description | Concepts |
|---|---|---|
| [100-Days-of-Python](100-Days-of-Python) | Daily solutions from Angela Yu's "100 Days of Code" bootcamp — calculators, games, a password generator, a blind auction app, and more. See its own [README](100-Days-of-Python/README.md) for the full day-by-day index. | Fundamentals through intermediate Python |
| [OOP-coffee-machine](OOP-coffee-machine) | A coffee vending machine simulator refactored into classes (`CoffeeMaker`, `MoneyMachine`, `Menu`) instead of one procedural script. | OOP, separation of concerns |
| [CoffeeMachine](CoffeeMachine) | The earlier procedural version of the coffee machine simulator — menu-driven, tracks resources and cost per drink. | Dictionaries, control flow |
| [hirst-painting](hirst-painting) | Recreates Damien Hirst's dot painting style using Turtle graphics and a sampled color palette. | Turtle graphics, generative art |
| [day-19](day-19) | A turtle race game — pick a color and watch turtles race to the finish line. | Turtle graphics, randomness |
| [day-18](day-18) | A spirograph generator drawing colorful geometric patterns with Turtle. | Turtle graphics, loops |
| [day-17-start](day-17-start) | A `User` class modeling followers/following relationships, with unit tests. | OOP, testing |
| [day-16-start](day-16-start) | Practice with classes and importing across modules. | OOP, modules |

## Running a project

Each folder is self-contained. From inside a project's folder:

```bash
python main.py
```

Some projects (Turtle-based ones) open a GUI window, so they need to run locally rather than in a browser sandbox.

## Tech

Python 3, with the standard library (`turtle`, `random`, etc.) — no external dependencies unless noted inside a specific project folder.
