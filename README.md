# Numerical Methods for Root Finding

This project implements several numerical methods for finding the roots of functions. It includes the following methods:

- **Bisection Method**
- **Secant Method**
- **Iteration Method**
- **Newton-Raphson Method**

## Table of Contents

- [Introduction](#introduction)
- [Methods](#methods)
  - [Bisection Method](#bisection-method)
  - [Secant Method](#secant-method)
  - [Iteration Method](#iteration-method)
  - [Newton-Raphson Method](#newton-raphson-method)
- [Usage](#usage)

## Introduction

Root finding is a fundamental problem in numerical analysis. These methods are used to locate roots of real-valued functions. Each method has its own advantages and is suited for different types of problems.

## Methods

### Bisection Method

The Bisection Method is a bracketing method that repeatedly bisects an interval and selects a subinterval in which a root must lie. It requires two initial points, \(x_0\) and \(x_1\), such that \(f(x_0)\) and \(f(x_1)\) have opposite signs.

### Secant Method

The Secant Method uses two initial approximations to approximate the root of the function. It uses the formula based on the line connecting two points on the function graph. Unlike the Bisection Method, it does not require the function to change signs.

### Iteration Method

The Iteration Method (or Fixed-Point Iteration) involves rearranging the equation \(f(x) = 0\) into the form \(x = g(x)\). The method iteratively substitutes the previous value to converge to the root.

### Newton-Raphson Method

The Newton-Raphson Method is an iterative root-finding algorithm that uses the function's derivative. It starts with an initial guess and iteratively improves the approximation using the formula:
\[ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \]

## Usage

To use any of these methods, simply call the respective function with the appropriate parameters. Each function is designed to compute the root of the specified function using the method described.
