import flet as ft

def main(page):
    def checkbox_changed(e):
        t1.value = f"Checkbox value changed to {c_main.value}"
        t1.update()

    def button_clicked(e):
        t2.value = (
            f"Checkboxes values are: {c1.value}, {c2.value}, {c3.value}, {c4.value}, {c5.value}."
        )
        t2.update()

    c_main = ft.Checkbox(label="Checkbox with 'change' event", on_change=checkbox_changed)
    t1 = ft.Text()
    t2 = ft.Text()
    c1 = ft.Checkbox(label="Aceito os termos e condições", value=False)
    c2 = ft.Checkbox(label=" Checkbox mágico com estado indefinido", tristate=True)
    c3 = ft.Checkbox(label="Sim, quero receber notificações ", value=True)
    c4 = ft.Checkbox(label="Este checkbox está desativado ", disabled=True)
    c5 = ft.Checkbox(label=" Rótulo posicionado à esquerda", label_position=ft.LabelPosition.LEFT)
        
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)

    page.add(
        c_main,
        t1,
        c1,
        c2,
        c3,
        c4,
        c5,
        b,
        t2
    )

ft.app(main)


#anotaçoes uteis para estudos


#checkbox_changed(e): É chamada sempre que o valor do checkbox principal ( c_main ) muda. Atualiza o texto t1 para mostrar o novo valor do checkbox.
#button_clicked(e): É chamada quando o botão é clicado. Recupera os valores de todos os checkboxes e exibe-os no texto t2
#Checkbox Principal : Tem um evento on_changeque dispara a função checkbox_changedsempre que seu valor muda.
#Textos : t1e t2são usados ​​para exibir mensagens dinâmicas baseadas nas ações do usuário.
#Checkboxes Secundários : Cada um tem características diferentes:

#c1: Desmarcado por padrão.
#c2: tristate=Truepermite três estados: True , False , e None .
#c3: Marcado por padrão.
#c4: Desabilitado (não pode ser clicado).
#c5: Rótulo posicionado à esquerda.

#Botão : Dispara a função button_clickedpara verificar e exibir os valores das caixas de seleção.

#Adição de Componentes na Página Todos os componentes são adicionados à página na ordem especificada.(page add)
