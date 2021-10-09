climbing_parties_count: int = int(input())

climbing_parties: list = [0] * 5

for _ in range(climbing_parties_count):
    climbing_party_size: int = int(input())
    peak_index: int = (
        0 if 0 < climbing_party_size <= 5 else 
        1 if 6 <= climbing_party_size <= 12 else
        2 if 13 <= climbing_party_size <= 25 else
        3 if 26 <= climbing_party_size <= 40 else
        4
    )
    climbing_parties[peak_index]+=climbing_party_size

climbers: int = sum(climbing_parties)

for peak_party in climbing_parties:
    print(f'{peak_party/climbers*100:.2f}%')
