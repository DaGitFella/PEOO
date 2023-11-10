class ManipulacaoArquivo:
    def __init__(self, Arquivo, modo = 'r', codificacao ='UTF-8') -> None:
        self.__arquivo = Arquivo
        self.__modo = modo
        self.__codificacao = codificacao
        self.lista = []
    
    def get_arquivo(self):
        print(self.__arquivo)

    def set_arquivo(self, novo_arquivo):
        self.__arquivo = novo_arquivo
    
    def get_modo(self):
        print(self.__modo)
    
    def set_modo(self, novo_modo):
        self.__modo = novo_modo
    
    def get_codificacao(self):
        print(self.__codificacao)
    
    def set_codificacao(self, nova_codificacao):
        self.__codificacao = nova_codificacao
    
    def obter_dados_arquivo(self):
        try:
            with open(self.__arquivo, self.__modo, encoding=self.__codificacao) as arquivo:
                for line in arquivo.readlines():
                    self.lista.append(line.replace('\n', ''))

                return self.lista
        except FileNotFoundError:
            return 'invalid path'
    
    def separar_dados(self):
        empty_list = []
        lista = self.obter_dados_arquivo()
        for line in lista:
            empty_list.extend(line.split())
        
        return empty_list
    
    def calc_media(self):
        dados = self.separar_dados()
        

    def exportar_calculo_media(self):
        pass
