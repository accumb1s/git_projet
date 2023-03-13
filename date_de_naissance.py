import datetime
import locale

# Définir la langue de l'interface utilisateur en français
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

# Demander la date de naissance à l'utilisateur
date_str = input("Entrez votre date de naissance (sous la forme jj/mm/aaaa) : ")

# Convertir la chaîne de caractères en objet datetime
date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')

# Trouver le jour de la semaine en français
jour_semaine = date_obj.strftime('%A')

# Afficher le résultat
print("Vous êtes né(e) un", jour_semaine)

# test
