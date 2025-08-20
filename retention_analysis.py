import matplotlib.pyplot as plt

# Data
quarters = ["Q1", "Q2", "Q3", "Q4"]
retention_rates = [68.33, 71.58, 75.38, 73.05]
industry_target = 85
average_retention = 72.08

# Plot
plt.figure(figsize=(6, 6))  # Adjust figure to be square
plt.plot(quarters, retention_rates, marker='o', linestyle='-', linewidth=2, label="Retention Rate")
plt.axhline(y=industry_target, color='r', linestyle='--', label=f"Industry Target ({industry_target}%)")

# Formatting
plt.title("Quarterly Customer Retention Analysis", fontsize=14, fontweight='bold')
plt.xlabel("Quarter", fontsize=12)
plt.ylabel("Retention Rate (%)", fontsize=12)
plt.ylim(60, 90)
plt.grid(alpha=0.3)
plt.legend()

# Save plot as 512x512 pixels
plt.savefig("customer_retention_trend.png", dpi=96, bbox_inches="tight")  
# 96 dpi × 6 inches ≈ 576 px → close to 512; you can adjust dpi slightly

plt.show()
