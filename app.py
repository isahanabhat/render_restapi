from flask import Flask, request, jsonify
import re
from datetime import datetime

app = Flask(__name__)

FULL_NAME = "sahana_bhat"
DOB = "26052004"
EMAIL = "isahanabhat@gmail.com"
ROLL_NO = "22BCE2889"


@app.route('/bfhl', methods=['POST'])
def bfhl_handler():
    try:
        incoming = request.json.get("data", [])

        evens = []
        odds = []
        letters = []
        specials = []

        total = 0
        joined_alpha = ""

        for val in incoming:
            if val.isdigit():
                n = int(val)
                if n % 2 == 0:
                    evens.append(val)
                else:
                    odds.append(val)
                total += n
            elif val.isalpha():
                letters.append(val.upper())
                joined_alpha += val
            else:
                specials.append(val)

        rev_str = ""
        flip = True
        for c in joined_alpha[::-1]:
            if flip:
                rev_str += c.upper()
            else:
                rev_str += c.lower()
            flip = not flip

        output = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NO,
            "odd_numbers": odds,
            "even_numbers": evens,
            "alphabets": letters,
            "special_characters": specials,
            "sum": str(total),
            "concat_string": rev_str
        }

        return jsonify(output), 200

    except Exception as err:
        return jsonify({
            "is_success": False,
            "error": str(err)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
