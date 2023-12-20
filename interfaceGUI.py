import PySimpleGUI as psg
from bancodedados import conectar, read, create, update, delete

def listar_estudantes(con, window):
    cursor = con.cursor()

    query = '''SELECT * FROM estudante;'''

    try:
        cursor.execute(query)

        header = '----------------------------- LISTA DE ALUNOS -----------------------------\n'
        header += '\n         ------ Matrícula ------                ------ Nome ------\n\n'

        data = [f'               {campo[0]}                             {campo[1]} ' for campo in cursor.fetchall()]
        result = header + '\n'.join(data)

        window['lista_estudantes'].update(values=result.split('\n'))

    except (Exception) as error:
        print('Conectou mas não funcionou! ' + str(error))
    finally:
        cursor.close()

def main():
    psg.theme('Default1')

    layout = [
        [psg.Text('Matrícula:'), psg.InputText(key='matrícula')],
        [psg.Text('Nome:'), psg.InputText(key='nome')],
        [psg.Button('Inserir', button_color= ('white','darkblue')), psg.Button('Listar', button_color= ('white','darkblue')), psg.Button('Excluir', button_color= ('white','red')), psg.Button('Sair', button_color=('white', 'red'))],
        [psg.Listbox(values=[], size=(50, 10), key='lista_estudantes')],
    ]

    window = psg.Window('PySimpleGUI + MySQL', layout)

    con = conectar()

    while True:
        eventos, valores = window.read()

        if eventos == psg.WINDOW_CLOSED or eventos == 'Sair':
            break
        elif eventos == 'Inserir':
            matricula = valores['matrícula'].strip()
            nome = valores['nome'].strip()

            if matricula and nome:
                create(con, [(matricula, nome)])
                psg.popup('Estudante inserido com sucesso.', title='Sucesso')
            else:
                psg.popup('Por favor, informe a matrícula e o nome.', title='Erro')
        elif eventos == 'Excluir':
            delete(con, [(valores['matrícula'],)])
            psg.popup('Estudante excluído com sucesso.', title='Sucesso')
        elif eventos == 'Listar':
            listar_estudantes(con, window)

    window.close()

if __name__ == "__main__":
    main()
