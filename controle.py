from PyQt5 import uic, QtWidgets
import mysql.connector

banco =  mysql.connector.connect(
    host="localhost",
    user ="root",
    passwd="root",
    database="cadastro_produtos"
)

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ''

    if formulario.radioButton.isChecked():
        print('Categoria informatica foi selecionada')
        categoria = 'Informatica'
    elif formulario.radioButton_2.isChecked():
        print('Categoria alimentos foi selecionada')
        categoria = 'Alimentos'
    else:
        print('Categoria eletronicos foi selecionada')
        categoria = 'Eletronicos'


        
    print('codigo: ', linha1)
    print('descricao: ', linha2)
    print('preco: ', linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    formulario.lineEdit.setText('')
    formulario.lineEdit_2.setText('')
    formulario.lineEdit_3.setText('')

def chama_segunda_tela():
    segunda_tela.show()



app = QtWidgets.QApplication([])
formulario = uic.loadUi('formulario.ui')
segunda_tela = uic.loadUi('listar_dados.ui')
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)


formulario.show()
app.exec_()




