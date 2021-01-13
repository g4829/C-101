import dropbox
class TransferData(object):
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'overwrite')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.AmPJjuPRAnzeQJ1jJJZC4bDra3PArjhxcH5oKCHTFFO-diziGz1mLepr7GuEkaMdI0KriOZopu-45oBUYjiix66UQJw6Yj08bB8wLv1s0Ij9I5qqkiv-5_RbfZcoqycQuze7wHY'
    transferData=TransferData(access_token)

    file_from=input("ENTER THE FILE PATH TO TRANSFER")
    file_to=input("ENTER THE FULL PATH TO UPLOAD THR DROPBOX")
    transferData.upload_file(file_from,file_to)
    print("FILE HAS BEEN MOVED")

main()