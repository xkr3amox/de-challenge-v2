# DE Challenge

This is the New Challenge for Data Engineers.

The EPL (English Premier League) had information of season between 09-10 and 18-19. They hire you as a DE to process the data per season to get some information relevant for the EPL and also send it for the teams and media involved.

For this Challenge: 
- We want you to do a Job who give us the Data for the Analytics team, but with a few concerns:
- The Job must be an ETL code in Java or Scala or Python.
- And we want a Deployment for this code.

Also we want an architecture proposition for this case:

La EPL al final de temporada entrega diversos premios a los jugadores y equipos, entre los que tenemos: equipo goleador, mejor entrenador, jugador goleador, arquero menos batido, al jugador con mas asistencias, al jugador que mas kilometros recorrió por partido jugado, "golden boy" (mejor jugador sub 20), entre otros.

Durante cada partido que se empieza a desarrollar, la EPL posee el registro de cada uno de los equipos involucrados (planilla de jugadores con nombre y apellido, dorsal, nombre del entrenador), los goles a favor y en contra antes del partido a jugarse y durante el transcurso del partido va registrando en tiempo real los disparos, disparos a puerta, goles, asistencias, faltas, tarjetas y tapadas de un portero. 

Cada jugador, por su parte, cuenta con un aparato que permite ver la distancia recorrida durante los minutos que estuvo en cancha, el agua perdida y los minutos de juego. Esta informacion es enviada en tiempo real a una central universal (dada por el proveedor de la herramienta) y enviada a cada uno de los centros de analisis de cada equipo para futuros analisis. 

La informacion del partido mas la de los jugadores es cruzada y enviada a los distintos sitios deportivos, en tiempo real, para tener la información del momento de cada partido disputado, asi como a las casas de apuestas para ir cambiando cada 5 minutos los % de apuesta a cada una de las alternativas que ofrecen. Proponga una arquitectura sobre la situacion planteada, de preferencia con herramientas open source.


# ETL Job

The job must receive the datasets & brings a few things:

The position table for all the seasons
*The other requeriments will be in the email

The data is in the folder data/ in the root. The report need to be exported to a file, you can chose the extension of the file, but remember this is an ETL Job.

Word Meaning

Name | Meaning
--- | --- 
DIV | division (E0, premier league)  
Date | date   
HOMETEAM | Equipo Local   
AWAYTEAM | Equipo Visita   
FTHG | Full Time Home Goals  
FTAG | Full Time Away Goals  
FTR | Full Time Result (H, A, D)[Home, Away, Draw] 
HTHG | Half Time Home Goals  
HTAG | Half Time Away Goals  
HTR | Half Time Result  
Referee | Arbitro   
HS | Home Shots   
AS | Away Shots   
HST | Home Shots Target  
AST | Away Shots Target  
HF | Home Fault   
AF | Away Faut   
HC | Home Card   
AC | Away Card   
HY | Home Yellow   
AY | Away Yellow   
HR | Home Red   
AR | Away Red

# Deployment
We want you to give us the way to deploy your job and run it in any environment, So please put the way to deploy very clearly.

## Concerns
- You can create a new README.md (choose a new name) for anything you want to tell us. Please don't name README.md
- We want to see if you know how to code in a professional way, so use the best practices of Software Engineering!.
- This is an ETL Job, so show us all you know about good practices to do ETL's.
- Save all the changes in your personal GitHub account using a Fork from this repository and send us the link to clone and see the repository.

### Disclaimer Note
"This challenge is your cover letter, the elections you choose to do & not to do matters!!, and will be ask in the next interview. If you don't get to finish the challenge, we will have to end your application"

## Datasets
Dataset for the challenge is inside folder "data"
