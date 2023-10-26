import os


def list_dir(path):
    try:
        items = os.listdir(path)

        for item in items:
            item_path = os.path.join(path, item)

            if os.path.isdir(item_path):

                print(f'Directory: {item_path}')
                list_dir(item_path)

            else:
                print(f'File: {item_path}')

    except PermissionError as e:
        print(f'PermissionError: {e}')
    except FileNotFoundError as e:
        print(f'FileNotFoundError: {e}')
    except Exception as e:
        print(f'Error: {e}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_dir = '/Users/hardi/Documents'
    list_dir(start_dir)

