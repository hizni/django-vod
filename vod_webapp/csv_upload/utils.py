import csv


# handles uploaded file
def handle_uploaded_file(uploaded_file, expected_fields, record_creation_function):
    uploaded_file.seek(0)

    # important - csv file must be encoded in UTF-8
    sniffdialect = csv.Sniffer().sniff(uploaded_file.read(10000), delimiters='\t,;')
    uploaded_file.seek(0)

    # print sniffdialect.fieldnames
    data = csv.DictReader(uploaded_file, dialect=sniffdialect)

    if not csv_validate_uploaded_fields(data.fieldnames, expected_fields):
        return False, -1

    result, rows_error = record_creation_function(data)

    return result, rows_error


# checks that fields in uploaded CSV file match
def csv_validate_uploaded_fields(field_names, required_fields):
    # required_fields = ('first_name', 'last_name', 'unique_id')

    for field in required_fields:
        if field not in field_names:
            return False
    return True


# validates the extension of a given file
def validate_file_extension(value, required_extensions):

    for extension in required_extensions:
        if value.endswith(extension):
            return True

    return False


