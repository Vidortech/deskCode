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
from funcoes import *


COR_PRINCIPAL = (0.18, 0.33, 0.52, 1)
COR_SECUNDARIA = (0.96, 0.76, 0.32, 1)
COR_FUNDO = (0.9, 0.9, 0.9, 1)



class CalculadoraApp(App):
    def build(self):
        Window.clearcolor = COR_FUNDO

        layout = BoxLayout(orientation='vertical', padding=10, spacing=0)

        # Título
        titulo = Label(text="Calculadora de Física e Engenharia",
                       font_size=20, color=COR_PRINCIPAL)
        layout.add_widget(titulo)

        button_velocidade_media = Button(
            text="Calcular Velocidade Média", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_velocidade_media.bind(
            on_press=self.mostrar_popup_velocidade_media)
        button_velocidade_media.font_name = "Arial"
        button_velocidade_media.font_size = 18
        layout.add_widget(button_velocidade_media)

        button_forca = Button(
            text="Calcular Força", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_forca.bind(on_press=self.mostrar_popup_forca)
        button_forca.font_name = "Arial"
        button_forca.font_size = 18
        layout.add_widget(button_forca)

        button_bhaskara = Button(
            text="Calcular Bhaskara", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_bhaskara.bind(on_press=self.mostrar_popup_bhaskara)
        button_bhaskara.font_name = "Arial"
        button_bhaskara.font_size = 18
        layout.add_widget(button_bhaskara)

        button_complexidade_ciclomática = Button(
            text="Calcular Complexidade Ciclomática", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_complexidade_ciclomática.bind(on_press=self.mostrar_popup_complexidade_ciclomatica)
        button_complexidade_ciclomática.font_name = "Arial"
        button_complexidade_ciclomática.font_size = 18
        layout.add_widget(button_complexidade_ciclomática)



        # 

            #
             
                # TERMINAR DE ARRUMAR A FUNÇÃO DE CÁLCULO DE COMPLEXIDADE CICLOMÁTICA

            # 

        # 




        button_logaritmo = Button(
            text="Calcular Log Simples", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_logaritmo.bind(on_press=self.mostrar_popup_logaritmo)
        button_logaritmo.font_name = "Arial"
        button_logaritmo.font_size = 18
        layout.add_widget(button_logaritmo)

        button_forca = Button(
            text="Calcular Força", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_forca.bind(on_press=self.mostrar_popup_forca)
        button_forca.font_name = "Arial"
        button_forca.font_size = 18
        layout.add_widget(button_forca)

        button_forca = Button(
            text="Calcular Força", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_forca.bind(on_press=self.mostrar_popup_forca)
        button_forca.font_name = "Arial"
        button_forca.font_size = 18
        layout.add_widget(button_forca)

        button_forca = Button(
            text="Calcular Força", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_forca.bind(on_press=self.mostrar_popup_forca)
        button_forca.font_name = "Arial"
        button_forca.font_size = 18
        layout.add_widget(button_forca)

        button_forca = Button(
            text="Calcular Força", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_forca.bind(on_press=self.mostrar_popup_forca)
        button_forca.font_name = "Arial"
        button_forca.font_size = 18
        layout.add_widget(button_forca)

        button_forca = Button(
            text="Calcular Força", background_color=COR_SECUNDARIA, size_hint_y=None, height=60)
        button_forca.bind(on_press=self.mostrar_popup_forca)
        button_forca.font_name = "Arial"
        button_forca.font_size = 18
        layout.add_widget(button_forca)

        return layout

    def mostrar_popup_velocidade_media(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Distância (m):", color=COR_PRINCIPAL))
        self.distancia_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.distancia_input)
        content.add_widget(Label(text="Tempo (s):", color=COR_PRINCIPAL))
        self.tempo_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.tempo_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_velocidade_media_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Velocidade Média',
                      content=content, size_hint=(None, None), size=(400, 300))
        popup.open()

    def calcular_velocidade_media_callback(self, instance):
        distancia = self.distancia_input.text
        tempo = self.tempo_input.text
        resultado = calcular_velocidade_media(distancia, tempo)
        if resultado is not None:
            popup_resultado = Popup(title='Resultado', content=Label(text=f'A velocidade média é {
                                    resultado:.2f} m/s', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        else:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira valores numéricos para distância e tempo.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

    def mostrar_popup_forca(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Massa (kg):", color=COR_PRINCIPAL))
        self.massa_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.massa_input)
        content.add_widget(
            Label(text="Aceleração (m/s^2):", color=COR_PRINCIPAL))
        self.aceleracao_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.aceleracao_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(
            on_press=self.calcular_forca_massa_aceleracao_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Força', content=content,
                      size_hint=(None, None), size=(300, 300))
        popup.open()

    def calcular_forca_massa_aceleracao_callback(self, instance):
        massa = self.massa_input.text
        aceleracao = self.aceleracao_input.text
        resultado = calcular_forca_massa_aceleracao(massa, aceleracao)
        if resultado is not None:
            popup_resultado = Popup(title='Resultado', content=Label(text=f'A força é {
                                    resultado} N', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        else:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira valores numéricos para massa e aceleração.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()


    def mostrar_popup_complexidade_ciclomatica(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text='Insira o código para calcular a Complexidade Ciclomática:', color=COR_PRINCIPAL))
        self.source_code_input = TextInput(
            multiline=True, background_color=COR_FUNDO, height=300)
        content.add_widget(self.source_code_input)

        button_calcular = Button(
            text='Calcular', background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_complexidade_ciclomatica_callback)
        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Complexidade Ciclomática',
                    content=content, size_hint=(None, None), size=(400, 400))
        popup.open()

    def calcular_complexidade_ciclomatica_callback(self, instance):
        source_code = self.source_code_input.text
        resultado = calcular_complexidade_ciclomatica(source_code)
        popup_resultado = Popup(title='Resultado', content=Label(
            text=f'A complexidade ciclomática é {resultado}', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
        popup_resultado.open()




    def mostrar_popup_bhaskara(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Coeficiente a:", color=COR_PRINCIPAL))
        self.coef_a_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.coef_a_input)
        content.add_widget(Label(text="Coeficiente b:", color=COR_PRINCIPAL))
        self.coef_b_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.coef_b_input)
        content.add_widget(Label(text="Coeficiente c:", color=COR_PRINCIPAL))
        self.coef_c_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.coef_c_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_bhaskara_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Bhaskara',
                        content=content, size_hint=(None, None), size=(400, 400))
        popup.open()



    def calcular_bhaskara_callback(self, instance):
        coef_a = self.coef_a_input.text
        coef_b = self.coef_b_input.text
        coef_c = self.coef_c_input.text

        resultado = bhaskara(coef_a, coef_b, coef_c)  # Chamando a função bhaskara do arquivo bhaskara.py

        popup_resultado = Popup(title='Resultado', content=Label(
            text=resultado, color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
        popup_resultado.open()



    def mostrar_popup_logaritmo(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Número:", color=COR_PRINCIPAL))
        self.num_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.num_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_logaritmo_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Logaritmo',
                    content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

    def calcular_logaritmo_callback(self, instance):
        num = self.num_input.text
        try:
            num = float(num)
            resultado = logaritmo(num)
            popup_resultado = Popup(title='Resultado', content=Label(
                text=f'O logaritmo de {num} é {resultado}', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        except ValueError:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira um número válido.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()


if __name__ == '__main__':
    CalculadoraApp().run()
