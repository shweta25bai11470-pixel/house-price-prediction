import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv(r"C:\Users\Dell\Downloads\archive\Participants_Data_HPP\Train.csv")

# Drop ADDRESS
data = data.drop(['ADDRESS'], axis=1)

# Convert text to numbers
data = pd.get_dummies(data, columns=['POSTED_BY', 'BHK_OR_RK'], drop_first=True)

# Separate features and target
X = data.drop('TARGET(PRICE_IN_LACS)', axis=1)
y = data['TARGET(PRICE_IN_LACS)']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Results
print("\n--- Model Evaluation ---")
print("Sample Predictions:", predictions[:5])
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

print("Average price:", y.mean())
print("Max price:", y.max())
print("Min price:", y.min())

print(data.groupby('BHK_NO.')['TARGET(PRICE_IN_LACS)'].mean())

print(data[['LATITUDE', 'LONGITUDE', 'TARGET(PRICE_IN_LACS)']].head())

# ---- USER INPUT PART ----

print("\nEnter house details:")

under_construction = int(input("Under Construction (0 or 1): "))
rera = int(input("RERA approved (0 or 1): "))
bhk = int(input("Number of BHK: "))
sqft = float(input("Square feet: "))
ready_to_move = int(input("Ready to move (0 or 1): "))
resale = int(input("Resale (0 or 1): "))
longitude = float(input("Longitude: "))
latitude = float(input("Latitude: "))

posted_by = input("Posted by (Dealer/Owner/Builder): ")
bhk_type = input("Type (BHK/RK): ")

# Create base row with all columns = 0
user_df = pd.DataFrame(0, index=[0], columns=X.columns)

# Fill numeric values
user_df['UNDER_CONSTRUCTION'] = under_construction
user_df['RERA'] = rera
user_df['BHK_NO.'] = bhk
user_df['SQUARE_FT'] = sqft
user_df['READY_TO_MOVE'] = ready_to_move
user_df['RESALE'] = resale
user_df['LONGITUDE'] = longitude
user_df['LATITUDE'] = latitude

# Handle POSTED_BY
if posted_by.lower() == "dealer":
    if 'POSTED_BY_Dealer' in user_df.columns:
        user_df['POSTED_BY_Dealer'] = 1
elif posted_by.lower() == "owner":
    if 'POSTED_BY_Owner' in user_df.columns:
        user_df['POSTED_BY_Owner'] = 1

elif posted_by.lower() == "builder":
    if 'POSTED_BY_Builder' in user_df.columns:
        user_df['POSTED_BY_Builder'] = 1

# Handle RK
if bhk_type.lower() == "rk":
    if 'BHK_OR_RK_RK' in user_df.columns:
        user_df['BHK_OR_RK_RK'] = 1

# Scale
user_scaled = scaler.transform(user_df)

# Predict
predicted_price = model.predict(user_scaled)

print(f"\nPredicted Price: ₹{predicted_price[0]:.2f} Lakhs")