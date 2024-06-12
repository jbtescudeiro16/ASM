# ASM-Gestão de porto marítimo

Este repositório contém o material utilizado na unidade curricular de **Agentes e Sistemas Multiagente**, inseirda no perfil de Sistemas Inteligentes no âmbito do Mestrado em Engenharia Informática.

O trabalho prático propunha a utilização da bilioteca SPADE para a construção de um sistema multiagente, baseado em agentes e na comunicação entre eles. Decidimos optar por construir um **porto Marítimo** em que os agentes principais são o Barco, o Farol, o gestor de cais e a Polícia Marítima

## Estrutura
O repositório está organizado da seguinte forma :
```
- Agents- Contém os ficheiros relacionados com agentes.

- Behaviours- Contém os ficheiros relacionados aos comportamentos dos agentes.

- Class- Contém os ficheiros referentes às classes auxiliares utilizadas na conceção da marina.

- Docs- Contém o relatório do TP, bem como o trabalho de investigação e as revisões feitas aos outros artigos.

- Marina.py- Script que inicializa e é responsável por fazer a Marina funcionar.

- README.md- Descrição do repositório.

- results.json- Ficheiro resultado que contém as informações do porto(total de partidas, chegadas e operações canceladas), depois de o programa acabar .

- settings.json- Contém as configurações utilizadas para dar início à Marina.
```
## Modo de Funcionamento

Para o processo de inicialização, é lido do ficheiro de confirguração, o número de barcos que se encontram atracados no cais e pretendem abandonar, o número de barcos que se encontram fora do porto e pretendem atracar, o número de canais que dão acesso ao porto, e o número de cais de cada tipo disponíveis para os barcos conseguirem atracar.

