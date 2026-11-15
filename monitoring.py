
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Reference data
reference_data = pd.DataFrame({
    "num1": [10, 20, 30, 40, 50],
    "num2": [5, 10, 15, 20, 25]
})

# Current data
current_data = pd.DataFrame({
    "num1": [100, 200, 300, 400, 500],
    "num2": [50, 100, 150, 200, 250]
})

# Generate data drift report
report = Report([
    DataDriftPreset()
])

result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

# Save HTML report
result.save_html("drift_report.html")

print("Evidently report generated successfully!")
