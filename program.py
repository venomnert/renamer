
import sys
import renamer as rn

def main():
    command = 'start'
    selected_items = sys.argv
    renamer = rn.Renamer(command, selected_items)
    print("Enter [g] for slug conversion.\n"
          "Enter [p|s] 'text' for prefix or suffix.\n"
          "Enter [x] to exit \n")

    while True:
        command = input('Enter your input: ').lower().strip()
        if command == 'x':
            break
        else:
            renamer.set_command(command)
            renamer.execute()


if __name__ == '__main__':
    main()
