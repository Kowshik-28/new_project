# Email PDF Automation System

##  Overview

This project automates the process of:

* Reading emails from a mailbox (via IMAP)
* Downloading PDF attachments
* Extracting key information from PDFs
* Routing files into structured folders
* Logging all operations

It eliminates manual handling of attachments and ensures consistent file organization.

---

##  Features

*  Fetch emails using IMAP
*  Extract PDF attachments automatically
*  Parse PDF content (License Plate, Driver, Slip Number)
*  Dynamic folder creation
*  Duplicate file handling
*  Error handling (FAILED / UNKNOWN)
*  Logging system (`process.log`)

---

##  Project Structure

```
email_application/
│
├── automation.py        # Main execution script
├── imap_reader.py       # Fetch emails & download PDFs
├── pdf_utils.py         # Extract data from PDFs
├── file_router.py       # Move files to correct folders
├── logger.py            # Logging configuration
├── process.log          # Logs
│
├── temp_pdfs/           # Temporary downloaded PDFs
├── output/              # Final organized output
```

---

##  Installation

### 1. Create Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate
```

### 2. Install Dependencies

```bash
pip install pdfplumber
```

---

##  Configuration

Edit `imap_reader.py`:

```python
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
```

>  Use **Gmail App Password**, not your login password.

---

##  Email Requirements

* Email must contain **PDF attachments**
* Subject/body is optional
* System depends on **PDF content**

---

##  Supported PDF Types

###  Packing Slip

```
Packing Slip
Slip No: 10492
```

 Stored in:

```
output/Packing_Slips/10492/
```

---

###  Mileage

```
Mileage Report
Vehicle: AB-123-C
```

➡️ Stored in:

```
output/Mileage_Registration/AB-123-C/
```

---

###  Tachograph

```
Tachograph Report
Vehicle: TR-UCK-01
Driver: John Doe
```

 Stored in:

```
output/Tachograph_Files/TR-UCK-01/John Doe/
```

---

##  How to Run

```bash
python automation.py
```

---

##  Output Structure

```
output/
├── Packing_Slips/
├── Mileage_Registration/
├── Tachograph_Files/
├── UNKNOWN/
├── FAILED/
```

---

##  Error Handling

* Missing plate → `FAILED/`
* Unknown format → `UNKNOWN/`
* Duplicate files → Skipped
* All logs → `process.log`

---

##  Logging Example

See `process.log`:



---

##  Improvements (Next Steps)

*  Run automatically using cron (every 5 mins)
*  Process only new emails (`UNSEEN`)
*  Store processed email IDs (DB)
*  Build monitoring dashboard (FastAPI)

---

##  Notes

* Works on Linux / Windows
* Uses IMAP (no Outlook dependency)
* Designed for real-world automation

---

##  Summary

This system provides:

* Automation
* Reliability
* Scalability

Replacing manual email handling with a robust backend workflow.

---
