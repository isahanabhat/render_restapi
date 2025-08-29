from flask import Flask, request, jsonify
import re
from datetime import datetime

app = Flask(__name__)

# Replace with your details
FULL_NAME = "sahana_bhat"
DOB = "26052004"
EMAIL = "isahanabhat@gmail.com"
ROLL_NUMBER = "22BCE2889"

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get("data", [])

        even_numbers, odd_numbers, alphabets, special_chars = [], [], [], []
        total_sum = 0
        concat_alpha = ""

        for item in data:
            if item.isdigit():  # numeric
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                total_sum += num
            elif item.isalpha():  # alphabetic
                alphabets.append(item.upper())
                concat_alpha += item
            else:  # special characters
                special_chars.append(item)

        # reverse order + alternating caps
        rev_concat = ""
        toggle = True
        for ch in concat_alpha[::-1]:
            if toggle:
                rev_concat += ch.upper()
            else:
                rev_concat += ch.lower()
            toggle = not toggle

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(total_sum),
            "concat_string": rev_concat
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
