import argparse
from utils import logo, finish, createClientProject

def main() -> None:
    parser = argparse.ArgumentParser(description='CLI for building full-satck projects')

    parser.add_argument('--client', type=str, default='', help='generate client project with React')
    parser.add_argument('--desktop', action='store_true', help='adding desktop environment for client project')
    # @todo implementar creación de proyectos de escritorio
    # parser.add_argument('--api', type=str, default='', help='generate API project with node/express')
    args = parser.parse_args()

    logo()
    if args.client != '':
        createClientProject(args.client, args.desktop)
        finish()
    # if args.api == '' and args.client != '':
    #     createClientProject(args.client, args.desktop)

    # elif args.api != '' and args.client == '':
    #     print('haremos back')

    # elif args.api != '' and args.client != '':
    #     print('haremos ambos', args.desktop)
    else:
        print('no haremos ni madres')


if __name__ == "__main__":
    main()

