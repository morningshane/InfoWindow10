import todoist
import logging
import json

class ToDo:
    def __init__(self, opts):
        logging.debug("Todo API: TODOIST")
        self.api = todoist.TodoistAPI('1e5212f77e2020066a7837c5e6ca1785674a4177')
        self.api.sync()

    def list(self):
        items = []
        # Loop through original array from Todoist and pull out 
        # items of interest
        for item in self.api.state['items']:
            if item['checked'] == 0:
                items.append({
                    "content": item['content'],
                    "priority": item['priority'],
                })

        # Sort the array by priority    
        items = sorted(items, key = lambda i: i['priority'])

        # Reverse list, since Todoist sets priority in reverse.
        # On web interface HIGH=Priority1, but stored in API as 4. who knows?!
        items.reverse()

        return items
