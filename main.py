import sys

def function():
    try:
        fulltitle = sys.argv[1]
        title = fulltitle
        if ' ' in fulltitle:
            if len(fulltitle) >= 25:
                title = fulltitle[:25].rpartition(' ')[0]
                print(title + "..."),
            else:
                print(fulltitle)
        else:
            title = fulltitle[:25]
            print(title)
        return [fulltitle, title]
    except (IndexError, UnboundLocalError):
        print('No argument')


if __name__ == "__main__":
    function()