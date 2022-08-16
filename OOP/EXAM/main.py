from project.horse_race_app import HorseRaceApp

horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Thoroughbred", "Bocket", 100))
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))

print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))

for hr in horseRaceApp.horce_races:
    print(hr.race_type)
    for j in hr.jockeys:
        print(j.name, j.age, j.horse.name, j.horse.speed)

for j in horseRaceApp.jockeys:
    print(j.name, j.age, j.horse.name, j.horse.speed)

for h in horseRaceApp.horses:
    print(h.name, h.speed, h.is_taken)
