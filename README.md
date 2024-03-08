# Variatio

Variatio is an experimental Python library designed for advanced A/B testing analysis. It leverages statistical techniques and machine learning, including variance reduction through CUPED and integration with CatBoost for predictive insights. Variatio is ideal for data scientists and researchers looking to obtain deeper insights from their A/B testing efforts.

## Features

- Statistical Significance Testing: Compare metrics between control and test groups easily.
- CUPED Adjustments: Use Controlled-experiment Using Pre-Experiment Data (CUPED) techniques for variance reduction.
- Machine Learning Integration: Leverage CatBoost for predictive modeling and insights.

## Installation

Install Variatio directly from the source:

```bash
git clone https://github.com/dmitry_brazhenko/Variatio.git
cd Variatio
pip install .
```

## Quick Start

Here's how to use Variatio to analyze A/B testing data:

```python
from Variatio import calculate_cuped_and_compare
import pandas as pd

# Example data tables
event_data = pd.DataFrame({
    'timestamp': ['2023-01-01 00:00:00', '2023-01-01 01:00:00', '2023-01-01 02:00:00', '2023-01-01 03:00:00', '2023-01-01 04:00:00'],
    'userid': [7, 4, 5, 7, 3],
    'event_name': ['purchase', 'purchase', 'purchase', 'purchase', 'login'],
    'purchase_value': [274, 175, 179, 102, 0]
})

user_properties = pd.DataFrame({
    'userid': [1, 2, 3, 4, 5],
    'age': [56, 69, 46, 32, 60],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'country': ['USA', 'India', 'Australia', 'UK', 'Germany'],
    'device_type': ['Tablet', 'Mobile', 'Tablet', 'Tablet', 'Tablet'],
    'membership_status': ['Free', 'Free', 'Free', 'Free', 'Free']
})

user_allocations = pd.DataFrame({
    'timestamp': ['2022-12-15', '2022-12-16', '2022-12-17', '2022-12-18', '2022-12-19'],
    'userid': [1, 2, 3, 4, 5],
    'abgroup': ['A', 'B', 'B', 'B', 'A']
})

# Define your groups
control_group = 'A'
test_groups = ['B']

# Perform analysis
results = calculate_cuped_and_compare(event_data, user_allocations, user_properties, control_group, test_groups)

print(results)
```

## Contributing

Contributions to Variatio are welcome! Here are ways you can contribute:

- Fork the repository and submit a pull request.
- Report bugs or suggest features by opening an issue.
- Improve documentation for better understanding.

Please follow our contribution guidelines for a smooth collaboration process.

## License

Variatio is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

## Disclaimer

Variatio is an experimental tool provided "as is", without warranty of any kind. Use it at your own risk.
