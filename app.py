import os

from flask import (
    Flask,
    render_template,
    request,
    send_file
)
from src.preprocessing import load_and_clean_data

from src.feature_engineering import create_features

from src.anomaly_detection import (
    detect_rule_based_anomalies,
    detect_isolation_forest_anomalies,
    create_hybrid_anomaly
)
from src.visualization import (
    create_anomaly_plot,
    create_severity_pie_chart,
    create_usage_heatmap,
    create_interactive_anomaly_plot
)
from src.severity import (
    classify_anomaly_severity
)
from src.insights import (
    generate_ai_insights
)
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():

    if 'dataset' not in request.files:
        return "No file uploaded"

    file = request.files['dataset']

    if file.filename == '':
        return "No selected file"

    file_path = os.path.join(
        app.config['UPLOAD_FOLDER'],
        file.filename
    )

    file.save(file_path)

    # ML PIPELINE

    df = load_and_clean_data(file_path)

    df = create_features(df)

    df = detect_rule_based_anomalies(df)

    df = detect_isolation_forest_anomalies(df)

    df = create_hybrid_anomaly(df)
    df = classify_anomaly_severity(df)
    insights = generate_ai_insights(df)
    hybrid_anomalies = df[
        df['Hybrid_Anomaly'] == True
    ]
    report_path = (
    'outputs/anomaly_report.csv'
    )

    hybrid_anomalies.to_csv(
        report_path
    )
    plot_path = create_anomaly_plot(
        df,
        hybrid_anomalies
    )
    pie_chart_path = (
    create_severity_pie_chart(df)
)
    heatmap_path = (
    create_usage_heatmap(df)
)
    interactive_plot = (
    create_interactive_anomaly_plot(df)
)
    high_count = len(
    df[df['Severity'] == 'High']
)

    medium_count = len(
        df[df['Severity'] == 'Medium']
    )

    low_count = len(
        df[df['Severity'] == 'Low']
    )
    top_anomalies = (
    df[df['Hybrid_Anomaly'] == True]
    .sort_values(
        by='Anomaly_Score',
        ascending=False
    )
    .head(10)
)
    # RESULTS

    total_records = len(df)

    rule_anomalies = (
        df['Rule_Based_Anomaly'].sum()
    )

    ml_anomalies = (
        (df['IF_Anomaly'] == -1).sum()
    )

    hybrid_anomalies = (
        df['Hybrid_Anomaly'].sum()
    )

    return render_template(

        'results.html',

        total_records=total_records,

        rule_anomalies=rule_anomalies,

        ml_anomalies=ml_anomalies,

        hybrid_anomalies=hybrid_anomalies,

        plot_path=plot_path,high_count=high_count,
        medium_count=medium_count,
        low_count=low_count,
        pie_chart_path=pie_chart_path,
        heatmap_path=heatmap_path,
        insights=insights,
        interactive_plot=interactive_plot,
        top_anomalies=top_anomalies,
    )
@app.route('/download-report')
def download_report():

    report_path = (
        'outputs/anomaly_report.csv'
    )

    return send_file(
        report_path,
        as_attachment=True
    )

if __name__ == '__main__':

        app.run(debug=True)