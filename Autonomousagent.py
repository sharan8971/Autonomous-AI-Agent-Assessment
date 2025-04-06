
import os
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from fpdf import FPDF
import datetime

# ========== Task 1: Find Top 5 AI Headlines and Save to File ==========
def fetch_ai_headlines():
    print("Fetching AI headlines...")
    query = "latest AI news"
    url = f"https://news.google.com/search?q={query.replace(' ', '%20')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for item in soup.select("article h3")[:5]:
        headlines.append(item.text.strip())

    filename = "ai_headlines.txt"
    with open(filename, "w") as f:
        f.write("\n".join(headlines))
    print(f"Saved headlines to {filename}")
    return filename


# ========== Task 2: Search Smartphone Reviews, Extract Pros/Cons ==========
def analyze_smartphone_reviews():
    print("Analyzing smartphone reviews (placeholder)...")
    # Placeholder data
    reviews = [
        {"pros": ["Great battery life", "Excellent camera"], "cons": ["Expensive", "Bulky"]},
        {"pros": ["Smooth performance", "Bright screen"], "cons": ["No headphone jack", "Average build"]},
    ]

    summary = "Smartphone Review Summary\n\n"
    for i, review in enumerate(reviews, 1):
        summary += f"Review {i}:\nPros: {', '.join(review['pros'])}\nCons: {', '.join(review['cons'])}\n\n"

    filename = "smartphone_review_summary.txt"
    with open(filename, "w") as f:
        f.write(summary)
    print(f"Saved review summary to {filename}")
    return filename


# ========== Task 3: Research Renewable Energy, Analyze Trends, Create PDF ==========
def create_renewable_energy_report():
    print("Creating renewable energy report...")
    years = list(range(2015, 2025))
    solar = [2, 3, 4, 5, 7, 10, 13, 17, 22, 28]
    wind = [5, 6, 7, 8, 10, 12, 14, 16, 19, 22]

    plt.figure(figsize=(8, 4))
    plt.plot(years, solar, label="Solar")
    plt.plot(years, wind, label="Wind")
    plt.title("Renewable Energy Trends (2015–2024)")
    plt.xlabel("Year")
    plt.ylabel("Production (GW)")
    plt.legend()
    chart_path = "renewable_energy_trend.png"
    plt.savefig(chart_path)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Renewable Energy Trends Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "This report analyzes the growth trends in renewable energy sources, particularly Solar and Wind power, from 2015 to 2024.")

    pdf.image(chart_path, x=30, y=60, w=150)
    pdf.ln(100)

    filename = "renewable_energy_report.pdf"
    pdf.output(filename)
    print(f"Saved PDF report to {filename}")
    return filename


# ========== Execution ==========
if __name__ == "__main__":
    fetch_ai_headlines()
    analyze_smartphone_reviews()
    create_renewable_energy_report()
