from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    chars = ['1', '2', '3', '4', 'd', 'c', 
             '5', '6', '7', '8', '+', '-', 
             '9', '0', '.', '*', '/', '=']
    btn = {}
    gp = GridPanel()
    
    for index, i in enumerate(chars):
      if index < 6:
        row = 'A'
      elif 6<=index<12:
        row = 'B'
      else:
        row = 'C'
      btn[i] = Button(text=i, font='Consolas', bold=True, foreground='#000')
      btn[i].tag.name = i
      btn[i].set_event_handler('click', self.click)
      gp.add_component(btn[i], row=row, col_xs=3, width_xs=1)
      
    self.add_component(gp)
    space = Spacer(height=500)
    self.add_component(space)
    
  def click(self, **event_args):
    value = event_args['sender'].tag.name
    if value == '=':
      self.text_box_1.text = eval(self.text_box_1.text)
    elif value == 'c':
      self.text_box_1.text = ''
    elif value == 'd':
      self.text_box_1.text = self.text_box_1.text[:-1]
    else:
      self.text_box_1.text += value