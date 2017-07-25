from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from upload_demographic.forms import UploadForm
from csv_upload.models import Upload
from upload_demographic.models import StoredData
from csv_upload.utils import validate_file_extension, handle_uploaded_file, csv_validate_uploaded_fields


def demog_upload_view(request):

    expected_extensions = ('csv')
    required_fields = ('first_name', 'last_name', 'unique_id')
    pagination_size = 10

    # Handle file upload
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        # create upload audit record. need to pass in user credentials
        upload = Upload(uploaded_file='foo', uploaded_by='foo', created_by='foo')

        if form.is_valid():
            # gather submitted file information
            uploaded_file = request.FILES['demog_file']

            # depending on outcome of file extension validation
            if validate_file_extension(uploaded_file.name, expected_extensions):
                csv_result, rows_error = handle_uploaded_file(uploaded_file, required_fields, create_account_in_db)
                if csv_result:
                    upload.outcome = 'SUCCESS'
                    message = 'Successfully imported accounts from the csv file to the database.\n'
                    message += 'Please wait...'
                    messages.add_message(request, messages.INFO, message)
                else:
                    upload.outcome = 'ERRORED'
                    message = 'There are some errors occurred. Please try again.'
                    messages.add_message(request, messages.INFO, message)
            else:
                upload.outcome = 'FILE_ERROR'
                message = 'The chosen file that was uploaded was not one of the expected file extensions. ' \
                          'Please try again.'
                messages.add_message(request, messages.INFO, message)
        else:
            upload.outcome = 'UNEXPECTED'
            message = 'An unexpected error was encountered.'
            messages.add_message(request, messages.INFO, message)

        upload.save()

    else:
        form = UploadForm()  # A empty, unbound form

    # Load a paginated list of upload objects. Making use of Pagination library
    documents_list = Upload.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(documents_list, pagination_size)
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'upload_demog.html',
        {'documents': documents, 'form': form}
    )


# create record in database
def create_account_in_db(dict_data):
    list_data = []
    result = False
    rows_error = 0
    for record in dict_data:
        first_name = record['first_name']
        last_name = record['last_name']
        unique_id = record['unique_id']

        account = StoredData(first_name=first_name,
                             last_name=last_name,
                             unique_id=unique_id)
        list_data.append(account)

    if list_data:
        # bulk_create will create multiple object in a single query
        created_accounts = StoredData.objects.bulk_create(list_data)

        if len(list_data) == len(created_accounts):
            result = True
        else:
            rows_error = len(list_data) - len(created_accounts)

    return result, rows_error

