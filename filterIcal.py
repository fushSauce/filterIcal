from icalendar import Calendar, vDDDTypes
import click
from pathlib import Path
from datetime import datetime
import dateparser
import sys

def filter_events(start_date,end_date,calendar,organizer): 
    """
    Iterate ical events, finding events not matching criteria passed in
    arguments and removing them.
    """
    events_to_remove = []
    for event in calendar.walk('VEVENT'):
        event_start = str(event.decoded('dtstart'))
        event_end = str(event.decoded('dtend'))
        event_start_date = datetime.fromisoformat(event_start)
        event_end_date = datetime.fromisoformat(event_end)
        event_organizer=str(event.get('organizer')).strip()
        if organizer.strip() not in event_organizer.strip():
            events_to_remove.append(event)
            continue

        if not((event_start_date >= start_date) and (event_end_date <= end_date)):
            events_to_remove.append(event)
    for event in events_to_remove:
        calendar.subcomponents.remove(event)
    return calendar
    

@click.command()
@click.argument('ical_file', type=click.File('r'), default=sys.stdin)
@click.argument('from_date')
@click.argument('to_date')
@click.option('--organizer')
def main(from_date,to_date,ical_file,organizer):
    """
    Entrypoint to script.
    """

    calendar=Calendar.from_ical(ical_file.read())

    from_date = dateparser.parse(from_date)
    to_date = dateparser.parse(to_date)

    print(filter_events(from_date,to_date,calendar,organizer).to_ical().decode('utf-8'))

if __name__ == '__main__':
    main()