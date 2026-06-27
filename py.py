import pandas as pd
import numpy as np

# STEP 1: RAW DATA INGESTION
raw_cars_data = {
    'Car_Model': ['Honda Civic Oriel', 'Audi e-tron GT', 'Suzuki Alto VXL', 'BMW i4 eDrive40', 'Honda City Aspire', 'Porsche Taycan'],
    'Company': ['Honda', 'Audi', 'Suzuki', 'BMW', 'Honda', 'Porsche'],
    'Model_Year': [2022, 2023, np.nan, 2023, 2022, 2024],
    'Price': ['PKR 8,500,000', 'PKR 42,000,000', 'PKR 2,950,000', 'PKR 31,000,000', 'Missing', 'PKR 55,000,000'],
    'Type': ['Sedan', 'EV', 'Hatchback', 'EV', 'Sedan', 'EV']
}

df = pd.DataFrame(raw_cars_data)

print("--- Raw Data From Client ---")
print(df)
print("\n" + "="*50 + "\n")

# STEP 2: DATA CLEANING & PROCESSING (Aap ka code)

# 1. Clean and convert price column
df['Price'] = df['Price'].replace('Missing', np.nan)
df['Price'] = df['Price'].astype(str).str.replace(r'[PKR\s,]', '', regex=True)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# 2. Handle missing price values
median_price = df['Price'].median()
df['Price'] = df['Price'].fillna(median_price)

# 3. Impute missing model year
most_frequent_year = df['Model_Year'].mode()[0]
df['Model_Year'] = df['Model_Year'].fillna(most_frequent_year)
df['Model_Year'] = df['Model_Year'].astype(int)

print(" --- CLEANED & PIPELINE PROCESSED DATA ---")
print(df)
print("\nNew Data Types:")
print(df.dtypes)
print("\n" + "="*50 + "\n")

# STEP 3: PREMIUM MARKET INSIGHTS & EXECUTIONS (Naya code)

print("        PAKISTAN AUTOMOBILE PREMIUM MARKET REPORT       ")
print("==========================================================")

# 1. Total Valuation of this fleet
total_market_value = df['Price'].sum()
print(f" Total Premium Fleet Portfolio Value: PKR {total_market_value:,.2f}")

# 2. Average Price by Car Type (EV vs Sedan vs Hatchback)
avg_price_by_type = df.groupby('Type')['Price'].mean()
print("\n Average Price Distribution by Vehicle Category:")
for car_type, avg_price in avg_price_by_type.items():
    print(f"   -> {car_type}: PKR {avg_price:,.2f}")

# 3. Filtering High-Performance Electric Vehicles (EVs)
print("\n⚡ Premium Electric Vehicles (EV) Segment:")
ev_segment = df[df['Type'] == 'EV'][['Car_Model', 'Company', 'Price']]
print(ev_segment.to_string(index=False))

print("="*50 + "\n")