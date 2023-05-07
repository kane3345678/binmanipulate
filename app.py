from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hex_value = request.form.get('hex_value')
        binary_value = hex_to_binary(hex_value)
        return render_template('index.html', binary_value=binary_value)
    return render_template('index.html')

def hex_to_binary(hex_value):
    try:
        binary_value = bin(int(hex_value, 16))[2:].zfill(len(hex_value) * 4)
    except ValueError:
        binary_value = "Invalid Hex Value"
    return binary_value

if __name__ == '__main__':
    app.run(debug=True)

