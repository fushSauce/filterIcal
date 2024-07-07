from click.testing import CliRunner
from filter_ical import filter_ical
from icalendar import Calendar
import datetime 
import pytz


#############################
# From test ical file
#############################

# BEGIN:VEVENT
# DTSTART;TZID=Pacific/Auckland:20200918T143000Z # 2020-09-18 14:30-15:30
# DTEND;TZID=Pacific/Auckland:20200918T153000Z
# ORGANIZER;CN="Organizer Email";EMAIL="email@email.com":mailto:email@email.com
# SUMMARY:Test Event 1
# END:VEVENT

# BEGIN:VEVENT
# DTSTART;TZID=Pacific/Auckland:20200919T143000Z # 2020-09-19 14:30-15:30
# DTEND;TZID=Pacific/Auckland:20200919T153000Z
# ORGANIZER;CN="Organizer Email";EMAIL="email@email.com":mailto:email@email.com
# SUMMARY:Test Event 2
# END:VEVENT

# BEGIN:VEVENT
# DTSTART;TZID=Pacific/Auckland:20200920T143000Z # 2020-09-20 14:30-15:30
# DTEND;TZID=Pacific/Auckland:20200920T153000Z
# ORGANIZER;CN="Organizer Email";EMAIL="email@email.com":mailto:email@email.com
# SUMMARY:Test Event 3
# END:VEVENT

def test_no_change():
    """
    TODO
    """
    runner = CliRunner()
    result = runner.invoke(filter_ical, ["testCalendar.ics"])

    calendar=Calendar.from_ical(result.output.strip())

    event_dates = [event.get('dtstart').dt for event in calendar.walk('VEVENT')]

    assert len(event_dates) == 3

def test_date_range_gt():
    """
    TODO
    """
    runner = CliRunner()
    result = runner.invoke(filter_ical, ["testCalendar.ics","-f","18 Sep 2020 7pm NZST"])

    calendar=Calendar.from_ical(result.output.strip())

    event_dates = [event.get('dtstart').dt for event in calendar.walk('VEVENT')]

    tz=pytz.timezone('Pacific/Auckland')

    expected_dates = [
        tz.localize(datetime.datetime(2020,9,19,14,30)),
        tz.localize(datetime.datetime(2020,9,20,14,30))
    ]

    assert expected_dates == event_dates
    

def test_date_range_lt():
    """
    TODO
    """
    runner = CliRunner()
    result = runner.invoke(filter_ical, ["testCalendar.ics","-t","19 Sep 2020 7pm NZST"])

    calendar=Calendar.from_ical(result.output.strip())

    event_dates = [event.get('dtstart').dt for event in calendar.walk('VEVENT')]

    tz=pytz.timezone('Pacific/Auckland')

    expected_dates = [
        tz.localize(datetime.datetime(2020,9,18,14,30)),
        tz.localize(datetime.datetime(2020,9,19,14,30))
    ]

    assert expected_dates == event_dates

def test_date_range_between():
    """
    TODO
    """
    runner = CliRunner()
    result = runner.invoke(filter_ical, ["testCalendar.ics","-f","18 Sep 2020 7pm NZST", "-t","20 Sep 2020 10am NZST"])

    calendar=Calendar.from_ical(result.output.strip())

    event_dates = [event.get('dtstart').dt for event in calendar.walk('VEVENT')]

    tz=pytz.timezone('Pacific/Auckland')

    expected_dates = [
        tz.localize(datetime.datetime(2020,9,19,14,30))
    ]

    assert expected_dates == event_dates


def test_no_organiser():
    """
    TODO
    """
    runner = CliRunner()
    result = runner.invoke(filter_ical, ["testCalendar.ics"])

    calendar=Calendar.from_ical(result.output.strip())

    event_dates = [event.get('dtstart').dt for event in calendar.walk('VEVENT')]
    

def test_organiser():
    """
    TODO
    """
    runner = CliRunner()
    result = runner.invoke(filter_ical, ["testCalendar.ics"])

    calendar=Calendar.from_ical(result.output.strip())

    event_dates = [event.get('dtstart').dt for event in calendar.walk('VEVENT')]