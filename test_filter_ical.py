from click.testing import CliRunner
from filter_ical import filter_ical
from icalendar import Calendar

#############################
# From test ical file
#############################

# BEGIN:VEVENT
# DTSTART:20200918T143000Z
# DTEND:20200918T153000Z
# ORGANIZER;CN="Organizer Email";EMAIL="email@email.com":mailto:email@email.com
# SUMMARY:Test Event 1
# END:VEVENT

# BEGIN:VEVENT
# DTSTART:20200919T143000Z
# DTEND:20200919T153000Z
# ORGANIZER;CN="Organizer Email";EMAIL="email@email.com":mailto:email@email.com
# SUMMARY:Test Event 2
# END:VEVENT

# BEGIN:VEVENT
# DTSTART:20200920T143000Z
# DTEND:20200920T153000Z
# ORGANIZER;CN="Organizer Email";EMAIL="email@email.com":mailto:email@email.com
# SUMMARY:Test Event 3
# END:VEVENT

def test_date_range_gt():
    """
    TODO
    """
    runner = CliRunner()
    result = runner.invoke(filter_ical, ["testCalendar.ics","-f","1st Jan 2019 7pm NZST"])

    calendar=Calendar.from_ical(result.output.strip())

    assert len(calendar.walk('VEVENT')) == 3

def test_date_range_lt():
    """
    TODO
    """
    print("TODO")

def test_date_range_between():
    """
    TODO
    """
    print("TODO")

def test_no_organiser():
    """
    TODO
    """
    print("TODO")

def test_organiser():
    """
    TODO
    """
    print("TODO")