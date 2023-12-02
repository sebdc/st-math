import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class MidPoint:

    def __init__(self, expression_str, a, b, n):
        self.expression = sp.sympify(expression_str)
        self.a = a
        self.b = b
        self.n = n

    def evaluate_expression(self, x_value):
        # Substitute the x value into the expression
        result = self.expression.subs('x', x_value)
        return result

    def midpoint_rule(self):
        # Calculate the width of each subinterval
        delta_x = (self.b - self.a) / self.n

        # Initialize the sum for the midpoint rule
        result = 0

        # Apply the midpoint rule formula
        for i in range(self.n):
            midpoint = self.a + (i + 0.5) * delta_x
            result += self.evaluate_expression(midpoint) * delta_x

        return result

    def calculateAndPlot(self):
        try:
            plt.clf()

            x_values = np.linspace(self.a, self.b, 100)
            y_values = [self.evaluate_expression(x) for x in x_values]

            # Plotting
            plt.plot(x_values, y_values, label=f'$f(x) = {self.expression}$')
            plt.bar(
                np.linspace(self.a, self.b, self.n + 1)[:-1] + (self.b - self.a) / (2 * self.n),
                [self.evaluate_expression(self.a + (i + 0.5) * (self.b - self.a) / self.n) for i in range(self.n)],
                width=(self.b - self.a) / self.n, alpha=0.5, label='Midpoint Rule'
            )
            plt.title('Midpoint Rule Visualization')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()
            plt.grid(True)
            plt.savefig("static/plot.png")
            plt.close()

        except( KeyError, ValueError) as e:
            print( e )  
            return 
        
'''
def main():

    expression_str = input("Enter the expression in terms of x (e.g., ln(x)*sin(x)*5**x): ")

    a = float(input("Enter the lower bound of the interval: "))
    b = float(input("Enter the upper bound of the interval: "))
    n = int(input("Enter the number of subintervals: "))

    x_values = np.linspace(a, b, 100)
    y_values = [evaluate_expression(sp.sympify(expression_str), x) for x in x_values]

    # Plotting
    plt.plot(x_values, y_values, label=f'$f(x) = {expression_str}$')
    plt.bar(np.linspace(a, b, n+1)[:-1] + (b-a)/(2*n), [evaluate_expression(sp.sympify(expression_str), (a + (i + 0.5) * (b-a)/n)) for i in range(n)], width=(b-a)/n, alpha=0.5, label='Midpoint Rule')
    plt.title('Midpoint Rule Visualization')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.savefig("static/plot.png")
'''