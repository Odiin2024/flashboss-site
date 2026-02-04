#!/usr/bin/env python3
"""
FlashBoss Correction Puller

Pulls flashcard issue reports from Google Sheets (populated by Google Forms)
and exports them in machine-readable format for batch processing.

Setup:
1. Create a Google Cloud project
2. Enable Google Sheets API
3. Create a service account and download JSON credentials
4. Share your Google Sheet with the service account email
5. pip install gspread google-auth

Usage:
    python pull_corrections.py                    # Export all reports to JSON
    python pull_corrections.py --type typo        # Filter by issue type
    python pull_corrections.py --pack german      # Filter by language pack
    python pull_corrections.py --pending          # Show unprocessed only
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

try:
    import gspread
    from google.oauth2.service_account import Credentials
except ImportError:
    print("Missing dependencies. Run: pip install gspread google-auth")
    exit(1)


# ============================================================================
# CONFIGURATION - Update these values
# ============================================================================

# Path to your Google Cloud service account JSON file
SERVICE_ACCOUNT_FILE = 'service_account.json'

# Your Google Sheet ID (from the URL)
# https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit
SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID_HERE'

# Sheet name (usually "Form Responses 1" for Google Forms)
SHEET_NAME = 'Form Responses 1'

# Column mapping - adjust these to match your form's column headers
COLUMN_MAP = {
    'timestamp': 'Timestamp',
    'card_id': 'Card / Word',
    'language_pack': 'Language Pack',
    'issue_type': 'Issue Type',
    'description': 'Description',
    'suggested_fix': 'Suggested Fix',
    'contact': 'Contact (optional)',
    'status': 'Status',  # Add this column manually to track processed items
}

# ============================================================================
# FUNCTIONS
# ============================================================================

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def get_sheet():
    """Connect to Google Sheets and return the worksheet."""
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(SPREADSHEET_ID)
    return spreadsheet.worksheet(SHEET_NAME)


def get_all_reports(sheet):
    """Fetch all reports from the sheet."""
    records = sheet.get_all_records()

    reports = []
    for i, row in enumerate(records, start=2):  # Row 2 is first data row
        reports.append({
            'row_number': i,
            'timestamp': row.get(COLUMN_MAP['timestamp'], ''),
            'card_id': row.get(COLUMN_MAP['card_id'], ''),
            'language_pack': row.get(COLUMN_MAP['language_pack'], ''),
            'issue_type': row.get(COLUMN_MAP['issue_type'], ''),
            'description': row.get(COLUMN_MAP['description'], ''),
            'suggested_fix': row.get(COLUMN_MAP['suggested_fix'], ''),
            'contact': row.get(COLUMN_MAP['contact'], ''),
            'status': row.get(COLUMN_MAP['status'], ''),
        })

    return reports


def filter_reports(reports, issue_type=None, language_pack=None, pending_only=False):
    """Filter reports by criteria."""
    filtered = reports

    if issue_type:
        filtered = [r for r in filtered if issue_type.lower() in r['issue_type'].lower()]

    if language_pack:
        filtered = [r for r in filtered if language_pack.lower() in r['language_pack'].lower()]

    if pending_only:
        filtered = [r for r in filtered if not r['status'] or r['status'].lower() == 'pending']

    return filtered


def export_reports(reports, output_file='corrections.json'):
    """Export reports to JSON file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(reports, f, indent=2, ensure_ascii=False)
    print(f"Exported {len(reports)} reports to {output_file}")


def mark_as_processed(sheet, row_numbers, status='Processed'):
    """
    Mark reports as processed in the sheet.
    Requires a 'Status' column in your sheet.
    """
    # Find the Status column
    headers = sheet.row_values(1)
    try:
        status_col = headers.index(COLUMN_MAP['status']) + 1
    except ValueError:
        print(f"Warning: No '{COLUMN_MAP['status']}' column found. Add it to track processed items.")
        return

    for row_num in row_numbers:
        sheet.update_cell(row_num, status_col, status)
        print(f"Marked row {row_num} as {status}")


def print_summary(reports):
    """Print a summary of reports by type."""
    print("\n" + "=" * 50)
    print("CORRECTION REPORT SUMMARY")
    print("=" * 50)

    # By issue type
    by_type = {}
    for r in reports:
        t = r['issue_type'] or 'Unknown'
        by_type[t] = by_type.get(t, 0) + 1

    print("\nBy Issue Type:")
    for t, count in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {t}: {count}")

    # By language pack
    by_pack = {}
    for r in reports:
        p = r['language_pack'] or 'Unknown'
        by_pack[p] = by_pack.get(p, 0) + 1

    print("\nBy Language Pack:")
    for p, count in sorted(by_pack.items(), key=lambda x: -x[1]):
        print(f"  {p}: {count}")

    # Pending vs processed
    pending = sum(1 for r in reports if not r['status'] or r['status'].lower() == 'pending')
    processed = len(reports) - pending

    print(f"\nStatus: {pending} pending, {processed} processed")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(description='Pull flashcard corrections from Google Sheets')
    parser.add_argument('--type', '-t', help='Filter by issue type (e.g., typo, translation)')
    parser.add_argument('--pack', '-p', help='Filter by language pack (e.g., german, esperanto)')
    parser.add_argument('--pending', action='store_true', help='Show only unprocessed reports')
    parser.add_argument('--output', '-o', default='corrections.json', help='Output file (default: corrections.json)')
    parser.add_argument('--summary', '-s', action='store_true', help='Print summary only, no export')
    parser.add_argument('--mark-processed', '-m', nargs='+', type=int, help='Mark row numbers as processed')

    args = parser.parse_args()

    # Check for credentials
    if not Path(SERVICE_ACCOUNT_FILE).exists():
        print(f"Error: Service account file '{SERVICE_ACCOUNT_FILE}' not found.")
        print("\nSetup instructions:")
        print("1. Go to console.cloud.google.com")
        print("2. Create a project and enable Google Sheets API")
        print("3. Create a service account (IAM & Admin > Service Accounts)")
        print("4. Create and download a JSON key")
        print(f"5. Save it as '{SERVICE_ACCOUNT_FILE}' in this directory")
        print("6. Share your Google Sheet with the service account email")
        return

    if SPREADSHEET_ID == 'YOUR_SPREADSHEET_ID_HERE':
        print("Error: Please update SPREADSHEET_ID in this script.")
        print("Find it in your Google Sheet URL:")
        print("https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit")
        return

    print("Connecting to Google Sheets...")
    sheet = get_sheet()

    # Mark as processed if requested
    if args.mark_processed:
        mark_as_processed(sheet, args.mark_processed)
        return

    # Fetch and filter
    print("Fetching reports...")
    reports = get_all_reports(sheet)
    print(f"Found {len(reports)} total reports")

    filtered = filter_reports(
        reports,
        issue_type=args.type,
        language_pack=args.pack,
        pending_only=args.pending
    )

    if args.type or args.pack or args.pending:
        print(f"After filtering: {len(filtered)} reports")

    # Output
    if args.summary:
        print_summary(filtered)
    else:
        print_summary(filtered)
        export_reports(filtered, args.output)


if __name__ == '__main__':
    main()
