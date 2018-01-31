Title: Code
Date: 2017-02-01

## Goals

This station is a top-down introduction to some important programming concepts. Rather than learning the
nitty-gritty of a language, you will start with a working game, read the source code, and discuss design
considerations for your own programming. Key concepts include:

- **Model/view architecture**: Models should manage a program's state; views should manage rendering and
  user interacation. 
- **Modularity**: Small, resuable components with clear interfaces.
- **State**: A complete representation of what's happening in the app at any given time. 

Also, some more focused concepts:

- **Tick-based time model**: Complex systems are much easier to model when you break time into discrete steps
  and describe how they move from one moment to the next.
- **Frames and multiple coordinate systems**: We use some tricks to move between different coordinate systems.
- **Event models**: You can manage interactivity by creating objects that represent things that happen.
- **Coding style**: Lots of little tips that you can best learn by reading others' code.

## Preparation

- Download and install [Processing](https://processing.org/)
- Download version 1 of the [Hospitals game](https://github.com/cproctor/hospitals/releases)
- Open the [annotated source code](https://cproctor.github.io/hospitals/hospitals.html)

## Tangible User Interface Tables
For today's purposes, you will use the tangible user interface tables as a learning tool. 
We will teach you how to use the tangible interface tables in more detail later, but if you don't
want to wait:

- [Read about how tangible interface tables work]({filename}/modules/tangible-tables.md). Follow the setup instructions to install reacTIVision and the TUIO Processing library.
- Download version 2 of the [Hospitals game](https://github.com/cproctor/hospitals/releases)
- Read the [annotated source code](https://cproctor.github.io/hospitals/hospitals_tuio.html) for the TUIO version.

