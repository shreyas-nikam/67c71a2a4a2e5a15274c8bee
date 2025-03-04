# Compound Interest Visualizer

## Description

This Streamlit application is an interactive tool designed to visualize the power of compound interest and compare it with simple interest. Users can adjust various investment parameters such as principal amount, annual interest rate, investment duration, and compounding frequency to see how their investment grows over time.

The application provides:
- **Interactive Parameter Adjustment:** Use sliders and input fields to modify investment parameters and observe real-time changes in the investment growth chart.
- **Visual Comparison:**  Clearly see the difference between compound interest and simple interest growth through an interactive line chart.
- **Educational Tool:** Understand the concepts of compound and simple interest with clear explanations and mathematical formulas provided within the application.
- **Future Value Calculation:**  View the calculated future value of your investment at each year for both compound and simple interest.

This application is perfect for anyone looking to understand the impact of compound interest on their investments and for educational purposes.

## Installation

To run this Streamlit application, you need to have Python installed on your system. Follow these steps to set up the environment and install the necessary libraries:

1.  **Install Python:** If you don't have Python installed, download it from the official Python website ([https://www.python.org](https://www.python.org)). It is recommended to use Python 3.8 or later.

2.  **Create a Virtual Environment (Optional but Recommended):**
    Open your terminal or command prompt and navigate to your project directory. Create a virtual environment to isolate project dependencies:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    -   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    -   **On macOS and Linux:**
        ```bash
        source venv/bin/activate
        ```

3.  **Install Streamlit and Matplotlib:**
    Use pip to install Streamlit and Matplotlib, which are required to run this application:

    ```bash
    pip install streamlit matplotlib
    ```

## Usage

1.  **Run the Application:**
    Navigate to the directory containing the Streamlit application file (e.g., `app.py`) in your terminal or command prompt. Run the application using the following command:

    ```bash
    streamlit run your_app_file.py
    ```
    Replace `your_app_file.py` with the actual name of your Python file containing the Streamlit code.

2.  **Interact with the Application:**
    Once the application is running, Streamlit will automatically open it in your default web browser. You will see the "Compound Interest Visualizer" application.

    -   **Sidebar Controls:**
        -   **Principal Amount:** Enter the initial investment amount (minimum $1000, step $1000).
        -   **Annual Interest Rate (%):** Adjust the annual interest rate using the slider (0.0% to 20.0%, step 0.5%).
        -   **Investment Duration (Years):** Set the number of years for the investment (1 to 30 years, step 1 year).
        -   **Compounding Frequency:** Choose between "Annually" or "Monthly" compounding.
        -   **Show Simple Interest Comparison:** Check the box to display a comparison with simple interest on the chart.

    -   **Visualization:**
        -   The main area of the application displays a line chart visualizing the growth of your investment over the selected duration.
        -   **Compound Interest (Blue Line):** Shows the future value of your investment with compound interest.
        -   **Simple Interest (Orange Dashed Line - Optional):**  If enabled, shows the future value with simple interest for comparison.
        -   **Annotations:** Each point on the chart is annotated with the future value at the end of that year.

    -   **Explanations:**
        -   The application provides explanations of both compound and simple interest, along with their respective formulas in LaTeX format for clarity.
        -   A chart explanation is also provided below the visualization to help interpret the graph.

3.  **Explore and Learn:**
    Experiment with different investment parameters and compounding frequencies to understand how they impact the final investment value. Observe the significant difference compound interest makes, especially over longer investment periods.

## Credits

This application is developed and provided by **QuantUniversity**.

[![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)](https://www.quantuniversity.com)

© 2025 QuantUniversity. All Rights Reserved.

## License

This demonstration is for educational use and illustration purposes only.

**All Rights Reserved.**

Any reproduction, redistribution, or commercial use of this application without prior written consent from QuantUniversity is strictly prohibited. For inquiries regarding licensing or reproduction, please contact QuantUniversity through their official website.

For full legal documentation, please visit [link to legal documentation - *replace with actual link if available*].

This application is intended solely for educational purposes.
