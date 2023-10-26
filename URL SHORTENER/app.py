from flask import Flask, render_template, request, redirect, flash, url_for
import string
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Dictionary to store URL mappings (short URL to long URL)
url_dict = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')

    # Generate a random 6-character short URL
    short_url = generate_short_url()

    # Store the mapping in the dictionary
    url_dict[short_url] = long_url

    return render_template('shortened.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    if short_url in url_dict:
        long_url = url_dict[short_url]
        return redirect(long_url)
    else:
        flash('Short URL not found.')
        return redirect(url_for('index'))

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

if __name__ == '__main__':
    app.run(debug=True)
