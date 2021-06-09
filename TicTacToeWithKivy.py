from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty

class TicTacToeApp(App):
    pass
    
class TicTacToeGrid(GridLayout):
    pass
    
class GridEntry(Button):
    coords = ListProperty([0, 0])

class TicTacToeGrid(GridLayout):
    def __init__(self, *args, **kwargs):
        super(TicTacToeGrid, self).__init__(*args, **kwargs)
        for row in range(3):
            for column in range(3):
                grid_entry = GridEntry(coords = (row, column))
                grid_entry.bind(on_release = self.buttin_pressed)
                self.add_widget(grid_entry)
                
def button_pressed(self, instance):
    print('{} button clicked!'.format(instance, coords))
    
    
def build(self):
    return TicTacToeGrid()
        

if __name__ == "__main__":
	TicTacToeApp().run()
