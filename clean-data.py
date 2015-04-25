import sys
import csv
import re

# Messages we've already seen
message_set = set()

# Labels to filter out

target_label_codes = {
    'casualties',
    'infrastructure',
    'supplies',
    'missing'
}

def normalise(s):
    """Normalise a string for duplicate detection."""
    return re.sub(r'[^\w#]+', ' ', s.strip().lower())

def transform(reader, writer):
    """Filter the dataset"""
    writer.writeheader()

    for row in reader:

        # Filter out uninteresting label codes
        if row['labelCode_1'] not in target_label_codes:
            continue

        # Have we already seen this exact message text?
        message_norm = normalise(row['message'])
        if message_norm in message_set:
            continue
        else:
            message_set.add(message_norm)

        # Write the row
        writer.writerow(row)

# Read from standard input, and write to standard output
reader = csv.DictReader(sys.stdin)
writer = csv.DictWriter(sys.stdout, reader.fieldnames)

transform(reader, writer)

# end


