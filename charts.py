import plotly.express as px
import plotly.graph_objects as go

# Hardcoded Grok (xAI) Metrics
grok_metrics = {
    "company_name": "Seekr",
    "valuation_clean": 1_200_000_000,            # $1.2B valuation from recent round :contentReference[oaicite:1]{index=1}
    "total_funding_clean": 174_000_000,           # $100M (2025) + $74M (2023) :contentReference[oaicite:2]{index=2}
    "current_employees": 103,                     # ~103 employees as of June 2025 :contentReference[oaicite:3]{index=3}
    "founded": 2021,                              # Company founded in 2021 :contentReference[oaicite:4]{index=4}
    "employee_growth": None,                      # Not enough data to calculate growth
    "funding_per_employee": 174_000_000 / 103,
    "valuation_per_employee": 1_200_000_000 / 103,
    "capital_efficiency": 1_200_000_000 / 174_000_000,
}

def style_fig(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        legend_title_font_color='white'
    )
    return fig

def valuation_bar_chart(df):
    top = df[df['valuation_clean'].notnull()].copy()
    top = top.sort_values('valuation_clean', ascending=False).head(10)

    fig = px.bar(top, x='company_name', y='valuation_clean',
                 title='Top 10 AI Companies by Valuation',
                 labels={'valuation_clean': 'Valuation ($)'})

    fig.add_hline(y=grok_metrics["valuation_clean"],
                  line_dash="dot", line_color="crimson",
                  annotation_text="Seekr",
                  annotation_position="top left")

    return style_fig(fig)

def growth_scatter_plot(df):
    chart_df = df[df['employee_growth'].notnull() & df['total_funding_clean'].notnull()].copy()

    fig = px.scatter(chart_df, x='employee_growth', y='total_funding_clean',
                     size='current_employees', color='Industry',
                     hover_name='company_name',
                     title='Funding vs Growth Rate (Bubble = Headcount)',
                     labels={'employee_growth': 'Growth (%)', 'total_funding_clean': 'Funding ($)'})

    fig.add_trace(go.Scatter(
        x=[grok_metrics["employee_growth"]],
        y=[grok_metrics["total_funding_clean"]],
        mode='markers+text',
        marker=dict(size=20, color='crimson', line=dict(width=1, color='black')),
        name='Seekr',
        text=['Seekr'],
        textposition='top right'
    ))

    return style_fig(fig)

def funding_per_employee_chart(df):
    top = df[df['funding_per_employee'].notnull()].copy()
    top = top.sort_values('funding_per_employee', ascending=False).head(10)

    fig = px.bar(top, x='company_name', y='funding_per_employee',
                 title='Top 10 by Funding per Employee',
                 labels={'funding_per_employee': 'Funding / Employee ($)'})

    fig.add_hline(y=grok_metrics["funding_per_employee"],
                  line_dash="dot", line_color="crimson",
                  annotation_text="Seekr",
                  annotation_position="top left")

    return style_fig(fig)

def valuation_per_employee_chart(df):
    top = df[df['valuation_per_employee'].notnull()].copy()
    top = top.sort_values('valuation_per_employee', ascending=False).head(10)

    fig = px.bar(top, x='company_name', y='valuation_per_employee',
                 title='Top 10 by Valuation per Employee',
                 labels={'valuation_per_employee': 'Valuation / Employee ($)'})

    fig.add_hline(y=grok_metrics["valuation_per_employee"],
                  line_dash="dot", line_color="crimson",
                  annotation_text="Seekr",
                  annotation_position="top left")

    return style_fig(fig)

def headcount_vs_valuation_chart(df):
    chart_df = df[df['valuation_clean'].notnull() & df['current_employees'].notnull()].copy()

    fig = px.scatter(chart_df, x='current_employees', y='valuation_clean',
                     color='Industry', hover_name='company_name',
                     title='Current Employees vs Valuation ($)',
                     labels={'current_employees': 'Employees', 'valuation_clean': 'Valuation ($)'})

    fig.add_trace(go.Scatter(
        x=[grok_metrics["current_employees"]],
        y=[grok_metrics["valuation_clean"]],
        mode='markers+text',
        marker=dict(size=20, color='crimson', line=dict(width=1, color='black')),
        name='Seekr',
        text=['Seekr'],
        textposition='top right'
    ))

    return style_fig(fig)

def funding_vs_founding_year(df):
    chart_df = df[df['founded'].notnull()].copy()

    fig = px.scatter(chart_df, x='founded', y='total_funding_clean',
                     color='company_name', hover_name='company_name',
                     title='Funding vs Year Founded',
                     labels={'total_funding_clean': 'Funding ($)'})

    fig.add_trace(go.Scatter(
        x=[grok_metrics["founded"]],
        y=[grok_metrics["total_funding_clean"]],
        mode='markers+text',
        marker=dict(size=20, color='crimson', line=dict(width=1, color='black')),
        name='Seekr',
        text=['Seekr'],
        textposition='top right'
    ))

    return style_fig(fig)
