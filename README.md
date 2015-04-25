# Filter for cleaning AIDR data for the Standby Task Force

Started by David Megginson, 2015-04-25

## Filter rules

* Keep only messages with the label codes 'casualties', 'infrastructure', 'supplies', or 'missing'
* Remove filters with duplicate message content (after normalising whitespace, punctuation, and character case)

## Usage

python3 < data_in/ORIGINAL_AIDR_DATA.csv > data_out/CLEANED_AIDR_DATA.csv
