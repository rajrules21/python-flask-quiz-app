from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aws_quiz')  # Define route for AWS quiz
def aws_quiz():
    return render_template('aws.html')  # Render aws.html template

@app.route('/azure_quiz')  # Define route for Azure quiz
def azure_quiz():
    return render_template('azure.html')  # Render aws.html template

@app.route('/terraform_quiz')  # Define route for AWS quiz
def terraform_quiz():
    return render_template('terraform.html')  # Render aws.html template


if __name__ == '__main__':
    app.run(debug=True)
