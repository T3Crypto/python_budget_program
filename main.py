from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class BudgetCalculatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.message = Label(text='Welcome to the Budget Calculator')
        self.layout.add_widget(self.message)

        # Adding the image to the welcome page
        self.usmnt_image = Image(source='USMNT.png', size=(200, 200))
        self.layout.add_widget(self.usmnt_image)

        self.deposit_input = TextInput(hint_text='Enter your deposit', multiline=False)
        self.housing_input = TextInput(hint_text='Percentage for housing')
        self.food_input = TextInput(hint_text='Percentage for food')
        self.transportation_input = TextInput(hint_text='Percentage for transportation')
        self.calculate_button = Button(text='Calculate Budget')
        self.calculate_button.bind(on_press=self.calculate_budget)
        self.layout.add_widget(self.deposit_input)
        self.layout.add_widget(self.housing_input)
        self.layout.add_widget(self.food_input)
        self.layout.add_widget(self.transportation_input)
        self.layout.add_widget(self.calculate_button)

        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_budget(self, instance):
        try:
            deposit = float(self.deposit_input.text)
            housing = float(self.housing_input.text)
            food = float(self.food_input.text)
            transportation = float(self.transportation_input.text)

            hcalc = deposit * (housing / 100)
            fcalc = deposit * (food / 100)
            tcalc = deposit * (transportation / 100)

            hround = round(hcalc, 2)
            fround = round(fcalc, 2)
            tround = round(tcalc, 2)

            hresult = "Housing: $" + str(hround)
            fresult = "Food: $" + str(fround)
            tresult = "Transportation: $" + str(tround)

            self.result_label.text = hresult + '\n' + fresult + '\n' + tresult
        except ValueError:
            self.result_label.text = 'Invalid input. Please enter valid numbers.'

if __name__ == '__main__':
    BudgetCalculatorApp().run()
