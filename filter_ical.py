from icalendar import Calendar
import click
import dateparser
import sys
import operator
from loguru import logger



def event_date_check(event,op,date_filter):
    """TODO"""
    logger.debug(f"Event_date_check: Operator: {operator}, Date provided: {date_filter}, Event: {event}")
    date_start=str(event.get('dtstart').dt)
    date_end=str(event.get('dtstart').dt)

    date_start=dateparser.parse(date_start)
    date_end=dateparser.parse(date_end)
    logger.debug(f"Event Date start: {date_start},Event Date end: {date_end}, Provided date: {date_filter}")

    start_true=op(date_start,date_filter)
    end_true=op(date_end,date_filter)

    logger.debug(f"Start true: {start_true}, End True: {end_true}, both true: {start_true and end_true}")
    return start_true and end_true

def event_organiser_check(event,organiser_filter):
    """TODO"""
    event_organiser_email=event.get('organizer').split(':')[1].strip()
    logger.debug(f"Event organiser check called. Organiser provided: {organiser_filter}, event organizer email found: {event_organiser_email}, equal: {event_organiser_email == organiser_filter}")
    return event_organiser_email == organiser_filter

@click.command()
@click.argument('ical_file', type=click.File('r'), default=sys.stdin)
@click.option('-f','--from',"from_value")
@click.option('-t','--to',"to_value")
@click.option('-o','--organizer','organizer_value')
@click.option('-d','--debug',"debug_value",is_flag=True)
def filter_ical(from_value,to_value,ical_file,organizer_value,debug_value):
    """
    Entrypoint to script.
    """

    if not debug_value:
        logger.remove()

    logger.debug(f"Command run, arguments: From value: {from_value}, To value: {to_value}, Organizer: {organizer_value}")

    calendar=Calendar.from_ical(ical_file.read())
    events = [event for event in calendar.walk('VEVENT')]

    from_date = None
    to_date = None

    events_to_keep = events.copy()

    if from_value is not None:
        from_date = dateparser.parse(from_value)
        events_to_keep=list(filter(lambda event: event_date_check(event,operator.gt,from_date),events_to_keep))
    if to_value is not None:
        to_date = dateparser.parse(to_value)
        events_to_keep=list(filter(lambda event: event_date_check(event,operator.lt,to_date),events_to_keep))
    if organizer_value is not None:
        events_to_keep=list(filter(lambda event: event_organiser_check(event,organizer_value),events_to_keep))

    logger.debug(f"Filtered events: {events_to_keep}")
    events_to_remove = []
    for event in calendar.walk('VEVENT'):
        if (event not in events_to_keep):
            events_to_remove.append(event)
    logger.debug(f"Events to remove: {events_to_remove}")
    for event in events_to_remove:
        calendar.subcomponents.remove(event)
    
    print(calendar.to_ical().decode('utf-8'))

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    filter_ical()