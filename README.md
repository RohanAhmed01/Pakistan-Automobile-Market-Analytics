# Pakistan-Automobile-Market-Analytics
A data preprocessing and exploratory data analysis pipeline evaluating Pakistan's premium automotive sector using Pandas.
# Pakistan Automotive Market Analytics Infrastructure 🚗📊

A specialized data preprocessing and exploratory data analysis (application) pipeline engineered to sanitize, reconstruct, and evaluate premium vehicle market profiles in Pakistan.

##  Data Engineering & Pipeline Fixes
* **String Parsing & Standardization:** Utilized advanced string formatting to strip local currency indicators (`PKR`) and commas from messy raw inputs.
* **Statistical Imputation:** 
  * Handled missing pricing structures by calculating and deploying the data fleet's **Median Price**.
  * Reconstructed missing temporal attributes (Model Years) using **Mode Imputation** (`.mode()[0]`).
* **Type Casting:** Converted unorganized mixed-type columns into structurally sound `float64` and `int64` data types ready for downstream analytics.

##  Executive Market Insights Generated
* **Fleet Valuation:** Dynamically sums up total vehicle assets to represent the complete portfolio market valuation.
* **Segment Breakdown:** Categorizes and evaluates the average market valuation across distinct vehicle categories (EVs, Sedans, Hatchbacks).
* **High-Performance Filter:** Automatically isolates and extracts details regarding premium high-end Electric Vehicles (EV) segment.

##  Environment
* **Engine:** Python
* **Data Stack:** Pandas, NumPy
* **IDE:** PyCharm
