import pandas as pd

score, attempts = pd.read_excel('test_data.xlsx', sheet_name=['Score', 'Attemps']).values()
attempts = attempts.sort_values(by='Date', ascending=True).drop_duplicates(subset='Player', keep='last')
score_attempts = pd.merge(score, attempts, on='Player', how='inner')
score_attempts['Date'] = score_attempts['Date'].dt.strftime('%d.%m.%Y')
score_attempts['User'] = ["yaroslav.galitsyn@valuemont.com" for i in range(len(score_attempts))]

score_attempts.to_excel('result.xlsx', index=False)
