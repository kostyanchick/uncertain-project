from service_api.app import app


def runserver(host, port, debug):
    app.run(host=host, port=port, debug=debug)


def main():
    runserver(app.config['SERVICE_HOST'], app.config['SERVICE_PORT'], app.config['DEBUG'])


if __name__ == "__main__":
    try:
        main()
    except OSError as e:
        print(e)
    except Exception:
        print('Unexpected error occurred')

