#  Começaremos montando as fórmulas para a resolução dos problemas e montando o algorítmo
# Definir as fórmulas para transcrever para python e fazer os testes de cálculo com cada uma delas
# Pesquisar novas fórmulas para conseguirmos deixar o programa ainda mais inteligente

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window


COR_PRINCIPAL = (0.18, 0.33, 0.52, 1)  
COR_SECUNDARIA = (0.96, 0.76, 0.32, 1)  
COR_FUNDO = (0.9, 0.9, 0.9, 1)  

def calcular_velocidade_media(distancia, tempo):
    try:
        distancia = float(distancia)
        tempo = float(tempo)
        velocidade_media = distancia / tempo
        return velocidade_media
    except ValueError:
        return None

def calcular_forca_massa_aceleracao(massa, aceleracao):
    try:
        massa = float(massa)
        aceleracao = float(aceleracao)
        forca = massa * aceleracao
        return forca
    except ValueError:
        return None

class CalculadoraApp(App):
    def build(self):
        Window.clearcolor = COR_FUNDO  

        layout = BoxLayout(orientation='vertical', padding=10, spacing=0)

        # Título
        titulo = Label(text="Calculadora de Física e Engenharia", font_size=20, color=COR_PRINCIPAL)
        layout.add_widget(titulo)

        button_velocidade_media = Button(text="Calcular Velocidade Média", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_velocidade_media.bind(on_press=self.mostrar_popup_velocidade_media)
        button_velocidade_media.font_name = "Arial"
        button_velocidade_media.font_size = 18
        layout.add_widget(button_velocidade_media)

        button_forca = Button(text="Calcular Força", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_forca.bind(on_press=self.mostrar_popup_forca)
        button_forca.font_name = "Arial"
        button_forca.font_size = 18
        layout.add_widget(button_forca)

        return layout

    def mostrar_popup_velocidade_media(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Distância (m):", color=COR_PRINCIPAL))
        self.distancia_input = TextInput(multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.distancia_input)
        content.add_widget(Label(text="Tempo (s):", color=COR_PRINCIPAL))
        self.tempo_input = TextInput(multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.tempo_input)

        button_calcular = Button(text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_velocidade_media_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Velocidade Média', content=content, size_hint=(None, None), size=(400, 300))
        popup.open()

    def calcular_velocidade_media_callback(self, instance):
        distancia = self.distancia_input.text
        tempo = self.tempo_input.text
        resultado = calcular_velocidade_media(distancia, tempo)
        if resultado is not None:
            popup_resultado = Popup(title='Resultado', content=Label(text=f'A velocidade média é {resultado} m/s', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        else:
            popup_erro = Popup(title='Erro', content=Label(text='Por favor, insira valores numéricos para distância e tempo.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

    def mostrar_popup_forca(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Massa (kg):", color=COR_PRINCIPAL))
        self.massa_input = TextInput(multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.massa_input)
        content.add_widget(Label(text="Aceleração (m/s^2):", color=COR_PRINCIPAL))
        self.aceleracao_input = TextInput(multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.aceleracao_input)

        button_calcular = Button(text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_forca_massa_aceleracao_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Força', content=content, size_hint=(None, None), size=(300, 300))
        popup.open()

    def calcular_forca_massa_aceleracao_callback(self, instance):
        massa = self.massa_input.text
        aceleracao = self.aceleracao_input.text
        resultado = calcular_forca_massa_aceleracao(massa, aceleracao)
        if resultado is not None:
            popup_resultado = Popup(title='Resultado', content=Label(text=f'A força é {resultado} N', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        else:
            popup_erro = Popup(title='Erro', content=Label(text='Por favor, insira valores numéricos para massa e aceleração.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

if __name__ == '__main__':
    CalculadoraApp().run()
