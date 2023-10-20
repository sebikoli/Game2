import PySimpleGUI as psg

wiget = [
    [psg.Text("Name", text_color="red"), psg.InputText(key="name", default_text="sebi")],
    [psg.Text("Sizetile"), psg.OptionMenu([10, 20, 30, 40], key="size", default_value=20)],
    [psg.Text("Controllbuttons"), psg.Radio("WASD", 1, key="wasd", default=True), psg.Radio("Arrows", 1, key="arrows")],
    [psg.Text("Playersize"), psg.OptionMenu([50, 60, 70, 32], key="playersize", default_value=60)],
    [psg.Button("START"), psg.Button("EXIT")],
]
window = psg.Window("Snake", wiget)
close = 0
while close == 0:
    events = window.read()
    event_part_1 = events[0]
    event_part_2 = events[1]
    if event_part_1 == "START" or event_part_1 == "EXIT" or event_part_1 == psg.WIN_CLOSED:
        close = 1
