@app.route('/button-click', methods=['POST'])
def button_click():
    click_count = int(request.form['click_count'])
    if click_count > 5:
        # Perform actions to trigger a warning notification
        # For example, you can store the notification in a database or send an email.
        # You can add your specific implementation here.

    return 'Success'  # Return a response to the button click event