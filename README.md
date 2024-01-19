# Renomeador de Arquivos

Este é um simples script em Python projetado para renomear arquivos em um diretório específico. O script utiliza duas funções principais: `listar_arquivos` e `renomear_arquivo`.

## Como Usar

### Requisitos
- Python 3.x instalado

### Passos

1. Faça o download do script `renomear.py`.
2. Abra um terminal ou prompt de comando.
3. Navegue até o diretório onde o script está localizado.
4. Execute o script usando o comando `python renomear.py`.

### Personalização

- Você pode ajustar o diretório inicial modificando a variável `diretorio` no script.
- O script atualmente renomeia os arquivos usando um formato padrão: `{nome}S01E01.mkv`. Você pode personalizar o formato de renomeação ajustando a string passada para a função `renomear_arquivo`.

## Funções

### `listar_arquivos(diretorio: str) -> List`

Esta função lista os arquivos no diretório especificado, excluindo o próprio script (`renomear.py`). A lista resultante é ordenada alfabeticamente.

### `renomear_arquivo(caminho_atual: str, novo_nome: str) -> None`

Essa função renomeia um arquivo no caminho especificado para o novo nome fornecido. Antes de realizar a renomeação, verifica se o caminho atual e o novo caminho são diferentes para evitar renomear um arquivo para o mesmo nome.

## Exemplo de Uso

```python
if __name__ == "__main__":
    diretorio: str = './'
    arquivos: List = listar_arquivos('./')

    i: int = 1
    nome: str = ""  # nome da série

    for arq in arquivos:
        renomear_arquivo(f"./{arq}", f"{nome}S01E{i}.mkv")
        i += 1
```

Este exemplo renomeia os arquivos no diretório atual adicionando a sequência `S01E01`, `S01E02`, etc., ao nome da série fornecido. Certifique-se de ajustar a variável `nome` conforme necessário.

## Notas

- Certifique-se de ter backup dos arquivos antes de executar o script, especialmente se estiver usando-o em um diretório com arquivos importantes.
- Use este script com cuidado e apenas em diretórios onde você deseja aplicar a renomeação de arquivos de acordo com o padrão definido.
