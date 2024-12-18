import segno
from datetime import datetime
from pathlib import Path


###############################################################################
# STATIC DEFINITIONS
###############################################################################

date_iso8601 = f"%Y%m%dT%H%M%S%z"


###############################################################################
# CLASSES
###############################################################################

class MakeQR():
    def __init__(self, input_url, input_file):
        self.input_url = input_url
        self.output_file = input_file

    def generate_qr_code(self, scale=10):
        qrcode = segno.make(self.input_url)
        qrcode.save(self.output_file, scale=scale)


###############################################################################
# FUNCTIONS
###############################################################################

def check_if_dir_exists(input_dir, mkdir=True):
    # Check if specified path exists
    if (input_dir.parent.exists()==False) and (mkdir==True):
        # Make output path if it does not exist
        input_dir.parent.mkdir(parents=True)
    else:
        print(f"'{input_dir}' in '{input_dir.parent} already exists'")

def generate_timestamp():
    return datetime.now().astimezone().strftime(date_iso8601)

def set_output_file(input_file_name, mkdir=True):
    timestamp = generate_timestamp()
    file_out = Path(Path(__file__).parents[0], 'output', 
                    f'{timestamp}_{input_file_name}')
    check_if_dir_exists(file_out, mkdir=mkdir)
    return file_out


###############################################################################
# STANDALONE SCRIPT
###############################################################################

if __name__ == '__main__':
    # Get URL from user
    input_link = input("\nInput URL to convert: ")

    # Set output file
    file_out = set_output_file('qr.svg')

    # Generate QR code and save to disk
    qr_code = MakeQR(input_link, file_out)
    qr_code.generate_qr_code()
    print(f"\nQR code saved as '{file_out.name}' to: '{file_out.parent}'")