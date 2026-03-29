from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# ---------------- ML MODEL ---------------- #

# Training data
texts = [
    "add", "plus", "sum",
    "subtract", "minus",
    "multiply", "times",
    "divide", "divided"
]

labels = [
    "add", "add", "add",
    "subtract", "subtract",
    "multiply", "multiply",
    "divide", "divide"
]

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)


def predict_operation(user_input):
    X_test = vectorizer.transform([user_input])
    return model.predict(X_test)[0]


# ---------------- AI FUNCTION ---------------- #

def smart_input(user_input):
    user_input = user_input.lower()

    try:
        nums = [float(x) for x in user_input.split() if x.replace('.', '', 1).isdigit()]
        operation = predict_operation(user_input)

        if len(nums) < 2:
            return "Please provide two numbers"

        if operation == "add":
            return nums[0] + nums[1]

        elif operation == "subtract":
            return nums[0] - nums[1]

        elif operation == "multiply":
            return nums[0] * nums[1]

        elif operation == "divide":
            if nums[1] == 0:
                return "Cannot divide by zero"
            return nums[0] / nums[1]

    except:
        return "Invalid input"


# ---------------- MAIN CALCULATOR ---------------- #

def calculator():
    print("Simple Calculator")
    print("Operations: + - * /")

    while True:
        user = input("\nEnter 'smart' for AI mode or press Enter to continue: ")

        # -------- AI MODE -------- #
        if user.lower() == "smart":
            text = input("Enter (e.g., add 5 and 3): ")
            result = smart_input(text)
            print("Result:", result)

            choice = input("Continue? (y/n): ")
            if choice.lower() != 'y':
                print("Exiting calculator...")
                break
            continue

        # -------- NORMAL MODE -------- #
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+ - * /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2

            elif op == '-':
                result = num1 - num2

            elif op == '*':
                result = num1 * num2

            elif op == '/':
                if num2 == 0:
                    print("Cannot divide by zero")
                    continue
                result = num1 / num2

            else:
                print("Invalid operator")
                continue

            print("Result:", result)

        except:
            print("Invalid input. Please enter numbers correctly.")
            continue

        # -------- CONTINUE OPTION -------- #
        choice = input("Continue? (y/n): ")
        if choice.lower() != 'y':
            print("Exiting calculator...")
            break


# Run program
calculator()
