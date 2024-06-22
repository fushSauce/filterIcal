# ical Filter

Born from needing to extract my work events from my calendar between two dates.

## Usage

- `<ical-contents> | python3 filterIcal.py - "start-date" "end-date"`
  - Assuming you've copied the ical data from your calendar source, command could look something like:
  - `pbpaste | python3 filterIcal.py - "17 Jun 24 7am NZST" "28 Jun 24 7pm NZST"`
- I pipe the output to my clipboard and paste it into my timesheet at work where I have a [userscript](https://github.com/fushSauce/VUWTimesheetTimesaver) that uses the ical data as inputs to the timesheet fields.