# climatempodesafio
#Ler dois arquivos NetCDF com dados de temperatura, sendo um com dados de previsão e o outro com dados observados;
Para ler os arquivos netcdf primeiramente foram baixados os arquivos e guardados numa pasta do notebook e em seguida foram escritos os comando que permitem visualizar os dados (contidos Jupyter notebook) na qual permitiram visualizar os dados observados e previstas.

Calcular o índice RMSE para cada intervalo de 6 horas na série temporal em todos os pontos da matriz;
Nessa questao, primeiro foram transformados os arquivos netCDF em csv na qual permitiu observer os dados de cada variavel (temperaturas previstas e observadas) em seguida, foi feita um script na qual permitiu coincidir os dados (espacialmente e temporalmente). Depois disso, dividiu-se os mesmos dados em arquivos que variao de 6 em 6 horas, portanto, esses arquivos totalizaram 12, correspondente a 3 dias. Apos, calculou-se o indice RMSE a cada 6 horas.

Plotar mapas de duas dimensões do índice de cada período e um gráfico da série temporal do mesmo índice para São Paulo (Latitude -23.5489 e Longitude -46.6388, correspondente ao ponto Y: 8 e X: 26 na grade da matriz dos dados). Nessa questao, principalmente nas coordenadas oferecidas para a cidade de Sao Paulo, nao foram usados os mesmos dado que apos a coincidencia espacial e temporal descrita acima essas coordenadas ficaram isentas no arquivo CSV. Portanto, so podiria ser resolvida a questao se analisa-se os arquivos em netcdf usado daset ou mesmo Xarray. 
