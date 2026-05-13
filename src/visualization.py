import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
def create_anomaly_plot(df, anomalies):

    plt.figure(figsize=(15,5))

    plt.plot(
        df.index[:5000],
        df['Global_active_power'][:5000],
        label='Electricity Usage'
    )

    plt.scatter(
        anomalies.index[:100],
        anomalies['Global_active_power'][:100],
        color='red',
        label='Anomalies'
    )

    plt.title(
        "Electricity Consumption with Anomalies"
    )

    plt.xlabel("Time")

    plt.ylabel("Global Active Power")

    plt.legend()

    plot_path = (
        'static/plots/anomaly_plot.png'
    )

    plt.savefig(plot_path)

    plt.close()

    return plot_path
def create_severity_pie_chart(df):

    severity_counts = (
        df['Severity']
        .value_counts()
    )

    plt.figure(figsize=(6,6))

    plt.pie(
        severity_counts,
        labels=severity_counts.index,
        autopct='%1.1f%%'
    )

    plt.title(
        "Severity Distribution"
    )

    plot_path = (
        'static/plots/severity_pie.png'
    )

    plt.savefig(plot_path)

    plt.close()

    return plot_path
def create_usage_heatmap(df):

    heatmap_data = (
        df.groupby(['Weekday', 'Hour'])
        ['Global_active_power']
        .mean()
        .unstack()
    )

    plt.figure(figsize=(12,6))

    sns.heatmap(
        heatmap_data,
        cmap='YlOrRd'
    )

    plt.title(
        "Electricity Usage Heatmap"
    )

    plot_path = (
        'static/plots/heatmap.png'
    )

    plt.savefig(plot_path)

    plt.close()

    return plot_path
def create_interactive_anomaly_plot(df):

    plot_df = df.iloc[:5000].copy()

    plot_df['Anomaly_Label'] = (
        plot_df['Hybrid_Anomaly']
        .map({
            True: 'Anomaly',
            False: 'Normal'
        })
    )

    fig = px.line(
        plot_df,

        x=plot_df.index,

        y='Global_active_power',

        color='Anomaly_Label',

        title='Interactive Electricity Usage Analysis'
    )

    graph_html = fig.to_html(
        full_html=False
    )

    return graph_html