from remi import start, App
import remi.gui as gui
import socket
import sys

RED = "\033[0;31m"
debug_info = "main.Switch   INFO   "


class Switch(gui.Button):
    def __init__(self, title, **kwargs):
        super(Switch, self).__init__(**kwargs)
        self.title = title
        self.set_text("{}\n(OFF)".format(self.title))

    def switch(self):
        sys.stdout.write(RED)
        if self.style['background-color'] == '#f44336':  # red
            self.set_text("{}\n(ON)".format(self.title))
            self.style['background-color'] = '#4CAF50'  # green
            print(debug_info, self.title, 'turned on')
        elif self.style['background-color'] == '#4CAF50':  # green
            self.set_text("{}\n(OFF)".format(self.title))
            self.style['background-color'] = '#f44336'  # red
            print(debug_info, self.title, 'turned off')
        headers = {'Content-type': 'text/plain'}
        return ['OK', headers]


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.Widget(width='90%', height='35%')
        container2 = gui.VBox(width='50%', height='100%')
        container3 = gui.VBox(width='50%', height='100%')
        bt1 = Switch('Light', attributes={'id': 'light'})
        bt2 = Switch('PlayStation', attributes={'id': 'ps4'})

        container.style['overflow'] = 'auto'
        container.style['margin'] = 'auto'
        container.style['position'] = 'absolute'
        container.style['top'] = '0'
        container.style['left'] = '0'
        container.style['bottom'] = '0'
        container.style['right'] = '0'
        container.style['border'] = 'solid black'

        container2.style['overflow'] = 'auto'
        container2.style['position'] = 'absolute'
        container2.style['top'] = '0'
        container2.style['left'] = '0'
        container2.style['bottom'] = '0'
        container2.style['right'] = '0'

        container3.style['overflow'] = 'auto'
        container3.style['position'] = 'absolute'
        container3.style['top'] = '0'
        container3.style['left'] = '50%'
        container3.style['bottom'] = '0'
        container3.style['right'] = '0'

        bt1.style['width'] = '50%'
        bt1.style['height'] = '50%'
        bt1.style['overflow'] = 'auto'
        bt1.style['margin'] = 'auto'
        bt1.style['position'] = 'auto'
        bt1.style['top'] = '0'
        bt1.style['left'] = '0'
        bt1.style['bottom'] = '0'
        bt1.style['right'] = '0'
        bt1.style['background-color'] = '#f44336'  # red

        bt2.style['width'] = '50%'
        bt2.style['height'] = '50%'
        bt2.style['overflow'] = 'auto'
        bt2.style['margin'] = 'auto'
        bt2.style['position'] = 'auto'
        bt2.style['top'] = '0'
        bt2.style['left'] = '0'
        bt2.style['bottom'] = '0'
        bt2.style['right'] = '0'
        bt2.style['background-color'] = '#f44336'  # red

        bt1.onclick.connect(self.click)
        bt2.onclick.connect(self.click)

        container.append(container2)
        container.append(container3)

        container2.append(bt1)
        container3.append(bt2)

        return container

    def click(self, e):
        e.switch()


ip = '127.0.0.1'
port = 8082

start(MyApp, address=ip, port=8082, start_browser=False)
