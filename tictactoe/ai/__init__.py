from minimax import optimal
from basic import random
from basic import random_blocker
from basic import random_winner


AI_DIFFICULTY = {
    1: random,
    2: random_blocker,
    3: random_winner,
    4: optimal,
}
