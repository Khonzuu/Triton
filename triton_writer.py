import os
import curses

def draw(stdscr, buffer, y_offset, x_offset, top_buffer, left_margin):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    lines_to_display = min(max_y - top_buffer - 1, len(buffer) - y_offset)

    for i in range(lines_to_display):
        stdscr.addstr(i + top_buffer, left_margin, "".join(buffer[y_offset + i]))

    word_count = sum(len("".join(line).split()) for line in buffer)

    stdscr.addstr(max_y - 1, 0, f"Word count: {word_count}")

    stdscr.refresh()

def menu(stdscr, buffer):
    menu_options = ["Save and exit", "Exit without saving"]
    selected_option = 0

    while True:
        stdscr.clear()
        for i, option in enumerate(menu_options):
            if i == selected_option:
                stdscr.addstr(i, 0, option, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, option)
        stdscr.refresh()

        c = stdscr.getch()

        if c == curses.KEY_UP:
            selected_option = max(0, selected_option - 1)
        elif c == curses.KEY_DOWN:
            selected_option = min(len(menu_options) - 1, selected_option + 1)
        elif c == 10:  # Enter key
            break
        elif c == 27:  # Esc key
            return None, buffer

    if selected_option == 0:
        return "save", None
    elif selected_option == 1:
        return "exit", None

def main(stdscr, buffer):
    stdscr.timeout(100)
    curses.curs_set(2)
    curses.use_default_colors()
    y, x = 0, 0
    y_offset, x_offset = 0, 0
    top_buffer, left_margin = 2, 2

    while True:
        c = stdscr.getch()

        # Handle special keys
        if c == curses.KEY_LEFT:
            x = max(0, x - 1)
        elif c == curses.KEY_RIGHT:
            x = min(len(buffer[y]), x + 1)
        elif c == curses.KEY_UP:
            if y > 0:
                y -= 1
            elif y_offset > 0:
                y_offset -= 1
            x = min(len(buffer[y + y_offset]), x)
        elif c == curses.KEY_DOWN:
            if y < len(buffer) - y_offset - 1:
                y += 1
            elif y + y_offset < len(buffer) - 1:
                y_offset += 1
            x = min(len(buffer[y + y_offset]), x)

        # Ensure the cursor stays within the screen bounds

        draw(stdscr, buffer, y_offset, x_offset, top_buffer, left_margin)

        max_y, max_x = stdscr.getmaxyx()

        if y - y_offset + top_buffer < max_y - 2:
            if x + left_margin < max_x - 1:
                stdscr.move(y - y_offset + top_buffer, x + left_margin)
            else:
                 x = max_x - 3
        else:
            y = max_y - top_buffer - 3






       # Escape key
        if c == 27:  # Press 'Esc' to show the menu
            action, new_buffer = curses.wrapper(menu, buffer)
            if action == 'save': 
                return buffer, None
            elif action == 'open':
                return None, new_buffer
            elif action == 'exit':
                return None, None

        # enter key 
        if c == 10:
            if y < max_y - top_buffer -2:
                y += 1
            else:
                y_offset += 1
            buffer.insert(y + y_offset, buffer[y - 1 + y_offset][x:])
            buffer[y - 1 + y_offset] = buffer[y - 1 + y_offset][:x]
            x = 0

        # Backspace
        elif c == curses.KEY_BACKSPACE or c == 127 or c == 8:
            if x > 0:
                buffer[y].pop(x - 1)
                x -= 1
            elif y > 0:
                y -= 1
                x = len(buffer[y])
                buffer[y].extend(buffer.pop(y + 1))

        

        # Other characters
        elif 32 <= c <= 126:
            buffer[y].insert(x, chr(c))
            x += 1

     # If the current line is too long, wrap it to the next line
        if x + left_margin >= max_x - 1:
            next_line = buffer[y][x:]
            buffer[y] = buffer[y][:x]
            y += 1
            buffer.insert(y, next_line)
            x = 0



if __name__ == '__main__':
    print("Starting the text editor...")
    buffer = [['']]
    while buffer is not None:
        buffer, temp_buffer = curses.wrapper(main, buffer)
        if temp_buffer is not None:
            buffer = temp_buffer
        elif buffer is not None:
            output_filename = input("Enter the output filename (default: 'output.txt'): ")
            if not output_filename:
                output_filename = 'output.txt'
            with open(output_filename, 'w') as file:
                file.writelines("".join(line) + '\n' for line in buffer)
            print(f"Saving the edited text to '{output_filename}'...")




