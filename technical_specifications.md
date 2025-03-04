# Compound Interest Visualizer Streamlit Application

## Overview
This project involves developing a one-page Streamlit application named **Compound Interest Visualizer**. The goal is to demonstrate the mechanics and power of compound interest through interactive data visualization and computations. Users will gain an understanding of how compound interest accumulates earnings on principals and prior interest, contrasting it with simple interest growth, highlighting its significance in long-term investing. This aligns with the learning outcomes by enabling users to transform raw data into interactive visualizations and comprehend data preprocessing and exploration through synthetic datasets.

## Specifications

### User Inputs
- **Principal Amount**: A numeric input box for users to enter the initial amount of money to be invested.
- **Annual Interest Rate (%)**: A numeric input slider allowing users to choose the annual interest rate percentage, typically ranging from 0% to 20%.
- **Investment Duration**: A numeric input slider for users to select the number of years the money will be invested.
- **Compounding Frequency**: A dropdown menu offering options for monthly or annual compounding.

### Calculations
- **Future Value with Compound Interest**: Implement the compound interest formula:  
  \[
  FV = P \times (1 + \frac{r}{n})^{nt}
  \]
  where:
  - \(FV\) = future value of the investment,
  - \(P\) = principal amount,
  - \(r\) = annual interest rate (as a decimal),
  - \(n\) = number of times interest is compounded per year,
  - \(t\) = number of years the money is invested.
  
- **Future Value with Simple Interest**: Implement the simple interest formula:  
  \[
  FV = P \times (1 + r \times t)
  \]

### Visualizations
- **Interactive Line Chart**: Plot both simple and compound interest over time. The x-axis represents the investment duration in years, while the y-axis depicts the growth of the investment.
  - **Annotations**: Mark key points such as the end of each year to show total values. 
  - **Tooltips**: Display precise data values when hovering over the graph.

### User Interaction
- **Parameter Adjustment**: Allow users to adjust inputs and see real-time updates in the chart, providing immediate visualization of how changes affect outcome.
- **Checkbox**: An option to switch between displaying only compound interest or both compound and simple interest on the chart for clearer comparison.
- **Inline Help & Tooltips**: Comprehensive in-app documentation delivered via tooltips and a help section guiding users through using the app and understanding outputs.

### Dataset Details
- **Type**: Synthetic 
- **Purpose**: The synthetic dataset will help simulate realistic data structures and dynamics, showcasing the effect of variable manipulation on resulting graphs. This facilitates learning in a controlled simulation environment.

### Learning Outcomes
- Users will understand the mathematical and graphical difference between simple and compound interest.
- Gain skills in using Streamlit to transform data inputs into visual insights.
- Explore data preprocessing concepts by adjusting and observing the parameters’ influence on investment growth through a synthetic dataset.

### References
- The learning outcomes emphasize transforming real data concepts into a practical application, referenced by understanding financial growth mechanism as detailed in documents relating to fundamentals of investing.

This project aims to provide an intuitive and interactive experience that blends data science with financial literacy, supporting users to gain actionable insights into compound interest's role in wealth accumulation.