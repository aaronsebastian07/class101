import dropbox

class TransferData:
    def __init__(self, access_token):
            self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)


def main():
    access_token = 'sl.A0H2sPoBFrjbLMLtOxRs51Tltp9MURiRuYphjZ0bCAB2AOonE7iF2DXMjCP61FxJbfEK8bmrnZzBCfQDO5lOJB_gvRQQjk-0Y6Uz1w0V8Zvt0aEhyRyE39_zJ5bA9WQ53E_zGi8'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : .")
    file_to = input("enter the full path to upload to dropbox:-") 
    
        #This is the full path to upload
        #API v2
        transferData.upload_file(file_from, file_to)
        print('file has been moved !!!')

        main()
