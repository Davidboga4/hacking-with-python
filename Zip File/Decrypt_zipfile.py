# Extracting all from encrypted zipfile with specfic password.
from zipfile import ZipFile

zip_file = 'myzip.zip'
password = 'hello'

ZipFile(zip_file).extractall(pwd=bytes(password, 'utf-8'))
