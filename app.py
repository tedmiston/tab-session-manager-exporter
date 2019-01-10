"""
Parse Tab Session Manager export output from complex JSON into simple YAML.
"""

import json


def load_sessions():
    """
    Load the sessions export JSON file.
    """
    sessions = json.load(open('sessions.json'))
    return sessions


def generate_yaml_from_sessions(sessions):
    """
    Parse essential fields from sessions and dump into a simple YAML file.
    """
    print('---')

    print('sessions:')
    for session in sessions:
        session_name = session['name']
        session_window_count = session['windowsNumber']
        session_tab_count = session['tabsNumber']

        session_date = session['date']
        session_start_time = session['sessionStartTime']
        session_tags = session['tag']

        print(f'  - type: "session"')
        print(f'    name: "{session_name}"')
        print(f'    date: {session_date}')
        print(f'    start_time: {session_start_time}')

        if len(session_tags) > 0:
            print(f'    tags:')
            for tag in session_tags:
                print(f'      - type: "tag"')
                print(f'        name: "{tag}"')
        else:
            print(f'    tags: []')

        print(f'    counts:')
        print(f'      windows: {session_window_count}')
        print(f'      tabs: {session_tab_count}')

        print(f'    windows:')
        for _, window in session['windows'].items():
            print('      - type: "window"')
            print('        tabs:')
            for _, tab in window.items():
                title = tab['title']
                url = tab['url']
                print(f'          - type: "tab"')
                print(f'            title: "{title}"')
                print(f'            url: "{url}"')


def main():
    sessions = load_sessions()
    generate_yaml_from_sessions(sessions)


if __name__ == '__main__':
    main()
