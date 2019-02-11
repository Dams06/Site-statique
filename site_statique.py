import markdown2
import click

@click.command()
@click.option("--input_fichier", help = "fichier MD")
@click.option("--output_fichier", helps = "dossier html")

def convert(input_directory,output_fichier):
    input_fichier = open(input_directory, mode='r', encoding="utf-8")
    fichier = input_fichier.read()
    html = markdown2.markdown(fichier)

    output_fichier = output_fichier + "\index.html" 
    output_fichier2 = open(output_fichier, "w+", encoding="utf-8")
    output_fichier2.write('<!DOCTYPE html>\n<html>\n<head>\n<title> index </title>\n</head>\n<body>\n' + html + '</body>\n</html>')
    output_fichier2.close
    print("Bravo t'es moins nul que je le penser")
