from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import os

class TaskItem(BoxLayout):
    def __init__(self, task_text, delete_callback, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=40, **kwargs)
        self.task_label = Label(text=task_text)
        self.delete_button = Button(text='Delete', size_hint_x=0.3)
        self.delete_button.bind(on_press=self.delete_task)

        self.add_widget(self.task_label)
        self.add_widget(self.delete_button)

        self.delete_callback = delete_callback

    def delete_task(self, instance):
        self.delete_callback(self)

class ToDoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.task_input = TextInput(hint_text='Enter a task', size_hint=(1, 0.1))
        self.layout.add_widget(self.task_input)

        self.add_button = Button(text='Add Task', size_hint=(1, 0.1))
        self.add_button.bind(on_press=self.add_task)
        self.layout.add_widget(self.add_button)

        self.task_list = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.task_list)

        self.load_tasks()

        return self.layout

    def add_task(self, instance):
        task_text = self.task_input.text
        if task_text.strip() != '':
            task_item = TaskItem(task_text, self.remove_task)
            self.task_list.add_widget(task_item)
            self.task_input.text = ''
            self.save_tasks()

    def remove_task(self, task_item):
        self.task_list.remove_widget(task_item)
        self.save_tasks()

    def save_tasks(self):
        tasks = []
        for child in self.task_list.children:
            tasks.append(child.task_label.text)
        with open('tasks.txt', 'w') as f:
            for task in reversed(tasks):  # reversing because children are stacked bottom to top
                f.write(task + '\n')

    def load_tasks(self):
        if os.path.exists('tasks.txt'):
            with open('tasks.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    task_text = line.strip()
                    if task_text:
                        task_item = TaskItem(task_text, self.remove_task)
                        self.task_list.add_widget(task_item)

if __name__ == '__main__':
    ToDoApp().run()
