from flask import Flask, request, render_template_string

app = Flask(__name__)

# Set this to your password

PASSWORD = 'password' 

html = """
<title>Flask Password Protect</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>

<style>
form {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
}
</style>

<form method="POST">
  <label>Enter password: <input type="password" name="password"></label>
  <input type="submit" value="Submit">
</form>
"""

@app.route('/', methods=['GET', 'POST']) 
def index():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            return "Welcome!"
        else:
            return "Incorrect password"

    return render_template_string(html)

if __name__ == '__main__':
   app.run()
