from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.graphics import RoundedRectangle
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty
from kivy.uix.textinput import TextInput
from funcoes import *
import math

COR_PRINCIPAL = (0.18, 0.33, 0.52, 1)
COR_SECUNDARIA = (0.96, 0.76, 0.32, 1)
COR_FUNDO = (0.9, 0.9, 0.9, 1)
COR_ROXA = (16/255, 127/255, 223/255, 1)  

class RoundedButton(Button):
    background_color = ListProperty(COR_ROXA)  

    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.border = [0.1, 1, 0.1, 1]

    def on_size(self, instance, value):
        if self.canvas:
            self.canvas.before.clear()
            with self.canvas.before:
                RoundedRectangle(pos=self.pos, size=self.size, radius=[10,])

class CalculadoraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=2)
        titulo = Label(text="Calculadora Moderna", font_size=36, color='#107fdf')
        
        layout.add_widget(titulo)

        button_velocidade_media = RoundedButton(
            text="Calcular Velocidade Média", size_hint_y=None, height=60)
        button_velocidade_media.bind(
            on_press=self.mostrar_popup_velocidade_media)
        button_velocidade_media.font_name = "Arial"
        button_velocidade_media.font_size = 18
        layout.add_widget(button_velocidade_media)

        button_forca = RoundedButton(
            text="Calcular Força", size_hint_y=None, height=60)
        button_forca.bind(on_press=self.mostrar_popup_forca)
        button_forca.font_name = "Arial"
        button_forca.font_size = 18
        layout.add_widget(button_forca)

        button_bhaskara = RoundedButton(
            text="Calcular Bhaskara", size_hint_y=None, height=60)
        button_bhaskara.bind(on_press=self.mostrar_popup_bhaskara)
        button_bhaskara.font_name = "Arial"
        button_bhaskara.font_size = 18
        layout.add_widget(button_bhaskara)

        button_logaritmo = RoundedButton(
            text="Calcular Log Simples", size_hint_y=None, height=60)
        button_logaritmo.bind(on_press=self.mostrar_popup_logaritmo)
        button_logaritmo.font_name = "Arial"
        button_logaritmo.font_size = 18
        layout.add_widget(button_logaritmo)

        button_seer = RoundedButton(
            text="Calcular Taxa de Erro de Software", size_hint_y=None, height=60)
        button_seer.bind(on_press=self.mostrar_popup_seer)
        button_seer.font_name = "Arial"
        button_seer.font_size = 18
        layout.add_widget(button_seer)

        button_seno = RoundedButton(
            text="Calcular Seno", size_hint_y=None, height=60)
        button_seno.bind(on_press=self.mostrar_popup_seno)
        button_seno.font_name = "Arial"
        button_seno.font_size = 18
        layout.add_widget(button_seno)

        button_cosseno = RoundedButton(
            text="Calcular Cosseno", size_hint_y=None, height=60)
        button_cosseno.bind(on_press=self.mostrar_popup_cosseno)
        button_cosseno.font_name = "Arial"
        button_cosseno.font_size = 18
        layout.add_widget(button_cosseno)

        button_exponencial = RoundedButton(
            text="Calcular Exponencial", size_hint_y=None, height=60)
        button_exponencial.bind(on_press=self.mostrar_popup_exponencial)
        button_exponencial.font_name = "Arial"
        button_exponencial.font_size = 18
        layout.add_widget(button_exponencial)

        button_log_natural = RoundedButton(
            text="Calcular Log Natural", size_hint_y=None, height=60)
        button_log_natural.bind(on_press=self.mostrar_popup_log_natural)
        button_log_natural.font_name = "Arial"
        button_log_natural.font_size = 18
        layout.add_widget(button_log_natural)

        button_equacao_movimento = RoundedButton(
            text="Calcular Equação de Movimento", size_hint_y=None, height=60)
        button_equacao_movimento.bind(on_press=self.mostrar_popup_equacao_movimento)
        button_equacao_movimento.font_name = "Arial"
        button_equacao_movimento.font_size = 18
        layout.add_widget(button_equacao_movimento)

        scrollview = ScrollView()
        scrollview.add_widget(layout)

        return scrollview
        
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
                text='Por favor, insira valores numéricos.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
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
                text='Por favor, insira valores numéricos.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

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

        resultado = bhaskara(coef_a, coef_b, coef_c)  

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
                    content=content, size_hint=(None, None), size=(400, 230))
        popup.open()

    def calcular_logaritmo_callback(self, instance):
        num = self.num_input.text
        try:
            num = float(num)
            resultado = math.log10(num)
            popup_resultado = Popup(title='Resultado', content=Label(
                text=f'O logaritmo de {num} é {resultado:.2f}', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        except ValueError:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira um número válido.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

    def mostrar_popup_seer(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Número de erros:", color=COR_PRINCIPAL))
        self.num_erros_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.num_erros_input)

        content.add_widget(Label(text="Linhas de Código:", color=COR_PRINCIPAL))
        self.linhas_codigo_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.linhas_codigo_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_seer_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular SEER',
                    content=content, size_hint=(None, None), size=(400, 300))
        popup.open()

    def calcular_seer_callback(self, instance):
        num_erros = self.num_erros_input.text
        linhas_codigo = self.linhas_codigo_input.text
        resultado = calcular_taxa_erro_software(num_erros, linhas_codigo)
        if resultado is not None:
            popup_resultado = Popup(title='Resultado', content=Label(
                text=f'A taxa de erro de software é {resultado:.2f}%', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        else:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira valores numéricos.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

    def mostrar_popup_seno(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Ângulo (em graus):", color=COR_PRINCIPAL))
        self.angulo_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.angulo_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_seno_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Seno',
                      content=content, size_hint=(None, None), size=(400, 350))
        popup.open()

    def calcular_seno_callback(self, instance):
        angulo = self.angulo_input.text
        try:
            angulo = float(angulo)
            resultado = math.sin(math.radians(angulo))  
            popup_resultado = Popup(title='Resultado', content=Label(
                text=f'O seno de {angulo}° é {resultado:.4f}', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        except ValueError:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira um ângulo válido.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

    def mostrar_popup_cosseno(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Ângulo (em graus):", color=COR_PRINCIPAL))
        self.angulo_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.angulo_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_cosseno_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Cosseno',
                      content=content, size_hint=(None, None), size=(400, 350))
        popup.open()

    def calcular_cosseno_callback(self, instance):
        angulo = self.angulo_input.text
        try:
            angulo = float(angulo)
            resultado = math.cos(math.radians(angulo)) 
            popup_resultado = Popup(title='Resultado', content=Label(
                text=f'O cosseno de {angulo}° é {resultado:.4f}', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        except ValueError:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira um ângulo válido.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

    def mostrar_popup_exponencial(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Base:", color=COR_PRINCIPAL))
        self.base_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.base_input)
        content.add_widget(Label(text="Expoente:", color=COR_PRINCIPAL))
        self.expoente_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.expoente_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_exponencial_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Exponencial',
                      content=content, size_hint=(None, None), size=(400, 350))
        popup.open()

    def calcular_exponencial_callback(self, instance):
        base = self.base_input.text
        expoente = self.expoente_input.text
        try:
            base = float(base)
            expoente = float(expoente)
            resultado = math.pow(base, expoente)
            popup_resultado = Popup(title='Resultado', content=Label(
                text=f'{base}^{expoente} = {resultado:.2f}', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        except ValueError:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira valores numéricos.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

    def mostrar_popup_log_natural(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Número:", color=COR_PRINCIPAL))
        self.num_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.num_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_log_natural_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Log Natural',
                    content=content, size_hint=(None, None), size=(400, 230))
        popup.open()

    def calcular_log_natural_callback(self, instance):
        num = self.num_input.text
        try:
            num = float(num)
            resultado = math.log(num)
            popup_resultado = Popup(title='Resultado', content=Label(
                text=f'O logaritmo natural de {num} é {resultado:.2f}', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        except ValueError:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira um número válido.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()

    def mostrar_popup_equacao_movimento(self, instance):
        content = BoxLayout(orientation='vertical', padding=10, spacing=5)
        content.add_widget(Label(text="Velocidade Inicial (m/s):", color=COR_PRINCIPAL))
        self.velocidade_inicial_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.velocidade_inicial_input)
        content.add_widget(Label(text="Aceleração (m/s^2):", color=COR_PRINCIPAL))
        self.aceleracao_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.aceleracao_input)
        content.add_widget(Label(text="Tempo (s):", color=COR_PRINCIPAL))
        self.tempo_input = TextInput(
            multiline=False, background_color=COR_FUNDO, height=50)
        content.add_widget(self.tempo_input)

        button_calcular = Button(
            text="Calcular", background_color=COR_PRINCIPAL, size_hint_y=None, height=50)
        button_calcular.bind(on_press=self.calcular_equacao_movimento_callback)

        content.add_widget(button_calcular)

        popup = Popup(title='Calcular Equação de Movimento',
                      content=content, size_hint=(None, None), size=(400, 350))
        popup.open()

    def calcular_equacao_movimento_callback(self, instance):
        velocidade_inicial = self.velocidade_inicial_input.text
        aceleracao = self.aceleracao_input.text
        tempo = self.tempo_input.text
        resultado = calcular_equacao_movimento(
            velocidade_inicial, aceleracao, tempo)
        if resultado is not None:
            popup_resultado = Popup(title='Resultado', content=Label(
                text=f'A posição final é {resultado:.2f} metros', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_resultado.open()
        else:
            popup_erro = Popup(title='Erro', content=Label(
                text='Por favor, insira valores numéricos.', color=COR_PRINCIPAL), size_hint=(None, None), size=(400, 200))
            popup_erro.open()



if __name__ == "__main__":
    CalculadoraApp().run()
