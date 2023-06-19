import pandas as pd
import seaborn as sns
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as canvas_rl

def make_report(df):

    pdf_filename = 'data_analysis_report.pdf'
    pdf = canvas_rl.Canvas(pdf_filename, pagesize=letter)

    # Print summary statistics for each column
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, 750, "Summary Statistics")

    pdf.setFont("Helvetica", 12)
    y_coordinate = 700
    for column in df.columns:
        stats = df[column].describe().to_string()
        pdf.drawString(50, y_coordinate, f"{column}:")
        pdf.drawString(120, y_coordinate, stats)
        y_coordinate -= 20

    # Generate distribution plots for each column
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y_coordinate - 40, "Distribution Plots")

    plot_width = 400
    plot_height = 300
    y_coordinate -= 80
    for column in df.columns:
        fig = sns.displot(data=df, x=column).fig
        canvas = fig.canvas
        canvas.print_png('temp.png')
        pdf.drawImage('temp.png', 50, y_coordinate - plot_height, width=plot_width, height=plot_height)
        pdf.drawString(50, y_coordinate - plot_height - 20, f"Distribution of {column}")
        y_coordinate -= plot_height + 80

    pdf.save()

def main():

    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data'
    df = pd.read_csv(url, header=None)

    make_report(df)


if __name__ == "__main__":
    
    main()
