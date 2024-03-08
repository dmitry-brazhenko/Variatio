def format_metrics_to_html(metrics, control_group, test_groups):
    # Incorporating CSS styles directly within the HTML output
    html = """
    <html>
    <head>
        <style>
            .significant { background-color: #4CAF50; color: white; }
            .moderate { background-color: #8BC34A; color: white; }
            .insignificant { background-color: #F44336; color: white; }
            .neutral { background-color: #FFC107; color: black; }
            td:hover::after {
                content: attr(data-significance);
                position: absolute;
                margin-left: 10px;
                white-space: nowrap;
                border: 1px solid #ddd;
                background-color: #f9f9f9;
                padding: 5px;
                z-index: 1;
            }
        </style>
    </head>
    <body>
    <table border='1'>
    <tr><th>Metric Type</th><th>Parameters</th><th>Control Group Value</th>"""

    # Adding headers for test groups with additional columns for differences
    for group in test_groups:
        html += f"<th>{group} Value</th><th>{group} Diff</th><th>{group} Diff (%)</th>"
    html += "</tr>"

    for metric in metrics:
        data = metric.result.data
        significance_data = metric.result.stat_significance

        # Extract parameters for display
        param_details = ', '.join(
            [f'{key}: {value}' for key, value in metric.metricparams.__dict__.items() if value is not None])

        # Metric type and parameters
        html += f"<tr><td>{metric.metrictype.name}</td>"
        html += f"<td>{param_details}</td>"
        html += f"<td>{data[control_group]:.2f}</td>"

        # Control and Test group values, with significance coloring
        for group in test_groups:
            p_value = significance_data.get(group, 1)  # Default p-value to 1 if not found
            cell_class = "significant" if p_value < 0.05 else "moderate" if p_value < 0.1 else "insignificant"
            test_val = data.get(group, 0)
            diff = test_val - data[control_group]
            diff_percentage = (diff / data[control_group] * 100) if data[control_group] else 0
            html += f"<td class='{cell_class}' data-significance='p-value: {p_value:.4f}'>{test_val:.2f}</td>"
            html += f"<td class='{cell_class}'>{diff:+.2f}</td>"
            html += f"<td class='{cell_class}'>{diff_percentage:+.2f}%</td>"

        html += "</tr>"

    html += "</table>"
    html += "</body></html>"
    return html
