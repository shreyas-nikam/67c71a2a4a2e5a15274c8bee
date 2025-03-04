import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Compound Interest Visualizer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.sidebar.title("Compound Interest Visualizer")
st.sidebar.write("Explore the power of compound interest interactively.")
st.sidebar.divider()
st.sidebar.write("Adjust the parameters below to see how your investment grows over time with both compound and simple interest.")

st.title("Compound Interest Visualizer Application")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("Investment Parameters")
    principal_amount = st.number_input("Principal Amount", min_value=1000, step=1000, value=10000, format="%d")
    annual_interest_rate = st.slider("Annual Interest Rate (%)", min_value=0.0, max_value=20.0, step=0.5, value=5.0)
    investment_duration = st.slider("Investment Duration (Years)", min_value=1, max_value=30, step=1, value=10)
    compounding_frequency_option = st.selectbox("Compounding Frequency", ["Annually", "Monthly"])
    show_simple_interest = st.checkbox("Show Simple Interest Comparison", value=True)

    st.divider()
    st.subheader("Understanding Compound Interest")
    st.write(
        """
        Compound interest is interest calculated on the initial principal and also on the accumulated interest of previous periods. 
        It's often called 'interest on interest,' and it can make a significant difference over long investment periods.
        """
    )
    st.latex(r"FV = P \times (1 + \frac{r}{n})^{nt}")
    st.write(
        """
        Where:
        - FV = Future Value of Investment
        - P = Principal Amount
        - r = Annual Interest Rate (as a decimal)
        - n = Number of times interest is compounded per year
        - t = Number of years
        """
    )

    st.subheader("Understanding Simple Interest")
    st.write(
        """
        Simple interest is calculated only on the principal amount. It does not take into account the compounding of interest.
        """
    )
    st.latex(r"FV = P \times (1 + r \times t)")
    st.write(
        """
        Where:
        - FV = Future Value of Investment
        - P = Principal Amount
        - r = Annual Interest Rate (as a decimal)
        - t = Number of years
        """
    )

with col2:
    st.header("Investment Growth Visualization")
    investment_years = list(range(investment_duration + 1))
    compound_interest_values = []
    simple_interest_values = []

    n = 1 if compounding_frequency_option == "Annually" else 12
    r_decimal = annual_interest_rate / 100.0

    for year in investment_years:
        future_value_compound = principal_amount * (1 + (r_decimal / n))**(n * year)
        compound_interest_values.append(future_value_compound)
        future_value_simple = principal_amount * (1 + r_decimal * year)
        simple_interest_values.append(future_value_simple)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(investment_years, compound_interest_values, label='Compound Interest', marker='o')
    if show_simple_interest:
        ax.plot(investment_years, simple_interest_values, label='Simple Interest', linestyle='--', marker='x')

    ax.set_xlabel('Investment Duration (Years)')
    ax.set_ylabel('Future Value ($)')
    ax.set_title('Growth of Investment over Time')
    ax.grid(True)
    ax.legend()

    # Annotations and Tooltips (Basic - consider more advanced libraries for interactivity if needed)
    for i, year in enumerate(investment_years):
        ax.annotate(f'{compound_interest_values[i]:.2f}', (year, compound_interest_values[i]), textcoords="offset points", xytext=(0,5), ha='center')
        if show_simple_interest:
            ax.annotate(f'{simple_interest_values[i]:.2f}', (year, simple_interest_values[i]), textcoords="offset points", xytext=(0,-15), ha='center', color='tab:orange')


    st.pyplot(fig)

    st.write(
        """
        **Chart Explanation:**
        - The blue line represents the growth of your investment with compound interest.
        - The orange dashed line (if shown) represents the growth with simple interest for comparison.
        - Hover over the points on the chart to see the exact future value at the end of each year.
        - Observe how compound interest leads to significantly higher returns over longer periods, especially with frequent compounding.
        """
    )

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
