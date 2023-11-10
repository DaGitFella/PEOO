from classes import ManipulacaoArquivo

m = ManipulacaoArquivo(r'atividades\prática arquivos\alunos.txt')
print(m.obter_dados_arquivo())
print(m.separar_dados())
print(m.calc_media())
