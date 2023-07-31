import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Global variables to store colors
pie_chart_colors = ['red', 'blue', 'green', 'yellow']
bar_graph_color = 'orange'
line_plot_color = 'purple'
scatter_plot_color = 'green'

def show_pie_chart():
    # Sample data for the pie chart
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]
    
    # Plot the pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=pie_chart_colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Sample Pie Chart')
    plt.show()

def show_bar_graph():
    # Sample data for the bar graph
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
    values = [20, 35, 25, 40]
    
    # Plot the bar graph
    plt.figure(figsize=(8, 6))
    plt.bar(categories, values, color=bar_graph_color)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Sample Bar Graph')
    plt.show()

def show_line_plot():
    # Sample data for the line plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Plot the line plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color=line_plot_color)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sample Line Plot')
    plt.grid(True)
    plt.show()

def show_scatter_plot():
    # Sample data for the scatter plot
    x = np.random.rand(50)
    y = np.random.rand(50)
    
    # Plot the scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color=scatter_plot_color, s=50)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sample Scatter Plot')
    plt.grid(True)
    plt.show()

def change_pie_chart_colors():
    global pie_chart_colors
    pie_chart_colors = ['purple', 'yellow', 'green', 'blue']

def change_bar_graph_color():
    global bar_graph_color
    bar_graph_color = 'blue'

def change_line_plot_color():
    global line_plot_color
    line_plot_color = 'orange'

def change_scatter_plot_color():
    global scatter_plot_color
    scatter_plot_color = 'red'

def on_pie_chart_click():
    change_pie_chart_colors()
    show_pie_chart()

def on_bar_graph_click():
    change_bar_graph_color()
    show_bar_graph()

def on_line_plot_click():
    change_line_plot_color()
    show_line_plot()

def on_scatter_plot_click():
    change_scatter_plot_color()
    show_scatter_plot()

def main():
    root = tk.Tk()
    root.title("Graph Display")
    
    # Create buttons to trigger the visualizations
    pie_chart_button = tk.Button(root, text="Click to Display Pie Chart", command=on_pie_chart_click)
    pie_chart_button.pack(pady=10)
    
    bar_graph_button = tk.Button(root, text="Click to Display Bar Graph", command=on_bar_graph_click)
    bar_graph_button.pack(pady=10)

    line_plot_button = tk.Button(root, text="Click to Display Line Plot", command=on_line_plot_click)
    line_plot_button.pack(pady=10)

    scatter_plot_button = tk.Button(root, text="Click to Display Scatter Plot", command=on_scatter_plot_click)
    scatter_plot_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
