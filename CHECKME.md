# DE Challenge
La solución se realizó en python usando la librería de Pandas para calcular toda la lógica de los reportes solicitados.
Se optó por este lenguaje y la librería para alinearse con lo solicitado y usar tecnologías open source.
También es un desafío personal, ya que mi experiencia se enfoca más en GCP y en muy pocas ocasiones puedo desarrollar sin usar los servicios que ofrece la plataforma

Existen muchos puntos de mejora sobre la solución a entregar, desde integrar pruebas, revisar para refactorizar, automatizar el rescate de archivos, entre otros. Sin embargo, el job realiza sus funciones
de manera clara y aprovechando los ciclos de la lectura archivo por archivo.

# Architecture Case

Para el problema planteado se ofrece una solución usando el ecosistema que ofrece Apache Kafka. Esto principalmente por la variedad de servicios que ofrecen al tratamineto de datos en streaming.
Sumado a eso, también se considera la integración de Kafka, que resulta rápida en la mayoría de los casos. Otro punto a considera fue que kafka permite realizar operaciones desde un tópico de entrada a uno de salida, ayudando a mantener
un flujo cercano al real-time.
También nos permite realizar analisis sobre los flujos que están integrados, ayudando al seguimiento de los procesos.


# Deployment
Las intrucciones para deployar el job se encuentran en el folder Deploy, en el archivo how-to-deploy.txt.