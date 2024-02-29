import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    df = pd.DataFrame(players)
    row, column = df.shape
    return [row, column]
    