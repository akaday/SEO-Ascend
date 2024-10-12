from trend_prediction import predict_trends

# Sample Data
data = {
    'dates': [1, 2, 3, 4, 5],
    'search_volume': [10, 20, 30, 40, 50]
}

# Run Prediction
predictions = predict_trends(data)
print("Predictions:", predictions)
