#!bin/python
from com.dave.error.exception import DataException
from com.dave.error.exception import FieldException
'''
{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "pageview",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}
'''
REQUIRED_FIELDS = ["session_id", "category", "name", "data", "timestamp"]
CATEGORIES = ['page interaction','form interaction']
def validate_basic_event(event_json):
    for field in REQUIRED_FIELDS:
        if field not in event_json:
            raise FieldException(f'{field} is missing from call.')


def validate_event(event_json):
    validate_basic_event(event_json)
    category = event_json['category']
    validate_category(category)
    return locals()[category.replace(' ', ' ')](event_json)


def validate_category(category):
    for cat in CATEGORIES:
        if cat == category:
            return

    raise DataException(f'{category} is missing from call.')

def page_interaction(event_json):
    #validate page_interaction
    name = event_json['name']
    if name == 'name1':
        pass
    elif name == 'name2':
        pass
    elif name == 'name3':
        pass
    elif name == 'name4':
        pass
    else:
        raise DataException(f'event name, "{name}", unknown.')
    return True

def form_interaction(event_json):
    name = event_json['name']
    if name == 'name5':
        pass
    elif name == 'name6':
        pass
    elif name == 'name7':
        pass
    elif name == 'name8':
        pass
    else:
        raise DataException(f'event name, "{name}", unknown.')
    return True


