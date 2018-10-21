# Credentials file

# MongoDB credentials
# Return:
# Parameters
# dblink - database link
# database_name - name of the database
# collection_name - name of the collection
def mongodb_parameters():

    params = {
        'dblink': 'mongodb://test:test123@ds137643.mlab.com:37643/elearn',
        'database_name': 'elearn'
    }

    return params