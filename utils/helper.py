def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'csv'}


def get_month_name(month_number):
    month_names = {
        "1": "January", "2": "February", "3": "March",
        "4": "April", "5": "May", "6": "June",
        "7": "July", "8": "August", "9": "September",
        "10": "October", "11": "November", "12": "December"
    }
    return month_names.get(month_number, "Invalid month")
