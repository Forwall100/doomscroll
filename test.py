import g4f
from g4f.Provider import H2o

print(g4f.Provider.Ails.params) # supported args

# Automatic selection of provider

# streamed completion
response = g4f.ChatCompletion.create(model='falcon-40b', messages=[
                                     {"role": "user", "content": "hello"}], stream=False, provider=H2o)

print(response)
