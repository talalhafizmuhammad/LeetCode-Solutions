class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(players: Tuple[int], round: int) -> Tuple[int, int]:
            if firstPlayer not in players or secondPlayer not in players:
                return (float('inf'), -float('inf'))

            i = players.index(firstPlayer)
            j = players.index(secondPlayer)
            if i + j == len(players) - 1:
                return (round, round)

            next_rounds = set()

            def simulate(i, j, state, path):
                if i > j:
                    path_sorted = tuple(sorted(path))
                    next_rounds.add(path_sorted)
                    return

                if i == j:
                    simulate(i + 1, j - 1, state, path + [players[i]])
                else:
                    p1, p2 = players[i], players[j]
                    
                    if {p1, p2} == {firstPlayer, secondPlayer}:
                        return
                    if p1 in (firstPlayer, secondPlayer):
                        simulate(i + 1, j - 1, state, path + [p1])
                    elif p2 in (firstPlayer, secondPlayer):
                        simulate(i + 1, j - 1, state, path + [p2])
                    else:
                        simulate(i + 1, j - 1, state, path + [p1])
                        simulate(i + 1, j - 1, state, path + [p2])

            simulate(0, len(players) - 1, 0, [])

            min_round = float('inf')
            max_round = -float('inf')
            for nxt in next_rounds:
                a, b = dfs(nxt, round + 1)
                min_round = min(min_round, a)
                max_round = max(max_round, b)

            return (min_round, max_round)

        players = tuple(range(1, n + 1))
        return list(dfs(players, 1))
