# post_release_hook.py generated by Pyrustic Manager
import sys
import os
import os.path
from datetime import datetime
import time


def get_data():
    """
    Return None or a dict with the keys:
        'script', 'target', 'app_pkg' and 'version'
    """
    items = ("script", "target", "app_pkg", "version")
    data = None
    if len(sys.argv) == len(items):
        data = {item: sys.argv[i] for i, item in enumerate(items)}
    return data


def get_date():
    """ Returns the current date. Format: Month day, year.
    Example: January 15, 2020
    """
    MONTHS = ("January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October",
              "November", "December")
    dt = datetime.fromtimestamp(time.time())
    text = "{month} {day}, {year}".format(month=MONTHS[dt.month - 1],
                                          day=dt.day, year=dt.year)
    return text


def update_changelog(path, data, version):
    """ Update the file CHANGELOG.md located at path, with data and version """
    if not data:
        return
    cache = "## Version {} of {}\n"
    data.insert(0, cache.format(version, get_date()))
    data.append("\n\n\n")
    data = "".join(data)
    try:
        with open(path, "r+") as file:
            cache = file.readlines()
            cache.insert(0, data)
            file.seek(0)
            file.write("".join(cache))
            file.truncate()
    except Exception as e:
        pass


def main():
    data = get_data()
    if not data:
        print("Missing sys.argv data")
        sys.exit(1)
    # cut LATEST_RELEASE.md content and then log it in CHANGELOG.md
    target = data["target"]
    latest_release_path = os.path.join(target, "LATEST_RELEASE.md")
    try:
        with open(latest_release_path, "r+") as file:
            cache = file.readlines()
            file.seek(0)
            file.write("")
            file.truncate()
    except Exception as e:
        pass
    else:
        changelog_path = os.path.join(target, "CHANGELOG.md")
        update_changelog(changelog_path, cache, data["version"])
    # exit
    sys.exit(0)


if __name__ == "__main__":
    main()
