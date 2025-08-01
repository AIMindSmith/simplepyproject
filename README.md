# 📄 test_case_1.py – Spam Detection Example
input_text = "Congratulations! You've won a free iPhone!"
prediction = model.predict(tfidf.transform([input_text]))
print(f"Prediction: {'Spam' if prediction[0] == 1 else 'Not Spam'}")
# Output: Spam

# 🔍 Spam Detection with TF-IDF + SVM
text = "Win a free cruise now!"
prediction = model.predict(tfidf.transform([text]))
print("Spam" if prediction[0] == 1 else "Not Spam")
# Output: Spam

# 📊 Linear Regression Prediction
new_data = [[5]]
print("Predicted:", model.predict(new_data)[0])
# Output: Predicted: 24.5 (example)

# 🔁 String Reversal
def reverse_string(s): return s[::-1]
print(reverse_string("Python"))
# Output: nohtyP

# 🧮 Factorial Calculation
def factorial(n): return 1 if n==0 else n*factorial(n-1)
print(factorial(5))
# Output: 120

# 🐛 Basic Error Handling
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Error:", e)
# Output: Error: division by zero
