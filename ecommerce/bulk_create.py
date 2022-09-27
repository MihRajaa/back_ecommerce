import csv

from adresse.models import Gouvernat, Ville


# Gouvernat.objects.all().delete()

# with open("E:/automate Python/adresse/region.csv", "r") as file:
#     data = dict(csv.reader(file, delimiter=",", quotechar='"'))
#     data = tuple(data)
#     try:
#         for row in data:
#             obj, create = Gouvernat.objects.get_or_create(name_gouv=row)
#     except:
#         pass

data = Gouvernat.objects.all()

# for row in data:
#     with open(f"E:/automate Python/adresse/manicipalite/{row.name_gouv.lower()}.csv", "r") as sub_file:
#         sub_data = dict(csv.reader(sub_file, delimiter=",", quotechar='"'))
#         sub_data = tuple(sub_data)

#         for r in sub_data:
#             obj, create = Ville.objects.get_or_create(
#                 name_ville=r, gouvernat_id=row.id)


# for row in Gouvernat.objects.all().reverse():
#     if Gouvernat.objects.filter(name_gouv=row.name_gouv).count() > 1:
#         row.delete()


with open("E:/automate Python/adresse/region.csv", "r") as file:
    reader = csv.DictReader(file)
    for r in data:
        for row in reader:
            Gouvernat.objects.filter(
                gouvernat=row['gouvernat']).update(code_iso=row['code_iso'], code_poste=row['code_poste'], coordonnees=row['coordonnees'])
