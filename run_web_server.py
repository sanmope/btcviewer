__author__ = 'GastonLucero'

from clases.Server import Server


def main():
    port = 8080
    server = Server(port)
    server.run_server()

if __name__ == "__main__":
    main()
