
from flask import Flask, render_template, request

app = Flask(__name__)


# Existing Home Page
@app.route('/')
def hello_world():
    return 'Hello World from Robert Smith I am adding my first code change!'


# Existing Hello Page
@app.route('/hello')
def hello():
    return render_template('hello.html')


# Existing About Page
@app.route('/about')
def about():
    return render_template('about.html')


# Existing About CSS Page
@app.route('/about-css')
def about_css():
    return render_template('about-css.html')


# NEW: Favorite Course Page
@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject', '')
    course_number = request.args.get('course_number', '')

    return render_template(
        'favorite-course.html',
        subject=subject,
        course_number=course_number
    )


# NEW: Contact Form Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')

        return render_template(
            'contact.html',
            submitted=True,
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )

    return render_template('contact.html', submitted=False)


if __name__ == '__main__':
    app.run()

