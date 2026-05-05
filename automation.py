import logger
from imap_reader import fetch_attachments
from pdf_utils import extract_text, extract_license_plate, extract_driver_name, extract_packing_slip
from file_router import create_folder, move_file
import logging


def process_files():
    files = fetch_attachments()

    for file in files:
        try:
            text = extract_text(file)

            plate = extract_license_plate(text)

            if not plate:
                dest = create_folder("FAILED")
                move_file(file, dest)
                continue

            # Routing logic
            if "Packing Slip" in text:
                slip = extract_packing_slip(text) or "Unknown"
                dest = create_folder("Packing_Slips", slip)
            elif "Mileage" in text:
                dest = create_folder("Mileage_Registration", plate)

            elif "Tacho" in text:
                if plate == "TR-UCK-01":
                    driver = extract_driver_name(text) or "Unknown"
                    dest = create_folder("Tachograph_Files", plate, driver)
                else:
                    dest = create_folder("Tachograph_Files", plate)

            else:
                dest = create_folder("UNKNOWN")

            

            move_file(file, dest)

            logging.info(f"Processed {file}")

        except Exception as e:
            logging.error(f"Error processing {file}: {e}")


if __name__ == "__main__":
    process_files()